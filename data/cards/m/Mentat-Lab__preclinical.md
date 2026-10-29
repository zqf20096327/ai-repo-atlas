# Mentat-Lab/preclinical

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-06-21 · [GitHub](https://github.com/Mentat-Lab/preclinical) · [官网](https://preclinical.dev/) · 组织维护

**医疗 AI agent 安全测试平台：对抗多轮对话模拟与自动评分**

面向医疗 AI agent 的开源自托管测试平台：模拟对抗性患者多轮对话，采集完整对话记录，并按安全规则对结果自动评分。支持 OpenAI、Anthropic、Vapi、LiveKit、Pipecat、ElevenLabs 及 Browser Use Cloud 等被测对象接入通道；测试患者与评分由可配置的 LLM 模型驱动（默认 gpt-4o-mini）。以 Docker Compose 自托管，另提供 Python CLI、Claude Code 插件与 Agent Skills（Cursor/Windsurf/Copilot 等）接入方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模拟对抗性患者多轮对话并采集对话记录
- 按安全规则对 agent 回答结果自动评分
- 支持 OpenAI/Vapi/LiveKit/Pipecat/ElevenLabs/Browser Use 等被测通道
- Docker Compose 自托管，另提供 Python CLI、Claude Code 插件与 Agent Skills

## 适用场景

- 上线前对我开发的医疗 AI agent 做对抗性安全测试
- 留存测试对话记录用于审查与合规追溯
- 持续运行基准测试比较 agent 版本的安全表现

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: Open-source platform for testing healthcare AI agents with adversarial multi-turn conversations and automated gradin
> L7: Preclinical simulates realistic adversarial patient interactions against your healthcare AI agent, captures transcri
> L65: ## Supported Providers

## 星数曲线

```mermaid
xychart-beta
    title "Mentat-Lab/preclinical 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fef201e835a8` · [字段定义](../../DATASET.md)*
