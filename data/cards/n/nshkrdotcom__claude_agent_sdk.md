# nshkrdotcom/claude_agent_sdk

⭐ 36 · Elixir · MIT · 推送 2026-09-30 · [GitHub](https://github.com/nshkrdotcom/claude_agent_sdk) · 组织维护

**Elixir 的 Claude Code SDK：以编程方式驱动 Claude CLI**

面向 Elixir 开发者的 Claude Code SDK，以 Claude Code CLI 为运行时契约，提供 query、流式输出、Client 三层 API，支持生命周期 hooks、权限控制回调、MCP 工具执行、子 agent 流式事件与三种认证方式（OAuth/API Key/CLI 登录），并可接入 AWS Bedrock、Google Vertex 或 Ollama 后端。需单独安装 Claude Code CLI（依赖 Node.js）与 cli_subprocess_core 库，要求 Elixir 1.19 以上。追踪与 Python/TypeScript SDK 的 parity。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- query/Streaming/Client 三层 API 覆盖简单查询到多轮 agent 控制
- 生命周期 hooks 与权限控制（set_permission_mode/interrupt/rewind_files）
- 通过 MCP 进行进程内工具执行
- 支持 OAuth/API Key/CLI 登录认证及 Bedrock/Vertex/Ollama 后端

## 适用场景

- 在 Elixir/BEAM 应用中构建 AI 编码助手或自动化代码审查流水线
- 构建带流式输出的多 agent 工作流与聊天界面
- 通过 MCP 接入自定义工具构建工具增强型应用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: An Elixir SDK aiming for high parity with the official claude-agent-sdk-python while treating the Claude Code CLI as
> L171: Claude Agent SDK 0.20 requires Elixir 1.19 or later and

## 星数曲线

```mermaid
xychart-beta
    title "nshkrdotcom/claude_agent_sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bc495f6dc2a3` · [字段定义](../../DATASET.md)*
