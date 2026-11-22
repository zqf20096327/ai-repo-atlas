# arihantsethia/clipport

⭐ 10 · Go · MIT · 推送 2026-10-15 · [GitHub](https://github.com/arihantsethia/clipport) · 个人维护

**把 Mac 剪贴板文本与截图粘贴进远程 iTerm SSH 会话的工具**

由 Go 编写的 macOS 命令行工具套件，包含 CLI、守护进程与菜单栏应用：通过 iTerm 快捷键 Cmd+Shift+V 读取本机剪贴板，文本直接粘贴到远程 shell，图片/截图经 SSH 上传并在远端插入 /tmp/clipport 路径；通过 OpenSSH LocalCommand 钩子或终端标题检测做会话匹配，上传文件以 0600 权限写入 0700 目录。另提供可选的远程剪贴板 shim（wl-paste/xclip 包装器）与令牌隧道模式。依赖 macOS、iTerm2、Homebrew 及免交互密码的 SSH 别名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一快捷键覆盖本地与远程 shell，按剪贴板内容自动选择粘贴行为
- 截图/图片经 SSH 上传至 /tmp/clipport 并以 0600/0700 权限写入
- 菜单栏应用监督守护进程，提供 clipctl doctor 诊断与 uninstall/更新命令
- 可选远程 shim 模式让远端程序经 SSH 隧道读取 Mac 剪贴板

## 适用场景

- 把本机截图路径粘贴进 VM 或远程服务器 shell
- 将本地图片交给远程命令处理而不手动 scp
- 在本地与 SSH 会话间保持统一的粘贴快捷键

## 场景标签

 · 领域:开发者工具/终端与剪贴板

## 证据(README 行号)

> L4:  Paste Mac clipboard text, images, and screenshots into remote iTerm SSH sessions.
> L11: Clipport lets you share images and screenshots over SSH without saving files by

## 星数曲线

```mermaid
xychart-beta
    title "arihantsethia/clipport 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 low · 依据 README sha `da85f4172032` · [字段定义](../../DATASET.md)*
