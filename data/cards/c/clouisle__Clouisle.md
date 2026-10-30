# clouisle/Clouisle

⭐ 19 · Python · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/clouisle/Clouisle) · [官网](https://clouisle.asia) · 组织维护 · 中文 README

**企业级多智能体协作平台与可视化工作流引擎**

面向企业部署的多智能体协作平台：提供拖拽式工作流编排（19 种节点类型）、多智能体编排（agent/sub_workflow 节点组合）、带人机协同审批与持久化执行。知识库系统支持 PDF/DOCX 等多格式解析、向量+BM25 混合检索与重排，并提供检索实验室做 A/B 对比。管理端可注册 23 个 LLM 供应商代码，含 openai、deepseek、ollama 等。企业特性含多租户、RBAC、SSO、TOTP 2FA、审计日志与 .clouisle 跨环境迁移包。沙箱执行依赖 Bubblewrap 用户/挂载命名空间且 worker 需特定内核能力。通过 Docker Compose/Helm 引导脚本部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化工作流编排，19 种节点类型，支持子工作流与人机审批
- 混合检索（Qdrant 向量 + pg_search BM25 + RRF）与检索实验室 A/B 诊断
- 23 个 LLM 供应商代码，覆盖 chat/embedding/文生图/文生视频/TTS/STT
- 多租户、RBAC、SSO、TOTP 2FA、审计日志与 .clouisle 标准化迁移包

## 适用场景

- 在企业内搭建与编排多智能体工作流并接入多种 LLM
- 构建带混合检索与重排的知识库问答系统
- 通过 Feishu/微信渠道做私有 Agent 对话与知识收集
- 以 Docker Compose 或 Kubernetes 单机/集群部署

## 场景标签

`多智能体` `工作流自动化` `RAG` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L28: - **Multi-Agent & Collaborative Runtime**: Build and orchestrate production-ready AI agent teams — workflows compos
> L76: Every provider is configured from the admin console: you supply the API key, optional base URL, model ID, and capab
> L130: - Docker and Docker Compose v2 for single-server deployment

## 星数曲线

```mermaid
xychart-beta
    title "clouisle/Clouisle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `915885eed17f` · [字段定义](../../DATASET.md)*
