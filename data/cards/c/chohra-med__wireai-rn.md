# chohra-med/wireai-rn

⭐ 13 · TypeScript · MIT · 推送 2026-08-20 · [GitHub](https://github.com/chohra-med/wireai-rn) · [官网](https://getwireai.com) · 个人维护

**React Native SDK：把 LLM 响应渲染为 Zod 校验的原生组件**

面向移动开发者的生成式 UI SDK：开发者用描述和 Zod schema 注册 React Native 组件，agent 返回 {action, component, props}，SDK 校验 props 后原生渲染，校验失败的输出不会上屏。内置 11 个组件，支持流式渐进渲染（Hermes 安全）、组件嵌套组合，可接 OpenAI、Ollama、LM Studio、Webhook 或 A2A 端点；云端 apiKey 仅限本地开发，线上建议走服务端 Webhook。附带 EU AI Act 合规立场说明与多个示例工程。

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

- Zod schema 校验 LLM 输出的 props，失败输出不上屏不崩溃
- 11 个内置组件，无 WebView，原生渲染且支持嵌套组合
- 流式渐进渲染，Hermes 安全（XHR 而非 fetch）
- 支持 OpenAI/Ollama/LM Studio/Webhook/A2A 多种接入方式

## 适用场景

- 在 React Native 应用中把 AI agent 输出渲染为原生交互界面
- 配合 Express + LangChain 服务端构建多步骤生成式 UI 流程
- Expo 应用中实现流式 token 渐进渲染的 AI 界面

## 场景标签

 · 领域:移动开发/LLM 前端

## 证据(README 行号)

> L5: Open-source React Native SDK for generative UI: render interactive native components from LLM responses. No WebView,
> L7: Your agent speaks JSON. Mobile users expect native UI. Wire RN closes that gap: register your React Native component
> L16: The agent returns `{ action, component, props }`, Wire RN validates `props` against the component's Zod schema, and

## 星数曲线

```mermaid
xychart-beta
    title "chohra-med/wireai-rn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0b63770783bd` · [字段定义](../../DATASET.md)*
