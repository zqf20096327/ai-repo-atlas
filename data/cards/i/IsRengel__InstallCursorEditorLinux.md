# IsRengel/InstallCursorEditorLinux

⭐ 157 · Shell · Apache-2.0 · 推送 2026-01-21 · [GitHub](https://github.com/IsRengel/InstallCursorEditorLinux) · 个人维护

**Linux 上安装 Cursor AI 代码编辑器的 Bash 安装脚本（已弃用）**

一个 Bash 安装脚本与指南，用于将 Cursor AI Code Editor 以桌面应用形式安装到各 Linux 发行版：下载 Cursor、写入 .desktop 文件、默认安装到 /opt/cursor/，并配置基于 systemd 的自动更新服务。README 顶部声明弃用通知：Cursor 已提供官方 .deb 包，该安装器不再必要，仓库仅保留作历史与教育用途。运行前需系统已装 git、curl、bash。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令克隆并运行 install.sh 完成 Cursor 桌面安装
- 配置 systemd 服务实现自动更新
- 覆盖 Debian/Arch/Fedora/openSUSE/Gentoo/Solus 等发行版的依赖安装说明
- 支持 cursor --uninstall 或手动清理卸载

## 适用场景

- 在任意 Linux 发行版上把 Cursor 安装为桌面应用
- 让 Cursor 通过 systemd 服务自动更新
- 学习 AppImage 转 .desktop 集成的安装脚本写法

## 场景标签

 · 领域:开发工具/安装脚本

## 证据(README 行号)

> L16: This guide helps you install **Cursor AI Code Editor** as a desktop application on Linux operating systems, regardl
> L20: Cursor IDE is an AI-powered code editor, built on the foundations of Visual Studio Code and enhanced with ChatGPT i
> L86: git clone https://github.com/IsRengel/InstallCursorEditorLinux.git --depth=1 && cd InstallCursorEditorLinux && ./in

## 星数曲线

```mermaid
xychart-beta
    title "IsRengel/InstallCursorEditorLinux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 156 --> 159
    line [158, 157]
```

2026-10-18 158 → 2026-10-25 157（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1b90f9bb8853` · [字段定义](../../DATASET.md)*
