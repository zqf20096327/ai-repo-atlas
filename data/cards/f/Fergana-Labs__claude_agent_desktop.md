# Fergana-Labs/claude_agent_desktop

⭐ 28 · Python · MIT · 推送 2025-11-11 · [GitHub](https://github.com/Fergana-Labs/claude_agent_desktop) · [官网](https://www.ferganalabs.com) · 个人维护

**免装 CLI 的 Claude Code 桌面端：Electron 图形界面加扩展技能**

基于 Claude Agent SDK / Claude Code CLI 封装的 Electron 桌面应用，让用户无需终端与命令行知识即可使用 Claude Code 的工具集（文件读写、Bash 执行、代码搜索、Git、联网检索、任务清单），并附带了 CLI 标准版中不含的 Excel/PowerPoint/Word 技能。会话持久化于本地 SQLite，可断点续聊；采用自带 Anthropic API Key 模式，密钥仅存本地。模型默认 claude-sonnet-4-5，可在源码中改为 opus/haiku。从源码构建需 Node.js 18+ 及各平台编译工具链，也提供 dmg/exe/AppImage 分发包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桌面 GUI 封装 Claude Code 工具集（Bash、文件操作、Git、联网检索）
- 含 CLI 标准版没有的 Excel/PowerPoint/Word 技能
- 会话存本地 SQLite，可恢复上下文
- 自带 Anthropic API Key，密钥仅本地存储

## 适用场景

- 不想装 CLI、偏好图形界面地使用 Claude Code 编码助手
- 让 Claude 生成或编辑 Office 文档
- 跨多次会话延续编码任务的上下文

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: A desktop application that lets you use Claude Agent without needing to install the Claude Code CLI. Get access to a
> L29: - **Bring Your Own API Key**: Use your own Anthropic API key for complete control over usage and billing. Your key 

## 星数曲线

```mermaid
xychart-beta
    title "Fergana-Labs/claude_agent_desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b6b7636497da` · [字段定义](../../DATASET.md)*
