# unisone/openclaw-config

⭐ 14 · Shell · MIT · 推送 2026-09-13 · [GitHub](https://github.com/unisone/openclaw-config) · [官网](https://github.com/openclaw/openclaw) · 个人维护

**OpenClaw 的生产级配置、脚本与工作区模板集合**

面向 OpenClaw（开源 AI agent 网关）用户的可复制构建块仓库，非 SDK。提供生产加固套件（密钥迁移 .env、崩溃恢复调优、日志轮转、备份监控）、工作区启动模板（AGENTS.md/SOUL.md/STATE.md 等）、技能路由负例覆盖、JSON5 网关配置片段（压缩、模型回退、LanceDB 记忆、Perplexity 搜索）、Shell 记忆引擎与 Python 任务运行器，以及 8 个多 agent 人设提示词。兼容 OpenClaw 2026.2.24+，通过 curl 安装脚本或 git clone 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生产加固套件：密钥入 .env、崩溃恢复、配置回滚、磁盘占用优化
- 工作区模板：AGENTS.md/SOUL.md/STATE.md/HEARTBEAT.md 等完整脚手架
- 技能路由覆盖：以负例降低重叠领域误触发
- 跨供应商模型回退与 LanceDB 长期记忆配置片段

## 适用场景

- 把我日常使用的 OpenClaw 部署加固到生产标准
- 为 agent 工作区搭建记忆生命周期与任务自动化
- 配置跨供应商模型回退避免级联故障

## 场景标签

 · 领域:AI agent 基础设施/运维配置

## 证据(README 行号)

> L5:  Production-tested configs, scripts, and workspace templates for OpenClaw.
> L6:  Not an SDK — just copyable building blocks from a real daily-driver setup.
> L139: |`config/`|Gateway config snippets (JSON5) — compaction, pruning, model fallbacks, memory, search, Slack|

## 星数曲线

```mermaid
xychart-beta
    title "unisone/openclaw-config 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8d8577e49058` · [字段定义](../../DATASET.md)*
