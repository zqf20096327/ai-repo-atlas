# fujc683/qwen4-max-api

⭐ 14 · NOASSERTION · 推送 2026-11-18 · [GitHub](https://github.com/fujc683/qwen4-max-api) · [官网](https://gola.apimart.ai/k-SBK4VP) · 个人维护

**开发者调用 Qwen4 Max API 的端点与参数指南**

一份介绍通过 APIMart 调用 Qwen4 Max 模型的文档型仓库：给出 OpenAI 兼容的 chat completions 端点、curl 与 Python SDK 调用示例，说明流式输出默认开启、reasoning_content 字段的解析方式与 reasoning tokens 的计费规则，并列出 messages/stream/max_tokens/temperature/tools 等参数说明与输入输出单价、prompt 缓存等注意事项。文档面向需要接入该 API 的开发者，内容为使用说明而非可运行的软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 chat completions 端点与 curl/Python 调用示例
- reasoning_content 字段与 reasoning_tokens 用量说明
- 参数表：stream 默认开启、function calling 支持 OpenAI schema
- 输入/输出每百万 token 单价与 prompt 缓存提示

## 适用场景

- 接入 Qwen4 Max API 做对话补全
- 解析推理模型的思考过程输出
- 估算带推理 token 任务的调用成本

## 场景标签

 · 领域:LLM API 使用文档

## 证据(README 行号)

> L3: > How to call Qwen4 Max on APIMart: chat completions, streaming defaults and reasoning output.
> L13: ## Endpoint
> L56: |`tools`|function calling, OpenAI schema|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `79e8cfc3a35e` · [字段定义](../../DATASET.md)*
