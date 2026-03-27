VS Code SSH 免密登录与防断连配置指南
1. 解决频繁断开 (KeepAlive)
修改本地 SSH 配置文件（VS Code 中按 `F1` -> `Remote-SSH: Open SSH Configuration File`）：

```

Host 10.16.113.209

    HostName 10.16.113.209

    User hmy

    # 添加以下两行保持心跳

    ServerAliveInterval 60

    ServerAliveCountMax 5

```

2. 解决反复输密码 (免密登录)
在 Windows PowerShell 中按顺序执行以下步骤：

第一步：生成本地密钥

如果以前没生成过，运行此命令并一路回车：

```

ssh-keygen -t rsa

```

第二步：创建服务器目录（修复报错关键）

防止出现 `No such file` 错误，先创建目录并给与正确权限（需输一次密码）：

```

ssh hmy@10.16.113.209 "mkdir -p ~/.ssh && chmod 700 ~/.ssh"

```

第三步：上传公钥

将本地公钥写入服务器，并设置文件权限（需输最后一次密码）：

```

type $env:USERPROFILE\.ssh\id_rsa.pub | ssh hmy@10.16.113.209 "cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

```

3. 验证
重启 VS Code，应不再提示输入密码，且连接更稳定。