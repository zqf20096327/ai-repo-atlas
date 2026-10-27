# mesa/mesa-llm

⭐ 79 · Python · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/mesa/mesa-llm) · 组织维护

**Mesa 框架扩展：将 LLM 接入 ABM 智能体做决策**

Mesa-LLM 是 Mesa 元胞/智能体建模（ABM）框架的扩展库，将大语言模型集成为智能体的决策组件，用于建模涉及自然语言的沟通、谈判与决策场景。用户可自建推理/记忆/通信模块接入现有代码，或使用预置模块快速搭建。支持 OpenAI、Anthropic、Ollama 等 8 家 LLM 提供商，通过 pip 从 PyPI 安装。仓库处于活跃开发期，作者声明 API 与功能可能显著变动，首个正式版本尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 LLM 作为 ABM 智能体的决策组件
- 可插拔的推理/记忆/通信模块，支持自建或预置
- 支持 8 家 LLM 提供商（OpenAI/Anthropic/Ollama 等）
- 提供 PyPI 包与 GitHub 源码安装途径

## 适用场景

- 构建智能体间用自然语言沟通谈判的仿真模型
- 在 Mesa 既有 ABM 项目中加入 LLM 驱动的决策智能体
- 复杂社会行为场景的语言驱动建模研究

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: Mesa-LLM integrates large language models (LLMs) as decision-making agents into the Mesa agent-based modeling (ABM)
> L44: ## Supported LLM Providers

## 星数曲线

```mermaid
xychart-beta
    title "mesa/mesa-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 75 --> 80
    line [76, 78, 79]
```

2026-10-18 76 → 2026-10-27 79（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `52d98bcc7b3a` · [字段定义](../../DATASET.md)*
