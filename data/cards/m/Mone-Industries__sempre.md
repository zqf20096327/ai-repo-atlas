# Mone-Industries/sempre

⭐ 20 · Smarty · 推送 2026-03-20 · [GitHub](https://github.com/Mone-Industries/sempre) · 组织维护

**自托管的 Docker 多智能体 AI 团队系统**

基于 OpenClaw + Ollama 构建的 Docker 化多智能体系统：用户通过 Discord、Web UI 或 SSH 下发任务，GM 智能体分诊任务并分派给多个 Worker 智能体并行执行研究、编码、数据提取与网页任务；研究结果写入共享 Obsidian 知识库供后续任务优先检索。集成 n8n 处理定时任务与 webhook，工具调用按平台服务强制路由（Brave Search、Crawl4AI、Browser-use、gh-proxy 等）。安装流程为克隆仓库、填写 config.json、make up；需 Docker、Tailscale 与 jq，Ollama Cloud 密钥需首次启动后手动注册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GM 分诊 + Worker 并行的多智能体协作架构
- 共享 Obsidian 知识库（disks/km/），任务结果沉淀并可被后续检索
- 强制工具路由：网页搜索/抓取/浏览器/GitHub/Google Workspace 各由专属服务承担
- n8n 承接定时报告、数据同步与 webhook 触发

## 适用场景

- 通过 Discord 或 Web UI 让一组 AI 智能体协作完成研究与编码任务
- 自托管一个长期运行、知识可累积的 AI 团队
- 把定时报告与自动化流程交给 n8n 与智能体配合执行

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: sempre is a **Docker-based multi-agent AI system** built on OpenClaw + Ollama. You define a team of agents, each wit
> L22: **GM (General Manager)** receives tasks from users via Discord or Web UI. It triages complexity, delegates to Worke
> L26: **Knowledge compounds over time** — every research result gets written to the shared Obsidian KM vault (`disks/km/`

## 星数曲线

```mermaid
xychart-beta
    title "Mone-Industries/sempre 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `41ee10dd6323` · [字段定义](../../DATASET.md)*
