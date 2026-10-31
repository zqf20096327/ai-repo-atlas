# kenshiro-o/nagato-ai

⭐ 119 · Python · MIT · 推送 2026-04-16 · [GitHub](https://github.com/kenshiro-o/nagato-ai) · 个人维护

**跨多家 LLM 构建 AI Agent 系统的 Python 库**

供开发者用代码创建和编排 AI Agent 的 Python 库（pip 包名 nagatoai_core），支持 OpenAI GPT、Anthropic Claude、Google Gemini、Groq（Llama 3）与 DeepSeek 等模型，可混合不同厂商模型组成协调者/工作者/评审者等多 agent 配置。提供工具调用机制（继承 AbstractTool 自定义工具）、基于 DAG 的图式 agent 工作流（Tool 节点、Agent 节点、顺序/条件等 Flow），并集成 Langfuse 做 LLM 调用追踪。作者声明库处于早期开发阶段，可能引入破坏性变更，本地 LLM（Ollama）支持仍在路线图未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 OpenAI/Anthropic/Gemini/Groq/DeepSeek 多厂商模型并可混合组队
- Coordinator/Worker/Critic 等多 agent 协作配置模式
- 基于 DAG 的图式 agent 系统（Tool 节点、Agent 节点、多种 Flow 控制结构）
- 自定义工具（AbstractTool 继承）与 Langfuse 追踪集成

## 适用场景

- 用不同厂商的模型组合搭建多 agent 协作系统
- 构建 YouTube 下载→转录→摘要这类多步骤工具工作流
- 为 LLM 应用添加自定义工具调用与调用链追踪

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: Nagato-AI is an intuitive AI Agent library that works across multiple LLMs.
> L67: Nagato currently supports the following LLMs
> L151: Nagato supports creating complex agent systems using a directed acyclic graph (DAG) approach. This allows you to c

## 星数曲线

```mermaid
xychart-beta
    title "kenshiro-o/nagato-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-31 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c9303c047147` · [字段定义](../../DATASET.md)*
