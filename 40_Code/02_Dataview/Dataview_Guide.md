# Dataview 配置与使用指南

## 插件安装

在 Obsidian 插件市场中搜索并安装 **Dataview** 插件。

## 基本设置

在 Obsidian 设置中启用：
- ✅ Enable Inline Fields
- ✅ Enable JavaScript Queries

## 常用查询示例

### 1. 显示今日 Daily Notes

```
```dataview
LIST
FROM "00_Inbox"
WHERE date = date(today)
SORT file.mday desc
```
```

### 2. 显示所有论文笔记

```
```dataview
LIST
FROM "10_Literature"
WHERE contains(tags, "literature")
SORT date_added desc
```
```

### 3. 显示项目中的代码笔记

```
```dataview
LIST
FROM "20_Projects"
WHERE contains(tags, "code/simulation")
```
```

### 4. 显示特定项目的实验日志

```
```dataview
LIST
FROM "20_Projects/cluster_paper"
WHERE contains(tags, "log")
SORT file.ctime desc
```
```

### 5. 显示需要处理的文献

```
```dataview
TABLE title, authors, year
FROM "10_Literature"
WHERE !contains(tags, "read")
SORT year desc
```
```

## YAML 属性规范

在笔记中添加以下属性：

```yaml
---
title: 笔记标题
date: 2024-01-01
tags: [tag1, tag2]
project: 项目名
code_link: vscode://file/path
---
```

## 自动汇总项目主页

在项目笔记中添加：

```
## 📋 相关笔记

```dataview
LIST
FROM "20_Projects/cluster_paper"
```
```

## 链接到 Dataview 文档

- [官方文档](https://blackgu.gitbook.io/dataview/)
- [查询语法](https://blackgu.gitbook.io/dataview/query/queries)