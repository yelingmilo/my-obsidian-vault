import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import os

def create_video(trajectories, trap_positions, params, output_path):
    """
    生成粒子运动动画视频
    """
    print("生成视频...")
    
    # 参数
    fps = params['simulation']['fps']
    particle_radius = params['particle']['diameter'] / 2
    trap_radius = params['trap']['radius']
    
    # 图像范围
    x_min = trap_positions[:, 0].min() - 2e-6
    x_max = trap_positions[:, 0].max() + 2e-6
    y_min = trap_positions[:, 1].min() - 2e-6
    y_max = trap_positions[:, 1].max() + 2e-6
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(x_min * 1e6, x_max * 1e6)
    ax.set_ylim(y_min * 1e6, y_max * 1e6)
    ax.set_xlabel('x (μm)', fontsize=12)
    ax.set_ylabel('y (μm)', fontsize=12)
    ax.set_title('胶体粒子 Lieb 晶格 Langevin 动力学模拟', fontsize=14)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # 绘制光阱 (淡红色)
    trap_patches = []
    for i, pos in enumerate(trap_positions):
        trap = Circle((pos[0] * 1e6, pos[1] * 1e6), 
                      radius=trap_radius * 1e6, 
                      facecolor='lightcoral', 
                      edgecolor='red',
                      alpha=0.4,
                      linewidth=2)
        ax.add_patch(trap)
        trap_patches.append(trap)
    
    # 粒子
    particles = []
    for i in range(len(trajectories[0])):
        particle, = ax.plot([], [], 'o', markersize=12, 
                           markerfacecolor='steelblue',
                           markeredgecolor='navy',
                           markeredgewidth=2)
        particles.append(particle)
    
    # 粒子编号
    text_labels = []
    for i in range(len(trajectories[0])):
        text = ax.text(0, 0, str(i+1), fontsize=8, 
                      ha='center', va='center',
                      color='white', fontweight='bold')
        text_labels.append(text)
    
    # 时间文本
    time_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                       fontsize=12, verticalalignment='top')
    
    def init():
        for particle in particles:
            particle.set_data([], [])
        for text in text_labels:
            text.set_position((0, 0))
        time_text.set_text('')
        return particles + text_labels + [time_text]
    
    def animate(frame):
        pos = trajectories[frame]
        t = frame / fps
        
        for i, (particle, text) in enumerate(zip(particles, text_labels)):
            x = pos[i, 0] * 1e6
            y = pos[i, 1] * 1e6
            particle.set_data([x], [y])
            text.set_position((x, y))
        
        time_text.set_text(f't = {t:.2f} s')
        return particles + text_labels + [time_text]
    
    # 创建动画
    n_frames = len(trajectories)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=1000/fps,
                                   blit=True)
    
    # 保存
    print(f"保存视频到: {output_path}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    anim.save(output_path, writer='ffmpeg', fps=fps, dpi=100)
    plt.close()
    
    print("视频生成完成!")

def plot_eigenmodes(eigenvalues, eigenvectors, trap_positions, params, output_dir):
    """绘制本征模式"""
    print("绘制本征模式...")
    
    particle_radius = params['particle']['diameter'] / 2
    
    # 前几个慢模式
    n_modes = min(6, len(eigenvalues))
    
    for mode_idx in range(n_modes):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # 光阱位置
        for pos in trap_positions:
            trap = Circle((pos[0] * 1e6, pos[1] * 1e6), 
                          radius=params['trap']['radius'] * 1e6,
                          facecolor='lightcoral', alpha=0.3)
            ax.add_patch(trap)
        
        # 本征向量 (取 x 分量)
        mode = eigenvectors[:, mode_idx]
        for i in range(len(trap_positions)):
            x = trap_positions[i, 0] * 1e6
            y = trap_positions[i, 1] * 1e6
            dx = mode[2*i] * 10
            dy = mode[2*i+1] * 10
            ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.05, 
                    fc='navy', ec='navy')
        
        ax.set_xlim(trap_positions[:, 0].min() * 1e6 - 2,
                   trap_positions[:, 0].max() * 1e6 + 2)
        ax.set_ylim(trap_positions[:, 1].min() * 1e6 - 2,
                   trap_positions[:, 1].max() * 1e6 + 2)
        ax.set_xlabel('x (μm)')
        ax.set_ylabel('y (μm)')
        ax.set_title(f'本征模式 {mode_idx+1}: λ = {eigenvalues[mode_idx]:.4e}')
        ax.set_aspect('equal')
        
        save_path = os.path.join(output_dir, f'eigenmode_{mode_idx+1}.png')
        plt.savefig(save_path, dpi=150)
        plt.close()
    
    print(f"本征模式图保存到: {output_dir}")