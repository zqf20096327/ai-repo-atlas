# pinkpixel-dev/mindbridge-mcp

⭐ 39 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/pinkpixel-dev/mindbridge-mcp) · 组织维护

**统一接入多家 LLM 的 MCP 路由服务器，支持多模型对比**

Model Context Protocol (MCP) 服务器，使 MCP 兼容应用（如 Claude Desktop、Cursor、Windsurf）通过统一接口调用多家 LLM 提供商：OpenAI、Anthropic、Google、DeepSeek、OpenRouter、Ollama 及 OpenAI 兼容 API。提供三个 MCP 工具：getSecondOpinion（向多模型问同一问题对比回答）、listProviders、listReasoningModels。API 密钥通过环境变量、MCP 配置或 JSON 配置，提供商自动发现。经 npm 或 Smithery 安装，也可从源码构建，需 Node.js 运行环境。MIT 许可。

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

- 单服务器统一接入 OpenAI/Anthropic/Google/DeepSeek/OpenRouter/Ollama 及 OpenAI 兼容 API
- getSecondOpinion 工具向多个模型提问并对比回答
- 提供 OpenAI 兼容 API 层，可嵌入期待 OpenAI 端点的工具
- 按环境变量/MCP 配置/JSON 配置，提供商自动发现

## 适用场景

- 在 Claude Desktop 或 Cursor 等 MCP 客户端中调用多家 LLM
- 构建多模型工作流，按任务路由到不同模型
- 让多个模型对同一问题给出第二意见并对比

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: MindBridge is your AI command hub — a Model Context Protocol (MCP) server built to unify, organize, and supercharge 
> L23: |Multi-LLM Support|Instantly switch between OpenAI, Anthropic, Google, DeepSeek, OpenRouter, Ollama (local models),

## 星数曲线

```mermaid
xychart-beta
    title "pinkpixel-dev/mindbridge-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01eb72dc26a8` · [字段定义](../../DATASET.md)*
