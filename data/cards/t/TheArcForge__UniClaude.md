# TheArcForge/UniClaude

⭐ 52 · C# · MIT · 推送 2026-05-11 · [GitHub](https://github.com/TheArcForge/UniClaude) · 组织维护

**把 Claude Code 嵌入 Unity 编辑器的可停靠聊天窗口插件**

Unity 6 编辑器扩展：通过 Unity Package Manager 安装，提供一个可停靠的聊天面板，经 Claude Code OAuth 使用 Claude 订阅（Pro/Max）认证。内置 Unity Agent 系统提示词、10 个开发生命周期架构技能、75+ 个经 MCP 协议暴露的编辑器工具（场景/预制体/组件/材质等修改，带 Undo 集成），并对项目场景、脚本、着色器建立索引。每次工具调用需显式批准。依赖 Node.js 18+ 构建 sidecar。注意：v1.0.0 为最终版本，因 Anthropic ToS 禁止第三方工具经订阅 OAuth 认证而停止维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 75+ 个 MCP 协议编辑器工具，带 Undo 集成与逐次调用权限批准
- 10 个覆盖 Unity 开发生命周期的架构技能（Agent SDK 插件系统按需加载）
- 项目感知：索引场景、预制体、脚本、着色器、ScriptableObjects
- Sonnet/Opus/Haiku 模型选择与可配置推理投入档位

## 适用场景

- 在 Unity 编辑器内直接对话 Claude 处理场景与脚本工作
- 让 Claude 按设计优先流程审查 Unity 架构并标记反模式
- 通过聊天窗口以权限批准方式让 AI 修改预制体与组件

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Claude Code, natively inside Unity Editor. A dockable chat window with full project awareness, 75+ MCP tools, an op
> L30: - **MCP server** — JSON-RPC 2.0 server that exposes Unity editor actions to any MCP-compatible client

## 星数曲线

```mermaid
xychart-beta
    title "TheArcForge/UniClaude 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-25 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c200a2a74efc` · [字段定义](../../DATASET.md)*
