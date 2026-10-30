# antsanchez/prompto

⭐ 17 · HTML · 推送 2026-10-29 · [GitHub](https://github.com/antsanchez/prompto) · [官网](https://prompto.asanchez.dev/) · 个人维护

**浏览器中与多家 LLM 对话的开源 Angular 聊天界面**

基于 Angular 22 与 LangChain.js 构建的开源聊天 UI，可在浏览器中切换使用 OpenAI、Anthropic、Google Gemini、Mistral、Cohere、xAI 及本地 Ollama 等多种 LLM。功能含消息线程对话、无上下文 Notebook、提示模板、图片/PDF 附件、多模型并排对比的 Arena、多 AI persona 讨论。聊天记录与设置保存在浏览器本地存储，设置页提供一键清除。可作为 PWA 安装；本地运行需 Node.js 22.22.3+，通过 npm 安装依赖并 ng serve 启动。连接跨域 Ollama 需配置其 CORS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 OpenAI/Anthropic/Gemini/Mistral/Cohere/xAI/Ollama 等多家提供商切换
- Arena 多模型并排对比与多 AI persona 讨论模式
- 提示模板创建与复用，支持图片和 PDF 附件
- PWA 支持，可作为应用安装到设备

## 适用场景

- 在同一界面内切换不同 LLM 提供商进行对话
- 并排对比多个模型对同一提示的回应
- 保存和复用常用提示模板进行日常 AI 对话

## 场景标签

`聊天机器人` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Welcome to Prompto, an open-source Angular chat interface designed to provide a user-friendly way of interacting wit
> L16: - OpenAI (GPT-4, GPT-3.5, etc.)
> L22: - Ollama (local models)

## 星数曲线

```mermaid
xychart-beta
    title "antsanchez/prompto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ef59ffcf0879` · [字段定义](../../DATASET.md)*
