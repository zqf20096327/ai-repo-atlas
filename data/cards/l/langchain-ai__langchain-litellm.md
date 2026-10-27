# langchain-ai/langchain-litellm

⭐ 60 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/langchain-ai/langchain-litellm) · [官网](https://docs.langchain.com/oss/python/integrations/providers/litellm) · 组织维护

**LangChain 与 LiteLLM 的模型调用集成包**

由 langchain-ai 组织维护的 Python 包，将 LiteLLM 封装为 LangChain 的模型接口：LiteLLM 是一个统一调用 Anthropic、Azure、Huggingface、Replicate 等多家模型服务的库，本包使其可作为 LangChain 应用中的 ChatModel 使用。文档指向 LangChain 官方 Docs，遵循其发布与版本策略。README 较简短，未给出使用示例与安装命令细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 LiteLLM 封装为 LangChain 集成类
- 经由 LiteLLM 覆盖 Anthropic/Azure/Huggingface/Replicate 等多家服务
- MIT 许可，发布于 PyPI

## 适用场景

- 在 LangChain 应用中通过统一接口调用多家模型服务商
- 已使用 LiteLLM 的项目接入 LangChain 生态

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L34: This package contains the LangChain integration with LiteLLM. LiteLLM is a library that simplifies calling Anthropi

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langchain-litellm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-27 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8065a6bee9db` · [字段定义](../../DATASET.md)*
