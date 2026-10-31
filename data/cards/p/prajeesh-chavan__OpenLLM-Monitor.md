# prajeesh-chavan/OpenLLM-Monitor

⭐ 45 · JavaScript · MIT · 推送 2026-07-07 · [GitHub](https://github.com/prajeesh-chavan/OpenLLM-Monitor) · 个人维护

**自托管 LLM API 调用实时监控与调试仪表盘**

开源可自托管的 LLM 可观测性仪表盘，以代理/SDK 包装等方式零代码接入，实时记录 OpenAI、Ollama、OpenRouter、Mistral 等 API 调用，追踪 token、延迟、成本、重试与错误，支持跨提供商重放与对比提示词、批量测试、成本预估及告警。技术栈为 Node.js + Express + MongoDB 后端与 React + Vite 前端，提供 Docker Compose 与手动安装两种方式，Anthropic 支持标注为待推出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零代码代理服务器接入，无需修改现有应用
- 跨 OpenAI/Ollama/OpenRouter/Mistral 的统一实时监控（token、延迟、成本、重试、错误）
- 提示词跨提供商/模型重放与对比、批量测试与成本预估
- WebSocket 实时更新、CSV/JSON 导出与告警系统

## 适用场景

- 监控生产环境中多家 LLM 提供商的调用成本与延迟
- 重放提示词在不同模型间做效果与费用对比
- 为 LLM 应用排查错误与分析重试情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: _Monitor, analyze, and optimize your LLM usage across multiple providers in real-time_
> L130: - 🚀 **Zero-code Proxy Servers** - Monitor without changing your code

## 星数曲线

```mermaid
xychart-beta
    title "prajeesh-chavan/OpenLLM-Monitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `84d71f3a3a86` · [字段定义](../../DATASET.md)*
