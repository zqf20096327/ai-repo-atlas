# coder/ai-tokenizer

⭐ 62 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/coder/ai-tokenizer) · [官网](https://coder.github.io/ai-tokenizer/) · 组织维护

**为 Vercel AI SDK 设计的快速 token 计数库**

npm 包 ai-tokenizer，提供对 AI SDK 工具与消息 schema 的 token 估算，也可按编码（如 o200k_base）直接计数。不使用 WASM，README 声称计数速度为 tiktoken 的 5-7 倍，并给出对 GPT-5、Claude Sonnet、Gemini 等主流模型 ≥97% 的准确率表格（基于与实际 API 响应对比）。每个编码未压缩体积为 2-8MB，需按需导入；README 警告并非所有工具/token 场景均经过准确率验证，存在边界情况。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 AI SDK 的工具与消息 schema
- 无 WASM，README 声称计数速度为 tiktoken 的 5-7 倍
- 对 GPT-5、Claude Sonnet、Gemini 等模型给出 ≥97% 准确率数据表
- 可按编码（如 o200k_base）直接计数 token

## 适用场景

- 在 AI SDK 应用中估算消息与工具调用的 token 消耗
- 不依赖 WASM 环境下进行 token 计数
- 批量文本的 token 用量预估

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: A faster than tiktoken tokenizer with first-class support for Vercel's AI SDK.
> L9: - Supports the AI SDK tool and message schema

## 星数曲线

```mermaid
xychart-beta
    title "coder/ai-tokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-25 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8a564528e80e` · [字段定义](../../DATASET.md)*
