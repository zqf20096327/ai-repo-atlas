# reVrost/go-openrouter

⭐ 128 · Go · Apache-2.0 · 推送 2026-07-27 · [GitHub](https://github.com/reVrost/go-openrouter) · 个人维护

**面向 Go 开发者的 OpenRouter API 非官方 SDK**

提供 OpenRouter API 的非官方 Go 客户端库，通过 go get 安装并使用 OPENROUTER_API_KEY 初始化。功能覆盖聊天补全、补全、流式输出、Embeddings、推理、工具调用、结构化输出、提示/响应缓存、网页搜索、多模态（图像/PDF/音频）、文本转语音与语音转文本转录。内置模型回退机制：对 402/429/5xx 等错误码自动切换备份模型，支持自定义回退策略；响应缓存通过 HTTP 头按请求启用。给需要在 Go 项目中接入 OpenRouter 多模型路由的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持聊天补全、流式输出、Embeddings、工具调用、结构化输出
- 内置模型回退机制（默认 402/429/5xx 等错误码触发，可自定义策略）
- 按请求启用 OpenRouter 响应缓存，通过 HTTP 头传递
- 文本转语音与语音转文本转录（本地文件自动 base64 编码）

## 适用场景

- 在 Go 服务中接入 OpenRouter 调用多种 LLM
- 为聊天补全配置主备模型自动回退
- 使用 Embeddings、TTS、语音转文本等多端点能力

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: This library provides unofficial Go client for Openrouter API
> L12: go get github.com/revrost/go-openrouter

## 星数曲线

```mermaid
xychart-beta
    title "reVrost/go-openrouter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 127 --> 129
    line [128, 128]
```

2026-10-18 128 → 2026-10-26 128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0842e280a407` · [字段定义](../../DATASET.md)*
