# schauh11/revit-mcp-server

⭐ 26 · C# · MIT · 推送 2026-02-05 · [GitHub](https://github.com/schauh11/revit-mcp-server) · 个人维护

**内嵌于 Revit 的自然语言 AI 助手插件（MCP，53+ 工具）**

为 Autodesk Revit 2026 提供的原生 WPF 聊天面板插件：用户以自然语言下达指令，插件经 WebSocket 连接本地 MCP 服务器（Node.js），转发至所配置的 AI 提供商（OpenRouter、Anthropic、DeepSeek、Qwen，含经 Ollama 本地运行），AI 调用 53+ 个直接访问 Revit API 的工具完成查询、选择、可见性、视图、图纸、MEP、标注与导出操作，并通过 ExternalEvent 保证线程安全、多步操作以原子事务执行。需 .NET 8.0 与 Node.js 18+，从源码克隆构建，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 53 个专用工具 + 5 个跨类别的动态意图工具（query/execute/analyze/navigate/create）
- 通过 .env 一行配置切换 OpenRouter/Anthropic/DeepSeek/Qwen，可经 Ollama 本地运行
- Revit API 调用走 ExternalEvent，多步操作为原子事务
- 提示词缓存与 SQLite 持久化 100 条对话历史

## 适用场景

- 在 Revit 内用自然语言查询构件、工程量与模型信息
- 用对话完成视图复制、图纸创建与视图布置等多步操作
- 执行 MEP 管线长度统计与电气盘表相关流程

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: **AI chat for Autodesk Revit that lives inside Revit.** No Claude Desktop. No external apps. Just a native chat pane
> L15: Supports multiple AI providers out of the box: OpenRouter (100+ models), Anthropic Claude, DeepSeek, and Qwen. Swit
> L183: 1. **User types** a natural language command in the embedded Revit chat panel

## 星数曲线

```mermaid
xychart-beta
    title "schauh11/revit-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2d4494331bdd` · [字段定义](../../DATASET.md)*
