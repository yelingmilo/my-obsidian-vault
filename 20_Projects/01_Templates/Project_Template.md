# 项目主页模板

## 项目信息

- **项目名称**: 
- **开始日期**: 
- **目标**: 

## 研究内容

### 目标
>

### 方法
>

## 代码

| 类型 | 路径 |
|------|------|
| 本地代码 | `code_link` |
| 服务器代码 | `server_path` |

## 实验日志

```dataview
LIST
FROM "20_Projects/项目名"
WHERE contains(tags, "log")
SORT file.ctime desc
LIMIT 10
```

## 进度看板

```markdown
- [ ] **Backlog** 
- [ ] **Running**
- [ ] **Analysis**
- [ ] **Writing**
- [ ] **Done**
```

## 参考文献

```dataview
LIST
FROM "10_Literature"
WHERE contains(project, "项目名")
```

## 讨论区

> 记录讨论要点和下一步计划