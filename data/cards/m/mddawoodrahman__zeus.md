# mddawoodrahman/zeus

⭐ 14 · JavaScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/mddawoodrahman/zeus) · [官网](https://chromewebstore.google.com/detail/zeus-%E2%80%94-prompt-enhancement/nejhojapbopmedoagaimcdmgekjnkoal) · 个人维护

**Chrome 扩展：在 ChatGPT/Claude/Gemini 等聊天页一键改写优化提示词**

Manifest V3 Chrome 扩展，在支持的 LLM 聊天站点输入框旁注入增强按钮，将用户提示词改写为更清晰、结构化的版本后回填输入框。请求经云端或本地 LLM 提供商路由，支持 Gemini、OpenAI、Claude、OpenRouter、本地 Ollama 及自动回退模式。另含 Chrome 侧边栏工作台（历史记录、模板变量、diff 查看）、Copilot 式行内补全建议与延迟监控。终端用户以开发者模式加载未打包目录安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键改写提示词并保留原意图，回填至输入框
- 支持 Gemini/OpenAI/Claude/OpenRouter/本地 Ollama 及自动路由回退
- Chrome 侧边栏工作台：历史记录、模板变量注入、逐词 diff
- Copilot 式行内补全：输入停顿后流式灰色幽灵文本建议

## 适用场景

- 在 ChatGPT/Claude/Gemini 等聊天站直接优化我要发送的提示词
- 用本地 Ollama 无需云端 API key 改写提示词
- 跨多个 AI 平台统一提示词工作流

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Zeus is a Manifest V3 Chrome extension that improves user prompts directly in supported chat applications. It preser
> L26: - **Supported Providers**: Gemini, OpenAI, Claude, OpenRouter, and local Ollama.
> L104: - Ollama local runtime: `http://localhost:11434`

## 星数曲线

```mermaid
xychart-beta
    title "mddawoodrahman/zeus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a71452bb9dd3` · [字段定义](../../DATASET.md)*
