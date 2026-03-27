# 服务器运行指南

## 快速启动命令

```bash
# 1. SSH 到服务器
ssh hmy@10.16.113.209

# 2. 进入目录
cd /data/milo/oc/simulation/colloidal_lieb

# 3. 运行模拟
python scripts/run.py
```

## 预计运行时间

- 模拟时长: ~2-5 分钟 (取决于服务器性能)
- 视频生成: ~30 秒
- 总计: ~5 分钟

## 检查运行状态

```bash
# 查看正在运行的 Python 进程
ps aux | grep python

# 实时查看输出 (可选)
python scripts/run.py 2>&1 | tee run.log
```

## 输出文件位置

```
/data/milo/oc/simulation/260327/
├── trajectory.npz
├── eigenmodes.npz
└── simulation.mp4
```

## 下载结果到本地

```bash
# 从服务器下载结果到本地 (本地执行)
scp hmy@10.16.113.209:/data/milo/oc/simulation/260327/* Y:/milo/oc/simulation/260327/
```

## 常见问题

1. **缺少 ffmpeg**: `sudo apt install ffmpeg`
2. **缺少 Python 包**: `pip install numpy matplotlib pyyaml`
3. **内存不足**: 减少帧数或缩短时长