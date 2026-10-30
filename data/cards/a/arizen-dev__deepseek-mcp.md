# arizen-dev/deepseek-mcp

⭐ 54 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/arizen-dev/deepseek-mcp) · [官网](https://deepseek.com) · 个人维护

**把 DeepSeek 作为廉价受监督工人暴露给 MCP 客户端的 stdio 服务器**

面向 Claude Code、Codex 等 MCP 客户端的 Python stdio MCP 服务器，提供两个工具：deepseek（flash 非思考模型，用于分类/提取/格式化等机械任务）与 advise（pro 思考模型，用于架构与权衡建议）。它读取 JSON-RPC 消息，调用 DeepSeek 的 OpenAI 兼容 chat completions API，流式返回文本并附带模型、延迟、token 与成本元数据。需 DEEPSEEK_API_KEY；可通过 DEEPSEEK_BASE_URL 接入任意 OpenAI 兼容端点（含 Ollama、vLLM）。README 明确其不适用于自主架构设计、安全决策或最终交付文本，定位为需人工复核的辅助工人。

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

- 两个 MCP 工具：deepseek（flash，非思考）与 advise（pro，thinking）
- 响应附带模型/延迟/token/成本元数据，可开启调用日志（不记录 prompt）
- 支持任意 OpenAI 兼容端点：DeepSeek、Gemini、Ollama、vLLM、Mistral
- 输出仅文本，不能调用工具或访问文件系统，需人工复核

## 适用场景

- 让 Claude Code/Codex 把分类、提取、格式化等机械任务外包给廉价模型
- 为团队拉取低成本的第二意见与权衡分析
- 通过本地 Ollama/vLLM 端点在 MCP 客户端内使用自有模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: `deepseek-mcp` is a tiny stdio MCP server with two tools:
> L230: 2. exposes two MCP tools: `deepseek` (flash, non-thinking) and `advise` (pro, thinking);
> L231: 3. sends your prompt to DeepSeek's OpenAI-compatible chat completions API;

## 星数曲线

```mermaid
xychart-beta
    title "arizen-dev/deepseek-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-30 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `fda934aefcd1` · [字段定义](../../DATASET.md)*
