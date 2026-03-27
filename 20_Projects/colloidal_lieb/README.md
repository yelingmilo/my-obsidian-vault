# 胶体粒子 Lieb 晶格 Langevin 动力学模拟

## 概述

模拟 21 个胶体粒子在 Lieb 晶格光阱中的过阻尼 Langevin 动力学。

## 物理模型

- **动力学**: 过阻尼郎之万方程 $\gamma \dot{\mathbf{r}} = -\nabla U + \sqrt{2\gamma k_B T} \eta(t)$
- **粒子相互作用**: Lennard-Jones 势
- **光阱势能**: 高斯势

## 参数

| 参数 | 值 |
|------|-----|
| 粒子直径 | 2 μm |
| 光阱数 | 21 (Lieb 晶格) |
| 光阱间距 | 3 μm |
| 溶液粘度 | 5 mPa·s (CMC 0.75 mg/mL) |
| 光阱刚度 | 0.5 pN/nm |
| 模拟时长 | 5 秒 |
| 帧率 | 30 fps |

## 运行方式

### 方式 1: 本地运行 (Windows)

```bash
cd D:\files\notebook\my_vault\20_Projects\colloidal_lieb
python scripts/run.py
```

需要安装:
```bash
pip install numpy matplotlib pyyaml
```

### 方式 2: 服务器运行 (Linux)

1. 上传代码到服务器:
```bash
rsync -av --exclude='__pycache__' D:/files/notebook/my_vault/20_Projects/colloidal_lieb/ hmy@10.16.113.209:/data/milo/oc/simulation/colloidal_lieb/
```

2. SSH 到服务器:
```bash
ssh hmy@10.16.113.209
```

3. 运行:
```bash
cd /data/milo/oc/simulation/colloidal_lieb
pip install numpy matplotlib pyyaml
python scripts/run.py
```

### 方式 3: VS Code Remote

1. 打开 VS Code
2. `Ctrl+Shift+P` → `Remote-SSH: Connect to Host`
3. 输入 `hmy@10.16.113.209`
4. 打开 `/data/milo/oc/simulation/colloidal_lieb/`
5. 运行 `python scripts/run.py`

## 输出

运行后会在 `/data/milo/oc/simulation/260327/` 目录下生成:

| 文件 | 说明 |
|------|------|
| `trajectory.npz` | 粒子轨迹数据 |
| `eigenmodes.npz` | 本征值和本征向量 |
| `simulation.mp4` | 稳态动画视频 |
| `eigenmode_*.png` | 本征模式图 |

## 本征值解读

动力学矩阵 $J_{ij} = \partial F_i / \partial r_j$ 的本征值:

- **λ ≈ 0**: Goldstone 模式 (平移对称性)
- **λ > 0**: 稳定模式 (衰减)
- **λ < 0**: 不稳定模式 (放大)

模拟应该所有模式都稳定 (λ > 0)，弛豫到稳态。

## 注意事项

1. 首次运行可能需要几分钟 (5×10⁶ 步)
2. 确保服务器有足够的计算资源
3. 视频生成需要 ffmpeg
4. 如果粒子飞出光阱区域，检查参数是否合理