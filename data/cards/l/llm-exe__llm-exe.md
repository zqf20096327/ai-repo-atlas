# llm-exe/llm-exe

⭐ 136 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/llm-exe/llm-exe) · [官网](https://llm-exe.com) · 组织维护

**TypeScript/JavaScript 的 LLM 应用构建库**

npm 包形式的 JavaScript/TypeScript 库，提供构建与维护 LLM 应用的基础组件：类型化 Prompt 模板（Handlebars 语法，支持文本与对话式）、内置与自定义解析器（string/json/boolean 等，JSON 可带 schema 校验）、执行器、会话状态管理与生命周期 Hooks。支持多 provider 切换（OpenAI/Anthropic/xAI/Google/AWS Bedrock/Ollama/DeepSeek）而不改代码，并允许 LLM 调用函数或其他执行器。ESM 优先，兼容 CommonJS，提供无需 API key 的 mock 模型用于测试。

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

- Handlebars 类型化 Prompt 模板（文本与对话式）
- 内置/自定义解析器，JSON 可带 schema 校验
- 多 provider 统一接口（OpenAI/Anthropic/xAI/Google/Bedrock/Ollama/DeepSeek）
- 会话状态管理与执行器 Hooks，支持 LLM 函数调用

## 适用场景

- 在 TypeScript 项目中以统一接口调用多家 LLM 并随时切换模型
- 构建带类型校验的结构化 LLM 输出
- 管理与复用多轮对话状态

## 场景标签

`模型网关` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: A package that provides simplified base components to make building and maintaining LLM-powered applications easier.
> L13: - Call LLMs from different providers without changing your code. (OpenAI/Anthropic/xAI/Google/AWS Bedrock/Ollama/De

## 星数曲线

```mermaid
xychart-beta
    title "llm-exe/llm-exe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 135 --> 137
    line [136, 136]
```

2026-10-18 136 → 2026-10-22 136（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3c4ad665d712` · [字段定义](../../DATASET.md)*
