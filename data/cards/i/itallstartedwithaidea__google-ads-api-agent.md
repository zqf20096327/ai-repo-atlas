# itallstartedwithaidea/google-ads-api-agent

⭐ 31 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/itallstartedwithaidea/google-ads-api-agent) · [官网](https://googleadsagent.ai) · 个人维护 · 中文 README

**广告投放者的 Claude 驱动 Google Ads 管理 Agent**

基于 Python 的 Google Ads 管理 Agent，通过 Google Ads API v23 对广告账户进行实时读写，包含 28 个自定义工具与 6 个专用子 Agent，由 Claude 的 Messages API 编排工具调用与结果解读。提供三种部署路径：Anthropic API 编程接入（本仓库开箱内容）、Agent 平台手动部署、Cloudflare 生产版（googleadsagent.ai 的 Buddy，含语义记忆、加密密钥存储、计费系统）。支持 pip 安装、CLI 交互、FastAPI REST 服务与 Docker 部署。需自备 Anthropic API key、Google Ads/MCC 账户及多个第三方服务凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个工具 + 6 个子 Agent，经 Google Ads API v23 实时读写广告账户
- 适配层将原平台 action 文件转为可独立运行的 Anthropic API 部署
- 内置 FastAPI REST 服务与 Docker Compose 部署方式
- 多语言 README（含中文）与云厂商生产架构参考文档

## 适用场景

- 投放人员用自然语言查询与管理 Google Ads 广告系列
- 在自己的应用中通过 REST API 集成广告管理 Agent
- 自动化广告投放流水线（SaaS、自动化管道）

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L9: An enterprise-grade, AI-powered Google Ads management system with **28 custom tools**, **6 specialized sub-agents**,
> L61: This is the **programmatic deployment** — no manual UI, no clicking. Everything runs through Claude's Messages API 
> L113: That's it. The agent is running, making real Google Ads API calls through your credentials, with Claude orchestrat

## 星数曲线

```mermaid
xychart-beta
    title "itallstartedwithaidea/google-ads-api-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9c0e6fc79c6d` · [字段定义](../../DATASET.md)*
