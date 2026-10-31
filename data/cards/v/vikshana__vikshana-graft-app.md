# vikshana/vikshana-graft-app

⭐ 55 · TypeScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/vikshana/vikshana-graft-app) · 个人维护

**Grafana 的 AI 助手插件：自然语言查询可观测性数据**

开源 Grafana 插件，让用户通过自然语言对话查询仪表盘、指标、日志、追踪与告警等可观测性数据。支持配置双模型（快速响应与深度推理）分别处理不同任务，可接入 Anthropic、OpenAI 兼容 API，以及 Ollama、LM Studio 本地推理；通过 Grafana 内置 MCP 工具与实例交互。依赖 Grafana 10.4.0+ 与 Grafana LLM Plugin 1.0.0+，当前为实验性开发阶段，插件未签名需在配置中允许加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言查询仪表盘、指标、日志、追踪与告警
- 双模型配置：Standard 快速响应与 Deep Research 深度推理
- 支持 Anthropic、OpenAI 兼容 API 及 Ollama/LM Studio 本地推理
- 聊天历史记录与可复用的提示词模板库

## 适用场景

- 在 Grafana 中用对话查询 CPU、错误率等指标
- 排查指标突变并协助创建告警
- 复用常用提示词模板进行日常运维问答

## 场景标签

`AI 助手` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: An open-source AI assistant plugin for Grafana, enabling natural language interaction with your observability data.
> L16: - **Natural Language Queries** - Ask questions about your dashboards, metrics, logs, traces, alerts or more

## 星数曲线

```mermaid
xychart-beta
    title "vikshana/vikshana-graft-app 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-31"]
    y-axis "stars" 51 --> 56
    line [52, 53, 55, 55]
```

2026-10-18 52 → 2026-10-31 55（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2d873dcdfc60` · [字段定义](../../DATASET.md)*
