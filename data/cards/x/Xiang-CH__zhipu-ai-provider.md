# Xiang-CH/zhipu-ai-provider

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-07-27 · [GitHub](https://github.com/Xiang-CH/zhipu-ai-provider) · [官网](https://www.npmjs.com/package/zhipu-ai-provider) · 个人维护 · 中文 README

**让 Vercel AI SDK 直接调用智谱 GLM 系列模型的社区 Provider**

面向 Vercel AI SDK 开发者的社区集成包：实现 AI SDK 6 的 LanguageModelV3 自定义 provider 契约，接入智谱（bigmodel.cn 与 z.ai 双端点）的 GLM 语言模型，并提供 embedding 与图像生成模型。支持流式输出、工具调用、视觉、推理参数（thinking 开关、reasoningEffort 六档）等；限制包括仅支持 function tools、图像生成仅返回 URL 至 providerMetadata、schema 引导结构化输出与视频/音频/OCR 模型未实现。通过 npm 安装，API key 经环境变量读取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时支持 bigmodel.cn 与 z.ai 双端点（zhipu/zai 实例或 createZhipu 自定义）
- 覆盖文本生成、流式、embedding、图像生成、工具调用、视觉与推理
- reasoningEffort 参数透传任意模型 ID，未来模型无需更新 provider

## 适用场景

- 在 Vercel AI 应用中使用智谱 GLM 模型替代其他模型供应商
- 通过统一 AI SDK 接口调用 GLM 的推理与视觉能力
- 集成智谱 embedding 与图像生成到 AI SDK 工作流

## 场景标签

 · 领域:LLM 基础设施/模型接入

## 证据(README 行号)

> L3: This is a Zhipu (Z.ai) provider for the Vercel AI SDK. It supports AI SDK 6 and the `LanguageModelV3` custom-provide
> L25: import { zhipu } from 'zhipu-ai-provider' // for bigmodel.cn

## 星数曲线

```mermaid
xychart-beta
    title "Xiang-CH/zhipu-ai-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5c20bae5f330` · [字段定义](../../DATASET.md)*
