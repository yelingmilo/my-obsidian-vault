# Kanban 看板配置指南

## 插件安装

在 Obsidian 插件市场中搜索并安装 **Kanban** 插件。

## 快速开始

1. 创建一个新笔记，命名为 `Project_Kanban.md`
2. 在笔记中添加：

```markdown
---
kanban-plugin: basic
---

## 项目看板

- [ ] **Backlog** 待验证的想法
  - [[想法1]]
  - [[想法2]]
- [ ] **In Progress** 正在进行的任务
  - [[任务A]]
- [ ] **Done** 已完成
  - [[任务B]]
```

## 项目进度看板示例

```markdown
## 🔬 Cluster Paper 项目进度

- [ ] **Backlog** 
  - [[调研新型光阱阵列设计]]
  - [[阅读相关文献]]
- [ ] **Running** 正在模拟
  - [[Main_simulation|参数扫描任务]] (PID: 12345)
- [ ] **Analysis** 数据分析中
  - [[分析第一组数据]]
- [ ] **Writing** 撰写中
  - [[Methods 部分]]
- [ ] **Done** 已完成
  - [[实验参数记录]]
```

## 与项目关联

在项目主页笔记中添加看板，快速查看项目状态。

## 快捷键

- `Ctrl+Shift+K` 打开看板视图
- 拖拽卡片切换状态