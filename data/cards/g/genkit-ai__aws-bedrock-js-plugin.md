# genkit-ai/aws-bedrock-js-plugin

⭐ 13 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/genkit-ai/aws-bedrock-js-plugin) · [官网](https://genkit-ai.github.io/aws-bedrock-js-plugin/) · 个人维护

**让 Genkit 框架接入 AWS Bedrock 模型 API 的社区插件**

面向 Google Genkit 框架开发者的社区插件 genkitx-aws-bedrock，由 Xavier Portilla Edo 构建，通过 AWS 官方 API 接入 Bedrock 的 Chat/Completion 与 Embeddings 模型，支持图像输入与多模态模型。提供多种 AWS 凭证配置方式（环境变量、credential-providers、本地直传）、跨区推理端点、自定义模型注册（含 defineAwsBedrockModel），并附 onCallGenkit 助手用于把 Genkit flow 部署为 AWS Lambda 函数，支持流式响应与内置鉴权 Context Provider。注意需匹配 Genkit 版本（<v0.9.0 对应插件 v1.9.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 Bedrock 全部 Chat/Completion 与 Embeddings 模型，支持图像输入与多模态
- onCallGenkit 将 Genkit flow 部署为 AWS Lambda，支持流式 SSE 响应
- customModels 选项与 defineAwsBedrockModel 注册自定义模型
- 内置 allowAll/requireHeader 等 Context Provider 鉴权助手

## 适用场景

- 在 Genkit 应用中调用 Bedrock 上的 Claude、Nova 等模型
- 把 Genkit flow 部署为 AWS Lambda 函数并做流式输出
- 为 Genkit flow 添加请求头鉴权等认证控制

## 场景标签

 · 领域:LLM 框架插件/云服务接入

## 证据(README 行号)

> L14: **`genkitx-aws-bedrock`** is a community plugin for using AWS Bedrock APIs with
> L17: This Genkit plugin allows the use of AWS Bedrock through their official APIs.
> L265: This plugin supports all currently available **Chat/Completion** and **Embeddings** models from AWS Bedrock. This 

## 星数曲线

```mermaid
xychart-beta
    title "genkit-ai/aws-bedrock-js-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9b49372dda54` · [字段定义](../../DATASET.md)*
