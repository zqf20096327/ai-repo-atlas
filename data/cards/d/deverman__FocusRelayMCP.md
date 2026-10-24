# deverman/FocusRelayMCP

⭐ 55 · Swift · MIT · 推送 2026-10-17 · [GitHub](https://github.com/deverman/FocusRelayMCP) · 个人维护

**让 AI 助手读写 OmniFocus 任务的 macOS MCP 服务器与 CLI**

用 Swift 编写的本地 MCP 服务器和 CLI，供 Claude Code、OpenCode、Codex CLI 等终端型 MCP 客户端通过文档化的 Omni Automation API 读取和修改 OmniFocus 任务与项目：查找/计数、更新字段、完成/移动、审批优先的收件箱工作流，写操作支持预览与保存后核验。架构为 Swift 服务器派发到运行在 OmniFocus 内的桥接插件，无云端服务。当前版本不支持创建或删除条目；桌面版 Claude Desktop 与 ChatGPT 应用暂不支持。经 Homebrew 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个面向模型的 MCP 工具（7 读 + edit_tasks/edit_projects）
- 写操作支持预览与保存后核验，失败即报告为失败
- Swift 服务器 + OmniFocus 内桥接插件，本地运行，无托管云服务
- 同核心提供 CLI，供脚本与 shell 型 agent 使用

## 适用场景

- 让 AI 助手小批量处理我的 OmniFocus 收件箱
- 用对话查找、标记、改期任务并核验改动
- 脚本或 CLI agent 精确查询任务数据

## 场景标签

 · 领域:效率工具/AI 集成

## 证据(README 行号)

> L5: FocusRelay is a fast, native Swift MCP server and CLI that helps AI assistants
> L184: FocusRelay currently supports terminal-based MCP clients: Claude Code,
> L191: Configure a local stdio MCP server with:

## 星数曲线

```mermaid
xychart-beta
    title "deverman/FocusRelayMCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-24 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e6403a237878` · [字段定义](../../DATASET.md)*
