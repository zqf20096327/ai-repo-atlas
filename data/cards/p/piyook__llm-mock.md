# piyook/llm-mock

⭐ 22 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/piyook/llm-mock) · [官网](https://www.npmjs.com/package/llmock) · 个人维护

**本地模拟 LLM API 的测试服务器，OpenAI/Claude 格式兼容**

基于 Fastify 的本地 npm 服务器，模拟 OpenAI、Gemini、Anthropic Messages 等 LLM API 响应，供开发与测试使用：支持 SSE 流式、可配置延迟、mock embeddings、按请求内容返回 fixture 固定回复、自定义回复池，以及 chaos 模式按频率注入 429/500 等错误以测试重试逻辑。内置请求日志与实时 dashboard，通过 npm create llmock 脚手架、npm install 或 Docker 三种方式安装运行，CLI 参数可覆盖 .llmockrc.json 配置。默认无鉴权并监听全部网络接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Gemini/Claude 三类内置预设，可自定义模型预设
- fixture 规则按请求内容子串匹配返回固定回复（含失败注入）
- chaos 模式可按 every/random 频率注入 HTTP 或流式错误（drop/stall 等）
- 实时 dashboard、请求日志与 mock embeddings 端点

## 适用场景

- 不花费 API 费用、离线开发联调 AI 应用
- 用可预测回复测试 UI 与解析逻辑
- 注入 429/500 与流中断测试重试和错误处理
- 为 embeddings/RAG 流程提供本地模拟向量接口

## 场景标签

 · 领域:LLM 开发/测试工具

## 证据(README 行号)

> L8: A lightweight local server that simulates LLM APIs for development and testing. Build and test AI-powered applicatio
> L23: - **OpenAI-compatible** — works with ChatGPT, Grok, Llama, DeepSeek, Gemini, and any OpenAI-style API
> L24: - **Anthropic Messages API** — built-in `claude` preset with the SDK's streaming event format

## 星数曲线

```mermaid
xychart-beta
    title "piyook/llm-mock 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7f4564a968a8` · [字段定义](../../DATASET.md)*
