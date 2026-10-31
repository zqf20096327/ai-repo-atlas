# spyder-ide/langchain-provider

⭐ 13 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/spyder-ide/langchain-provider) · 组织维护

**Spyder 6 的 LangChain 代码补全提供器插件**

为 Spyder 6（至少 6.1.0）提供的补全提供器插件，基于 LangChain 与 OpenAI 兼容 API 生成代码补全。使用需设置 OPENAI_API_KEY 环境变量，支持本地 LLM（如经 LMStudio）配合使用，并可通过状态栏菜单配置建议数量（1-10）、模型与 API URL，支持为结构化输出定义 JSON schema。从 PyPI 或源码 pip 安装，依赖 Spyder。

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

- 基于 LangChain 与 OpenAI 兼容 API 的补全提供器
- 支持本地 LLM（如 LMStudio）作为后端
- 可配置建议数量（1-10）、模型与 API URL
- 支持为模型结构化输出定义 JSON schema

## 适用场景

- 在 Spyder 中获得 AI 代码补全
- 接入本地 LLM 做编辑器内补全

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: To use this completions provider you will need to install Spyder 6 (at least 6.1.0)
> L18:  pip install git+https://github.com/spyder-ide/langchain-provider.git

## 星数曲线

```mermaid
xychart-beta
    title "spyder-ide/langchain-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f5a6c2a8c833` · [字段定义](../../DATASET.md)*
