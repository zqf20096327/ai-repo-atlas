# agentsystems/agentsystems

⭐ 115 · Shell · Apache-2.0 · 推送 2026-02-15 · [GitHub](https://github.com/agentsystems/agentsystems) · [官网](https://agentsystems.ai) · 组织维护

**自托管的第三方 AI agent 应用商店与运行时**

部署在用户自有基础设施上的 AI agent 分发与运行平台：提供按 GitHub 用户名索引的自托管目录、基于 Git 的联邦发现与免审核发布（自动合并 PR）；运行侧提供容器隔离、运行时凭证注入（与 agent 供应方分离）、默认拒绝出口流量与按 agent 白名单放行、供应方抽象（继承用户的 OpenAI/Anthropic/Bedrock/Ollama 配置）及哈希链审计日志。由 6 个仓库组成（网关、CLI、UI、构建库、模板、联邦索引）。当前为 pre-release，官方声明仅建议用于开发测试，生产需等稳定版。安装为 shell 脚本一键安装并经 `agentsystems up` 启动 Gateway/UI/egress 代理/PostgreSQL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自托管联邦 agent 目录，按 GitHub 用户名索引、免审核自动合并发布
- 容器隔离 + 运行时凭证注入 + 默认拒绝出口流量与按 agent 白名单
- 供应方抽象：agent 继承用户自己的 OpenAI/Anthropic/Bedrock/Ollama 配置
- 哈希链审计日志，平台由 6 个组件仓库组成

## 适用场景

- 在自己服务器上发现、安装并运行第三方 AI agent
- 不让数据离开自有基础设施地使用第三方 agent
- agent 开发者将自己的 agent 发布到联邦索引供他人发现
- 企业对 agent 的网络出口与凭证做集中管控和审计

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: **Self-hosted app store and runtime for third-party AI agents.**
> L22: **Distribution:**
> L31: - Provider abstraction (agents inherit your OpenAI/Anthropic/Bedrock/Ollama config)

## 星数曲线

```mermaid
xychart-beta
    title "agentsystems/agentsystems 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-24 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2c63985c7021` · [字段定义](../../DATASET.md)*
