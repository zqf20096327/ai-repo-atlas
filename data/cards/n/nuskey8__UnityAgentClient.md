# nuskey8/UnityAgentClient

⭐ 287 · C# · MIT · 推送 2025-11-05 · [GitHub](https://github.com/nuskey8/UnityAgentClient) · 个人维护

**让任意 AI agent 在 Unity 编辑器内运行的 ACP 客户端扩展**

Unity 编辑器扩展，实现 Agent Client Protocol（ACP）客户端，使兼容 ACP 的 AI agent（Gemini CLI、经 Zed 适配器的 Claude Code/Codex CLI、opencode、Goose 等）可在 Unity 编辑器内运行。支持将资源与编辑器信息作为上下文，内置 MCP 服务器，可拖拽资源附加上下文。需 Unity 2021.3+ 与 Node.js 运行时，依赖通过 NuGet 安装的 AgentClientProtocol 包，本体经 Package Manager 的 git URL 安装。README 不建议用于编辑器内编码（Domain Reload 会断开会话），定位是以整个 Unity 项目为文档供 agent 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 ACP 客户端，接入任何兼容 ACP 的 AI agent
- 资源与编辑器信息作为上下文，可拖拽资源附加
- 内置 MCP 服务器，可连接任意 MCP server
- 不依赖特定 LLM 提供商或 agent

## 适用场景

- 在 Unity 编辑器内直接与 AI agent 对话并利用项目资源作上下文
- 让团队成员借助 AI 加深对整个 Unity 项目的理解
- 识别 Unity 项目的瓶颈与问题，无需在编辑器与外部工具间切换

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: Unity Agent Client is an editor extension that uses the Agent Client Protocol (ACP) proposed by Zed to enable any A
> L18: - Integrate any AI agent into the Unity editor
> L19: - Supports all AI agents compatible with ACP (Gemini CLI, Claude Code, Codex CLI, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "nuskey8/UnityAgentClient 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 285 --> 288
    line [286, 287, 287]
```

2026-10-18 286 → 2026-10-23 287（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `23d49879aa2f` · [字段定义](../../DATASET.md)*
