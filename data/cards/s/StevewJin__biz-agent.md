# StevewJin/biz-agent

⭐ 3 · Java · MIT · 推送 2026-11-23 · [GitHub](https://github.com/StevewJin/biz-agent) · 个人维护 · 中文 README

**面向企业业务场景的自托管 AI 智能体平台**

Spring Boot + React 19 构建的自托管智能体平台，核心为单一 Agent Loop（规划→工具调用→结果回填，可配最大轮次），通过技能包（Markdown 提示词+资源引用+工具白名单）与扩展包（.bpk zip 或 jar 插件）在运行时注入能力，支持 SQL 只读查询、HTTP 工具、图表渲染与 xlsx/csv 导出。内置团队 RBAC（三角色）、技能/扩展上架审核、JWT 认证、AES 凭据加密与 SSRF 防护。运行需 JDK 22+、PostgreSQL 15+，提供 Docker Compose 与源码构建两种部署方式，LLM 端点支持任意 OpenAI 兼容接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Agent Loop：计划→工具调用→回填→继续，实时流式输出思考链
- 四种声明式扩展工具（sql/http/render/export），无需编码即可扩展
- 团队 RBAC + 技能/扩展包上架审核流程（draft/pending/approved/rejected）
- SQL/HTTP 调用全量审计记录与 AES 凭据加密

## 适用场景

- 接入业务数据库，把通用智能体变成懂业务的数据分析助手
- 管理企业内部 API 供智能体安全调用（凭据平台注入）
- 团队内按角色管理技能与扩展的上架审核
- 生成匿名分享链接，对外提供只读能力的智能体

## 场景标签

`Agent 框架` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L5: A lightweight AI agent platform for enterprise business scenarios: **one Agent Loop + skill packs + extension packs*
> L14: - Single reasoning loop: plan → tool call → feed results back → continue, up to `app.agent.max-turns` rounds
> L58: - **`backend`**: agent orchestration, skill packs, extension runtime, datasource/API management, auth


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `862f5b7cc40b` · [字段定义](../../DATASET.md)*
