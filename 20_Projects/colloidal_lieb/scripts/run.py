import numpy as np
import yaml
import os
from pathlib import Path

def load_params(param_file='params.yaml'):
    with open(param_file, 'r') as f:
        return yaml.safe_load(f)

def create_lieb_lattice(spacing, center=(0, 0)):
    """
    创建 Lieb 晶格光阱位置
    结构: 5 + 3 + 5 + 3 + 5 = 21 个光阱
    """
    positions = []
    row_offsets = [0, 0.5 * spacing, 0, 0.5 * spacing, 0]
    row_widths = [5, 3, 5, 3, 5]
    
    for i, (offset, width) in enumerate(zip(row_offsets, row_widths)):
        y = center[1] + (i - 2) * spacing
        x_start = center[0] - (width - 1) * spacing / 2 + offset
        for j in range(width):
            x = x_start + j * spacing
            positions.append(np.array([x, y]))
    
    return np.array(positions)

def lj_potential(r, sigma, epsilon):
    """Lennard-Jones 势能"""
    r = np.maximum(r, sigma * 0.8)
    inv_r6 = (sigma / r) ** 6
    return 4 * epsilon * (inv_r6 ** 2 - inv_r6)

def lj_force(r_vec, sigma, epsilon):
    """Lennard-Jones 力"""
    r = np.linalg.norm(r_vec)
    if r < 1e-10:
        return np.zeros(2)
    r = max(r, sigma * 0.8)
    inv_r = sigma / r
    inv_r6 = inv_r ** 6
    magnitude = 24 * epsilon * (2 * inv_r6 ** 2 - inv_r6) / r
    return magnitude * r_vec / r

def gaussian_trap_potential(r, r0, V0, w):
    """高斯光阱势能"""
    return V0 * np.exp(-np.linalg.norm(r - r0) ** 2 / (2 * w ** 2))

def gaussian_trap_force(r, r0, V0, w):
    """高斯光阱力 = -grad V"""
    dr = r - r0
    dist_sq = np.linalg.norm(dr) ** 2
    if dist_sq < 1e-10:
        return np.zeros(2)
    return (V0 / w ** 2) * np.exp(-dist_sq / (2 * w ** 2)) * dr

def compute_total_force(positions, trap_positions, trap_params, lj_params, kBT):
    """计算所有粒子受到的力"""
    N = len(positions)
    forces = np.zeros((N, 2))
    
    # 光阱力
    for i in range(N):
        for j, trap_pos in enumerate(trap_positions):
            f_trap = gaussian_trap_force(positions[i], trap_pos, 
                                        trap_params['depth'] * kBT, 
                                        trap_params['radius'])
            forces[i] += f_trap
    
    # LJ 相互作用力
    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[j] - positions[i]
            f_lj = lj_force(r_vec, lj_params['sigma'], lj_params['epsilon'] * kBT)
            forces[i] += f_lj
            forces[j] -= f_lj
    
    return forces

def compute_dynamics_matrix(positions, trap_positions, trap_params, lj_params, kBT, eps=1e-8):
    """
    计算动力学矩阵 J_ij = dF_i / dr_j
    """
    N = len(positions)
    J = np.zeros((2 * N, 2 * N))
    
    for i in range(N):
        for dim in range(2):
            idx = 2 * i + dim
            r_plus = positions.copy()
            r_plus[i, dim] += eps
            r_minus = positions.copy()
            r_minus[i, dim] -= eps
            
            f_plus = compute_total_force(r_plus, trap_positions, trap_params, lj_params, kBT)
            f_minus = compute_total_force(r_minus, trap_positions, trap_params, lj_params, kBT)
            
            J[:, idx] = (f_plus[:, dim] - f_minus[:, dim]) / (2 * eps)
    
    return J

def run_simulation(params):
    """运行主模拟"""
    print("=" * 50)
    print("胶体粒子 Lieb 晶格 Langevin 动力学模拟")
    print("=" * 50)
    
    # 物理常数
    kBT = 1.380649e-23 * params['fluid']['temperature']
    
    # 阻力系数 (Stokes)
    gamma = 6 * np.pi * params['fluid']['viscosity'] * (params['particle']['diameter'] / 2)
    print(f"阻力系数 γ = {gamma:.2e} N·s/m")
    
    # 时间参数
    dt = params['simulation']['dt']
    total_steps = int(params['simulation']['total_time'] / dt)
    eq_steps = int(params['simulation']['equilibration'] / dt)
    fps = params['simulation']['fps']
    frames = int(params['simulation']['total_time'] * fps)
    save_interval = total_steps // frames
    
    print(f"总步数: {total_steps}")
    print(f"弛豫步数: {eq_steps}")
    print(f"保存间隔: {save_interval}")
    
    # 创建光阱位置
    trap_positions = create_lieb_lattice(params['trap']['spacing'])
    N = len(trap_positions)
    print(f"光阱/粒子数: {N}")
    
    # 初始化粒子位置 (小扰动)
    np.random.seed(params['simulation']['seed'])
    positions = trap_positions + np.random.uniform(-0.1e-6, 0.1e-6, (N, 2))
    
    # 存储轨迹
    trajectories = np.zeros((frames, N, 2))
    frame_idx = 0
    
    # Langevin 模拟
    print("\n开始模拟...")
    sqrt_dt = np.sqrt(dt)
    sqrt_2gamma_kBT = np.sqrt(2 * gamma * kBT)
    
    for step in range(total_steps):
        # 计算力
        forces = compute_total_force(positions, trap_positions, 
                                    params['trap'], params['lj'], kBT)
        
        # 朗之万方程: dr/dt = F/gamma + noise/gamma
        noise = np.random.normal(0, 1, (N, 2))
        dr = (forces / gamma + sqrt_2gamma_kBT * noise / gamma) * dt
        
        # 位置更新 (Euler)
        positions += dr
        
        # 保存帧
        if step >= eq_steps and (step - eq_steps) % save_interval == 0:
            trajectories[frame_idx] = positions.copy()
            frame_idx += 1
            if frame_idx % 20 == 0:
                print(f"  进度: {frame_idx}/{frames} 帧")
    
    print("模拟完成!")
    
    # 计算动力学矩阵 (稳态)
    print("\n计算动力学矩阵...")
    final_positions = trajectories[-1]
    J = compute_dynamics_matrix(final_positions, trap_positions, 
                                params['trap'], params['lj'], kBT)
    
    # 对角化
    eigenvalues, eigenvectors = np.linalg.eig(J)
    eigenvalues = eigenvalues.real
    eigenvectors = eigenvectors.real
    
    # 排序
    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[idx]
    
    print("本征值 (前10个):")
    for i in range(min(10, len(eigenvalues))):
        print(f"  λ_{i} = {eigenvalues[i]:.4e}")
    
    return trajectories, trap_positions, eigenvalues, eigenvectors, params

def main():
    # 创建输出目录
    output_dir = Path(params['output']['base_dir'])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 运行模拟
    trajectories, trap_positions, eigenvalues, eigenvectors, params = run_simulation(params)
    
    # 保存结果
    np.savez(output_dir / params['output']['trajectory'],
             trajectories=trajectories,
             trap_positions=trap_positions,
             dt=params['simulation']['dt'])
    
    np.savez(output_dir / params['output']['eigenmodes'],
             eigenvalues=eigenvalues,
             eigenvectors=eigenvectors)
    
    print(f"\n结果保存到: {output_dir}")
    
    # 生成视频
    from visualization import create_video
    create_video(trajectories, trap_positions, params, output_dir / params['output']['video'])
    
    print("完成!")

if __name__ == "__main__":
    params = load_params('params.yaml')
    main()