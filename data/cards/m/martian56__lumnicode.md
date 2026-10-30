# martian56/lumnicode

⭐ 38 · TypeScript · MIT · 推送 2026-04-16 · [GitHub](https://github.com/martian56/lumnicode) · [官网](https://lumnicode.ufazien.com) · 个人维护

**BYOK 在线 AI 代码编辑器：自带 API key 的代码生成与辅助**

基于 React 19 + FastAPI 的网页版代码编辑器，内嵌 Monaco Editor 与 AI 辅助面板：Cmd+K 支持解释、重构、补全、找 bug、生成测试，AI 回答经 SSE 流式输出；通过 LangGraph 编排 plan-config-generate-finalize 流水线生成完整项目，进度经 WebSocket 实时推送。用户自带任意受支持提供商（OpenAI/Anthropic/Gemini/Groq/Together/Fireworks/Cohere）的 API key。本地开发需 Docker 启动 Postgres 与 MinIO，认证依赖 Clerk。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BYOK 多提供商接入：OpenAI/Anthropic/Gemini/Groq/Together/Fireworks/Cohere
- Cmd+K AI 命令面板：解释/重构/补全/找 bug/生成测试
- LangGraph plan-config-generate-finalize 项目生成流水线，WebSocket 实时进度
- S3/MinIO 文件存储与 SSE 流式 AI 输出

## 适用场景

- 不想订阅、用自己 API key 的网页端 AI 编码
- 让 AI 按计划流水线生成完整项目并实时查看进度
- 在浏览器中获得带智能补全与高亮的 VS Code 级编辑体验

## 场景标签

`代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L16: Lumnicode is an online code editor with built-in AI assistance. Unlike other AI coding tools, you connect **your ow
> L23: - **AI Command Palette** -- `Cmd+K` for explain, refactor, complete, find bugs, generate tests
> L25: - **LangGraph orchestration** -- AI project generation with plan-config-generate-finalize pipeline

## 星数曲线

```mermaid
xychart-beta
    title "martian56/lumnicode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9ecc4c132ea1` · [字段定义](../../DATASET.md)*
