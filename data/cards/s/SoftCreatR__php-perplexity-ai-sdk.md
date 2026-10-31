# SoftCreatR/php-perplexity-ai-sdk

⭐ 14 · PHP · ISC · 推送 2026-10-23 · [GitHub](https://github.com/SoftCreatR/php-perplexity-ai-sdk) · [官网](https://packagist.org/packages/softcreatr/php-perplexity-ai-sdk) · 个人维护

**接入 Perplexity API 的 PHP SDK，覆盖 Agent/搜索/嵌入等端点**

基于 PSR-17/PSR-18 接口的 Perplexity API PHP 客户端库，方法目录对齐 Perplexity API 参考：Agent、Search、Embeddings、Models、Orchestrator（限量预览）、Skills、Files、Batches 等。提供 SSE 流式解码（支持任意分块、CRLF/LF、[DONE]）、multipart 文件流式上传、结构化 PerplexityAIException（保留状态码、响应体、x-request-id）、可选响应包装与 ModelResponse DTO，以及独立的组织分析 API 认证。要求 PHP 8.2.35+/8.3.36+/8.4.27+/8.5.12+，依赖 PSR-17/PSR-18 实现（如 Guzzle）与 JSON 扩展，通过 composer 安装，每个 SDK 方法附示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSE 流式回调解码，支持任意分块、CRLF/LF、未终止帧与 [DONE]
- multipart 上传流式传输原始字节而非 base64 编码
- 结构化异常保留 API 错误、响应头、状态码与 x-request-id
- 可选 ModelResponse DTO 与 JSONPayloadContract 载荷校验包装

## 适用场景

- PHP 项目中调用 Perplexity 的 Agent API 与搜索端点
- 为 Perplexity 组织分析 API 做单独认证集成
- 通过 SDK 管理文件、技能与批处理任务

## 场景标签

 · 领域:LLM API 客户端/开发库

## 证据(README 行号)

> L8: A lightweight PSR-17/PSR-18 client for the current Perplexity API, with
> L27: composer require softcreatr/php-perplexity-ai-sdk guzzlehttp/guzzle
> L234: The catalog follows the current Perplexity API reference.

## 星数曲线

```mermaid
xychart-beta
    title "SoftCreatR/php-perplexity-ai-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `895e8b8b6f6a` · [字段定义](../../DATASET.md)*
