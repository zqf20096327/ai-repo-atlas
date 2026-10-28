# gkvoelkl/python-selma

⭐ 20 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/gkvoelkl/python-selma) · 个人维护

**用 Python 从零重建 OpenClaw 架构的教学型自主 agent**

面向学习者的自主 agent 简化实现：以 Python 重建 OpenClaw 式架构，通过 FastAPI 网关与 Streamlit 仪表盘运行，支持 Ollama 本地模型或 OpenAI 兼容/Anthropic API。提供流式对话、多会话、SKILL.md 技能扩展（内置 summarize/web-research 等 4 个）、Telegram 与 WebChat 通道，以及 OpenTelemetry + Arize Phoenix 本地追踪。README 明确声明为玩具项目，未做安全加固，禁止用于生产或商业环境，且暂不接受 PR。安装依赖 uv 与 git clone 源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SKILL.md 格式技能扩展，内置 summarize/web-research/blogwatcher/healthcheck 四个技能
- Ollama 本地模型或 OpenAI 兼容/Anthropic API 可选后端
- OpenTelemetry + Arize Phoenix 全本地 LLM 调用追踪（opt-in）
- WebChat 流式对话与 Telegram 通道适配

## 适用场景

- 学习自主 agent 的内部架构与组件交互方式
- 在本地用 Ollama 跑一个可对话、可扩展技能的 agent
- 通过 Phoenix UI 观察每次 agent 运行与 LLM 调用细节

## 场景标签

`Agent 框架` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Agent Selma** is a simplified, educational reimplementation of the OpenClaw project.
> L11: The primary goal is to deconstruct and understand the underlying architecture of autonomous agents by rebuilding th
> L22: |LLM API|Ollama (local) or any OpenAI-compatible API|

## 星数曲线

```mermaid
xychart-beta
    title "gkvoelkl/python-selma 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7c0b27391d1f` · [字段定义](../../DATASET.md)*
