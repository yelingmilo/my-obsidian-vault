# Shell Commands 配置指南

## 插件安装

在 Obsidian 插件市场中搜索并安装 **Shell Commands** 插件。

## SSH 命令配置

安装插件后，在设置中添加以下命令：

### 命令 1: 在服务器运行 Python 脚本

- **名称**: Run Python on Server
- **命令**: `ssh hmy@10.16.113.209 'cd /data/milo && python3 {{input}}'`
- **提示**: 输入 Python 脚本名

### 命令 2: 在服务器运行可执行文件

- **名称**: Run C++/Binary on Server
- **命令**: `ssh hmy@10.16.113.209 'cd /data/milo && ./{{input}}'`
- **提示**: 输入可执行文件名

### 命令 3: 查看服务器任务状态

- **名称**: Check Server Processes
- **命令**: `ssh hmy@10.16.113.209 'ps aux | grep python'`

### 命令 4: 查看服务器磁盘使用

- **名称**: Check Server Disk Usage
- **命令**: `ssh hmy@10.16.113.209 'df -h /data/milo'`

### 命令 5: 同步本地代码到服务器

- **名称**: Sync Code to Server
- **命令**: `rsync -av --exclude='*.pyc' --exclude='__pycache__' {{input}} hmy@10.16.113.209:/data/milo/`
- **提示**: 输入本地代码目录路径

## 使用方式

在 Obsidian 笔记中或命令面板中输入 `Shell Commands:` 即可调用已配置的命令。

## 快捷方式

可以在设置中为每个命令绑定键盘快捷键，如 `Ctrl+Shift+P` 运行 Python。