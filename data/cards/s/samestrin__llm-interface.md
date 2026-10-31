# samestrin/llm-interface

⭐ 123 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/samestrin/llm-interface) · [官网](https://www.npmjs.com/package/llm-interface) · 个人维护

**Node.js 统一 LLM 接口库：一个 API 调用 36 家模型服务商**

面向 Node.js 开发者的 npm 模块，通过 LLMInterface.sendMessage 单一接口访问 36 个 LLM 服务商（34 个托管 + 2 个本地如 Ollama、LLaMA.CPP）及数百个模型，支持 chat completion、流式、embeddings 与故障转移。机制上提供动态模块加载、响应缓存（simple-cache/flat-cache/cache-manager 可选）、失败自动重试、JSON 输出与无效 JSON 修复。安装为 npm install llm-interface，依赖 axios 与 Google Gemini SDK 等。限制：Recovery Mode 目前仅 Groq 可用；测试中 NVIDIA 与 Ollama 用例被跳过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 sendMessage 接口覆盖 36 家 LLM 服务商、数百个模型
- chat completion、流式、embeddings 均支持故障转移
- 响应缓存（三种缓存后端可选）与失败自动重试
- JSON 输出支持与无效 JSON 响应自动修复

## 适用场景

- Node.js 应用中切换或并存多家 LLM 服务商而无需重写调用代码
- 统一处理多模型的聊天、流式与 embeddings 请求
- 通过缓存与重试降低 API 成本并提高调用成功率

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: LLM Interface is an npm module that streamlines your interactions with various Large Language Model (LLM) providers 
> L23: - **Unified Interface**: `LLMInterface.sendMessage` is a single, consistent interface to interact with **36 differe

## 星数曲线

```mermaid
xychart-beta
    title "samestrin/llm-interface 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 122 --> 125
    line [124, 123, 123]
```

2026-10-18 124 → 2026-10-31 123（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `69ac17fa57d8` · [字段定义](../../DATASET.md)*
