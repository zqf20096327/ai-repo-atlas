# zbndev/tidemark

⭐ 63 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/zbndev/tidemark) · [官网](https://tidemark.zbndev.com) · 组织维护

**追踪 AI 订阅与 API key 配额余量的桌面应用**

Linux/Windows 桌面应用，用 Rust + Slint 编写，读取用户添加的 AI 服务商（58 个内置，可通过 Lua 插件扩展）的用量接口，显示配额余量、多账户卡片、配额不足与重置通知、历史消费图表。Linux 端提供 tidemarkctl CLI，输出 JSON 并内置 Waybar 模块；后台守护进程通过 D-Bus 供窗口与脚本共用读数。凭据存于系统钥匙串，无遥测。要求 Linux 有 Wayland/X11 与 OpenGL，Windows 10 1803+ x64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 58 个内置提供商，支持通过 .tidemark-provider 文件（沙箱化 Lua）添加自定义提供商
- 多账户管理与配额历史图表、低配额与重置通知
- tidemarkctl CLI 输出 JSON，内置 Waybar 模块与 guard/watch 命令
- 凭据存系统钥匙串，无遥测，仅连接用户添加的服务商

## 适用场景

- 在桌面实时查看各 AI 订阅和 API key 的剩余配额
- 在脚本或 CI 中用 guard 命令判断配额是否充足
- 在 Waybar 等面板显示配额状态

## 场景标签

 · 领域:AI 服务监控/桌面工具

## 证据(README 行号)

> L13: Tidemark is a desktop app for Linux and Windows that tracks the usage limits of your AI
> L16: - **58 providers,** with everything each one reports about your

## 星数曲线

```mermaid
xychart-beta
    title "zbndev/tidemark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-28 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1bc198bd3a01` · [字段定义](../../DATASET.md)*
