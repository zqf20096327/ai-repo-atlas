# epam/ai-dial-adapter-bedrock

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/epam/ai-dial-adapter-bedrock) · [官网](https://dialx.ai) · 组织维护

**将 AWS Bedrock 模型接入 AI DIAL 平台的 LLM 适配器**

AI DIAL 生态的适配器组件：在独立容器中运行，把 AWS Bedrock 上的语言模型与嵌入模型的 API 统一到 DIAL Core 的协议。支持 Claude、Llama、Nova、DeepSeek R1、Jamba、Command R、Stable Diffusion 3.5 等模型，覆盖 chat completions、tokenize、truncate_prompt、configuration 等端点，基于 Converse API / Bedrock API / Anthropic SDK 三种实现。提供手动/自动 prompt caching、guardrail 配置与跨区域推理支持。限制：Bedrock 暂不支持 Claude 自动缓存；部分 tokenization 与 tools 为近似或模拟实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以表格列出各模型对 tokenize/truncate_prompt/tools/configuration 端点的支持程度
- 基于 Converse API、Bedrock API、Anthropic SDK 三种实现方式
- 支持手动 prompt caching（系统/消息/工具缓存断点）与跨区域推理（US/EU/APAC）
- 支持经 /configuration 端点配置优化延迟模式与 Bedrock Guardrail

## 适用场景

- 在 AI DIAL 平台中调用 AWS Bedrock 上的 Claude/Llama/Nova 等模型
- 对 Bedrock 对话模型启用 prompt caching 以复用缓存断点
- 通过 /configuration 端点为请求启用 guardrail 或优化延迟模式

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: LLM Adapters unify the APIs of respective LLMs to align with the Unified Protocol of DIAL Core. Each Adapter operat
> L17: The project implements AI DIAL API for language models and embedding models from AWS Bedrock.

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-adapter-bedrock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `69008524a266` · [字段定义](../../DATASET.md)*
