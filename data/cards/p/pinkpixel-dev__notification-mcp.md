# pinkpixel-dev/notification-mcp

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-07-12 · [GitHub](https://github.com/pinkpixel-dev/notification-mcp) · [官网](https://pinkpixel.dev) · 组织维护

**让 AI agent 在任务完成时发桌面通知与提示音的 MCP 服务器**

TypeScript 编写的 Model Context Protocol 服务器，向 MCP 客户端提供 notify（toast 通知+声音）与 play_notification（仅声音）两个工具，供 AI agent 在任务完成时调用。内置 5 个提示音文件（cosmic/fairy/gentle/pleasant/retro，可随机），支持通过环境变量选择内置音或指定自定义 MP3 路径，Windows/macOS/Linux 均可运行。通过 npx 免安装运行，也支持 npm 全局或本地安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- notify 工具支持 toast 通知、声音或两者组合（mode 可选）
- 内置 5 个提示音，npx 运行即可使用，无需手动下载
- 环境变量可配置内置音或自定义 MP3 绝对路径
- 跨平台支持 Windows/macOS/Linux

## 适用场景

- 为长时间运行的 AI agent 任务添加完成提醒
- 在编码 agent 完成任务时收到桌面通知和提示音
- 为 MCP 客户端（如 Claude 类工具）配置声音提醒

## 场景标签

 · 领域:AI agent 基础设施/MCP 工具

## 证据(README 行号)

> L17: A Model Context Protocol server that allows AI agents to play notification sounds when tasks are completed. This Ty
> L23: - `notify` - Show a desktop toast notification and/or play a sound when tasks complete (Recommended for summaries)

## 星数曲线

```mermaid
xychart-beta
    title "pinkpixel-dev/notification-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b001f2b1705d` · [字段定义](../../DATASET.md)*
