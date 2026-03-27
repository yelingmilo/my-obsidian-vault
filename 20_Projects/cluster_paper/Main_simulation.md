# Main code
```Python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1

# ==============================================================================
# 1. 核心函数定义
# ==============================================================================

def simulate_single_trajectory_PHASE_INTEGRAL(
    epsilon: float, N: float = 6.0, M: float = 12.0, L: float = 18.0,
    omega_base: float = 0.4, A_0: float = 10.0, A_flu:float = 0.0, D: float = 0.005, yw: float = 0.7,R: float = 6.7,
    x0: float = 0.12, t_span: tuple[float, float] = (0, 300),
    dt: float = 0.001, seed: int | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """
    数值模拟核心函数：计算粒子在周期性势场中的轨迹
    """
    if seed is not None: np.random.seed(seed)
    
    # 时间步进
    n_steps = int((t_span[1] - t_span[0]) / dt)
    t = np.linspace(t_span[0], t_span[1], n_steps + 1)
    
    # 初始化轨迹数组
    x_stoch = np.zeros(n_steps + 1)
    x_stoch[0] = x0
    
    # --- 物理系数计算 ---
    k = np.array([M, L, M + L, M - L])
    values = [M/N, L/N, (M+L)/N, (M-L)/N]
    delta = np.array([int(v.is_integer()) for v in values])
    
    # 高斯包络参数
    # R = 6.7
    B_factor = np.array([np.exp(-(v*yw/R)**2) for v in [M, L, M+L, M-L]])
    
    # #### Bessel 函数项 (模拟光镊势场强度)
    bessel_terms = np.array([
        2*M*2*N/(M*np.pi)*j1(M*np.pi/N),
        L*2*N/(L*np.pi)*j1(L*np.pi/N),
        (M+L)*2*N/((M+L)*np.pi)*j1((M+L)*np.pi/N),
        (M-L)*2*N/((M-L)*np.pi)*j1((M-L)*np.pi/N)
    ])
    # 综合振幅
    A_factor_const = np.abs(B_factor * delta * A_0 * bessel_terms)

    # print(A_factor_const[0], A_factor_const[3],A_factor_const[0]/A_factor_const[3])
    w_ratios = np.array([1.0, 0.0, M/(M+L), M/(M-L)])
    epsilon_factor = np.array([1.0, epsilon, epsilon, epsilon])
    A = A_factor_const * epsilon_factor
    # print(A)
    phase_accum = np.zeros_like(k, dtype=float)
    
    # 噪声项
    sqrt_2D_dt = np.sqrt(2 * D * dt)
    stoch_noise = np.random.normal(0, 1, n_steps) * sqrt_2D_dt
    
    # --- 时间积分循环 (Euler-Maruyama) ---
    for i in range(n_steps):
        # 驱动频率可能带有微小波动 A_flu
        omega_t = omega_base * (1.0 + A_flu * np.cos(2 * np.pi * 0.05 * t[i]))
        
        # 相位累积
        phase_accum += w_ratios * omega_t * dt
        
        # 计算受力: F = -dV/dx
        force = -np.sum(A * np.sin(k * x_stoch[i] - k * phase_accum))
        
        # 更新位置
        x_stoch[i+1] = x_stoch[i] + force * dt + stoch_noise[i]
    
    return t, x_stoch

def calculate_nm_ratio(t_data, theta_data, omega_val):
    """
    计算合成维度中的斜率比率 (Ratio = dn/dm)
    """
    # 计算合成维度坐标 n(t) 和 m(t)
    n_traj = -(theta_data - omega_val * t_data + np.pi/12*np.cos(omega_val*t_data)+0.15) * 6 / np.pi
    m_traj = (theta_data + 2 * omega_val * t_data + np.pi/12*np.cos(2*omega_val*t_data)+0.3) * 3 / np.pi

    delta_n = np.abs(n_traj[-1] - n_traj[0])
    delta_m = np.abs(m_traj[-1] - m_traj[0])
    
    return np.arctan(delta_m / delta_n)

# ==============================================================================
# 2. 运行数值模拟 (Simulation)
# ==============================================================================

# 配置参数
OMEGA_BASE = 0.842 
Y_OFFSET = 0.0
sim_eps_values = np.linspace(0.01, 0.40, 100) # 模拟范围和点数

print(f"--- 正在运行数值模拟 (Omega={OMEGA_BASE}) ---")
eps_sim_list = []
ratio_sim_list = []

for eps in sim_eps_values:
    # 运行单次模拟
    t_sim, theta_sim = simulate_single_trajectory_PHASE_INTEGRAL(
        epsilon=eps, t_span=(0, np.pi*60), dt=0.01,
        omega_base=OMEGA_BASE, A_0=19, D=0.0, yw=0.74, R=5 # D=0.0 表示无噪声确定性模拟
    )
    
    # 计算 Ratio
    ratio = calculate_nm_ratio(t_sim, theta_sim, OMEGA_BASE)
    
    if ratio is not None:
        eps_sim_list.append(eps)
        ratio_sim_list.append(ratio)

print(f"✅ 模拟数据就绪: {len(eps_sim_list)} 个样本")

# ==============================================================================
# 3. 绘图
# ==============================================================================

# 全局绘图风格设置
plt.rcParams.update({
    'font.size': 15, 'axes.titlesize': 18, 'axes.labelsize': 20,
    'xtick.labelsize': 15, 'ytick.labelsize': 15, 'legend.fontsize': 14,
    'lines.linewidth': 2.5, 'grid.linewidth': 1.5, 'font.family': 'sans-serif'
})

# 创建画布
fig, ax = plt.subplots(figsize=(7, 6))

# --- 绘制模拟数据 (红色实线) ---
if len(eps_sim_list) > 0:
    x_sim = np.array(eps_sim_list)
    y_sim = np.array(ratio_sim_list) + Y_OFFSET # 应用偏移量
    
    ax.plot(x_sim, y_sim, '-', color='#D32F2F', linewidth=3, alpha=0.9, 
            label='Simulation', zorder=4)

# --- 轴标签与范围 ---
ax.set_xlabel(r'$\epsilon$', fontsize=28)
ax.set_ylabel(r'$\Delta n^{(1)}/\Delta n^{(4)}$', fontsize=28)

# 自动调整范围
ax.set_ylim(-0.1, 2)
ax.set_xlim(0, 0.4)

# 指定刻度
ax.set_yticks([0, 1, 2, 3, 4, 5]) 
ax.tick_params(axis='y', labelsize=26)
ax.tick_params(axis='x', labelsize=26)

# 图例
ax.legend(loc='upper left', frameon=True, shadow=True, fontsize=24)

plt.tight_layout()
plt.show()
```