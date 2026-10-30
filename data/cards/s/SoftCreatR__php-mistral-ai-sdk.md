# SoftCreatR/php-mistral-ai-sdk

⭐ 19 · PHP · ISC · 推送 2026-10-23 · [GitHub](https://github.com/SoftCreatR/php-mistral-ai-sdk) · [官网](https://packagist.org/packages/softcreatr/php-mistral-ai-sdk) · 组织维护

**面向 PHP 开发者的 Mistral AI API 官方风格 SDK**

基于 PSR-17/PSR-18 接口的轻量 PHP 客户端，覆盖当前 Mistral AI API 的方法目录：聊天补全、FIM、嵌入、分类/审核、OCR、语音（Voxtral 转写）、Realtime 会话、模型管理、Agents、Conversations、Files、Batch、Libraries 及文档管理等。SDK 仅依赖 PSR 接口（Guzzle 为示例实现），支持 SSE 流式回调、multipart 流式上传、结构化 MistralAIException 与可选响应包装/DTO。要求 PHP 8.2.35+ 等指定补丁版本及 JSON 扩展，通过 composer 安装，附每个方法的可运行示例。

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

- 方法目录跟随 Mistral AI API 参考，含 Beta 端点与 v2 Prompts/Skills 路由
- 仅依赖 PSR-17/PSR-18 接口，可替换任意合规 HTTP 实现
- SSE 流式解码（任意分块、CRLF/LF、[DONE]）与流式 multipart 上传
- 结构化 MistralAIException 保留状态码、响应体与 x-request-id；可选 JSONPayloadContract 做响应校验

## 适用场景

- PHP 项目中接入 Mistral 的聊天、嵌入、OCR 与语音转写能力
- 批量任务与文件管理的工作流集成
- 用 SSE 回调实现流式对话界面

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L8: A lightweight PSR-17/PSR-18 client for the current Mistral AI API, with examples for
> L20: Guzzle is used below because it provides both the PSR-17 factories and a PSR-18 client implementation. The SDK itse

## 星数曲线

```mermaid
xychart-beta
    title "SoftCreatR/php-mistral-ai-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8f2d12d1af60` · [字段定义](../../DATASET.md)*
