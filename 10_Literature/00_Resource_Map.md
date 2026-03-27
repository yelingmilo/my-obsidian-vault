# 资源路径映射表

## 本地资源

| 类型 | 路径 |
|------|------|
| **NAS** | `Y:\milo\` |
| **Obsidian 库** | `D:\files\notebook\my_vault\` |

## 服务器资源

| 类型 | 路径 | 说明 |
|------|------|------|
| **SSH** | `ssh hmy@10.16.113.209` | 登录命令 |
| **用户目录** | `/home/hmy/` | SSH 登录后主目录 |
| **NAS 挂载** | `/data/milo/` | 服务器上 NAS 挂载点 |

## 快速链接

- **VS Code Remote**: [打开服务器](vscode://ssh-remote+10.16.113.209/home/hmy)
- **本地 NAS**: [打开](file:///Y:/milo)

## 代码目录结构（建议）

```
本地代码仓库/
├── colloids/           # 胶体物理模拟
│   ├── src/
│   ├── scripts/
│   └── results/
├── mbl/                # 多体局域化
│   ├── src/
│   └── analysis/
└── general/            # 通用工具
    └── utils/
```

## 笔记 YAML 属性规范

在代码相关笔记中添加：

```yaml
---
code_link: vscode://file///D:/path/to/local/code
server_path: /home/hmy/project_name
tags: [code/simulation]
---
```