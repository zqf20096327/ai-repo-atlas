# vibheksoni/UniClaudeProxy

⭐ 62 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/vibheksoni/UniClaudeProxy) · 个人维护

**让 Claude Code 接入任意 LLM 后端的 Anthropic API 代理**

基于 FastAPI 的本地 API 代理，运行在 localhost:9223，将 Claude Code 发出的 Anthropic Messages API 请求转换为 OpenAI 兼容 API（含 DeepSeek、GLM、Ollama、vLLM 等）、Google Gemini 原生 API 或 Anthropic 直通格式，并把响应以 Anthropic SSE 事件流回传。支持原生 function calling 与 ReAct XML 回退（面向无原生工具调用的模型）、thinking 块转换、图像三种处理模式、系统提示词替换、config.json 热重载；默认仅接受 localhost 连接。面向希望 Claude Code 使用非 Anthropic 模型的开发者，以 git clone + pip 安装运行。

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

- Anthropic ↔ OpenAI/Gemini/Claude 直通的双向协议转换与 SSE 流式回传
- ReAct XML 工具调用回退，支持无原生 function calling 的模型（如本地 Ollama）
- thinking/reasoning 块提取与 Gemini thoughtSignature 往返转换
- config.json 热重载、系统提示词替换、默认 localhost-only 安全模式

## 适用场景

- 在 Claude Code 中使用 DeepSeek、GLM、Gemini 或本地 Ollama 模型
- 把 Claude Code 的 API 流量统一路由到自选的推理后端
- 让拒绝 Claude 身份提示词的模型通过系统提示词替换正常工作

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: **UniClaudeProxy** is a lightweight, high-performance FastAPI proxy that lets Claude Code talk to **any LLM backend
> L251: Claude Code CLI  -->  UniClaudeProxy (localhost:9223)  -->  Any LLM Provider
> L252: (Anthropic fmt)       Route + Convert + Stream              (OpenAI/Gemini/etc)

## 星数曲线

```mermaid
xychart-beta
    title "vibheksoni/UniClaudeProxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d62f7ddc8db2` · [字段定义](../../DATASET.md)*
