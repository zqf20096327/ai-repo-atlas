# omarkamali/borgllm

⭐ 19 · Python · MIT · 推送 2025-12-11 · [GitHub](https://github.com/omarkamali/borgllm) · [官网](https://borgllm.com/) · 个人维护

**通用 Python LLM 客户端：多供应商接入、密钥轮换与限流回退**

面向开发者的 LLM 客户端库：集成 20+ 供应商，提供 BorgOpenAI/BorgAsyncOpenAI 作为 OpenAI SDK 的 drop-in 替代，通过 provider:model 格式自动解析供应商。关键机制包括多 API key 轮询轮换、429 限流冷却处理、供应商失败自动回退、可合并多个供应商的虚拟供应商，配置经程序化 API、borg.yml 或环境变量三层优先级生效。LangChain 集成为可选 extra。限制：需各供应商 API key，本地模型需自行配置 custom provider。

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

- BorgOpenAI/BorgAsyncOpenAI duck-type OpenAI SDK，无需迁移 API
- 多 API key 轮换与 429 限流冷却处理
- 供应商失败自动回退与虚拟供应商策略
- 内置 20+ 供应商，borg.yml 支持自定义供应商（如 Ollama/LM Studio）

## 适用场景

- 在多个 LLM 供应商之间统一 API 调用并自动回退
- 多 API key 场景下自动轮换以规避限流
- 不迁移代码地从 OpenAI SDK 切换到其他模型
- 通过 borg.yml 接入本地 Ollama/LM Studio 模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **BorgLLM** is a universal Python LLM client with integrated LLM providers, automatic API key rotation, rate limit h
> L24: - **🔄 Drop-in OpenAI SDK**: `BorgOpenAI` and `BorgAsyncOpenAI` duck-type the official clients

## 星数曲线

```mermaid
xychart-beta
    title "omarkamali/borgllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `899fd4e326d1` · [字段定义](../../DATASET.md)*
