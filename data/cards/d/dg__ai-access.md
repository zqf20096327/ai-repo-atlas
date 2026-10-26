# dg/ai-access

⭐ 66 · PHP · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/dg/ai-access) · [官网](https://ai-access.deegee.dev) · 个人维护

**PHP 统一 AI 接口库：一套代码接入 OpenAI/Claude/Gemini/DeepSeek/Grok**

面向 PHP 开发者的 AI 提供商客户端库，用统一接口封装 OpenAI、Claude、Gemini、DeepSeek、Grok 五家 API，切换提供商只需改一行代码。零依赖（纯 PHP + curl），不使用各厂商 SDK。覆盖多轮对话、流式输出、工具调用（模型出错回传自我修正）、推理力度统一参数、批量处理与嵌入；提供商特有选项以各 Provider 类的类型化命名参数暴露。另有通用客户端可对接 OpenAI 方言端点（Ollama、Mistral、OpenRouter、vLLM、Azure）。要求 PHP 8.3+，通过 Composer 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接口封装 5 家提供商，切换只需改一行
- 零依赖：纯 PHP 与 curl，不依赖厂商 SDK
- 工具调用全流程封装，模型参数错误回传其自行修正
- 通用客户端支持 OpenAI 方言端点（Ollama/vLLM/OpenRouter 等）

## 适用场景

- PHP 应用中集成多家 LLM 且保持代码可迁移
- 构建带工具调用与流式输出的对话功能
- 通过批量接口降低调用成本并跟踪 token 用量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: **One clean PHP interface for OpenAI, Claude, Gemini, DeepSeek and Grok.** Write your AI integration once, switch pr
> L57: Ollama, Mistral, OpenRouter, Together, vLLM or Azure. The mark means something

## 星数曲线

```mermaid
xychart-beta
    title "dg/ai-access 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0e82083f823e` · [字段定义](../../DATASET.md)*
