# rpgeeganage/pII-guard

⭐ 115 · TypeScript · NOASSERTION · 推送 2025-11-01 · [GitHub](https://github.com/rpgeeganage/pII-guard) · 个人维护

**用本地 LLM 检测日志中个人身份信息（PII）的工具**

个人实验性项目：使用 Ollama 运行的 gemma:3b 模型，对结构化与非结构化日志进行个人身份信息（PII）检测与管理，覆盖身份信息、GDPR 第 9 条敏感类别、政府与金融标识、网络设备信息及车牌等类型，面向数据隐私与 GDPR 合规场景。提供 Web 界面（端口 3000）与后端 API（端口 8888），通过 make 命令一键启动 PostgreSQL、Elasticsearch、RabbitMQ、Ollama 及前后端的全栈环境。README 自述为进行中的个人项目，欢迎贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 Ollama 本地运行 gemma:3b 做 PII 检测
- 覆盖 GDPR Art.9 敏感类别与政府/金融/网络设备等标识类型
- make all-in-up 一键启动含 PostgreSQL/Elasticsearch/RabbitMQ/Ollama 的全栈
- 提供 Web 界面与 API 端点提交检测任务

## 适用场景

- 我在日志流水线中检测并管理个人身份信息以支持 GDPR 合规
- 我想实验 LLM 方式对比正则方式做 PII 检测的效果
- 我需要对混杂、多语言的日志做敏感数据扫描

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **PII Guard** is an LLM-powered tool that detects and manages Personally Identifiable Information (PII) in logs — de
> L14: This project experiments with **Large Language Models (LLMs)** — specifically the `gemma:3b` model running locally 
> L73: - 🤖 Ollama (with `gemma:3b`)

## 星数曲线

```mermaid
xychart-beta
    title "rpgeeganage/pII-guard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 113 --> 116
    line [114, 115, 115]
```

2026-10-18 114 → 2026-10-25 115（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3a9d7fd9b15f` · [字段定义](../../DATASET.md)*
