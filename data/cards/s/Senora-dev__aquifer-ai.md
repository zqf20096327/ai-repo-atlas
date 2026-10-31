# Senora-dev/aquifer-ai

⭐ 14 · Python · NOASSERTION · 推送 2026-08-11 · [GitHub](https://github.com/Senora-dev/aquifer-ai) · [官网](https://aquifer-ai.dev) · 组织维护

**部署在自有 VPC 内的 AI Agent 上下文湖，聚合工程知识供检索**

面向工程团队的开源基础设施：以无头服务形式将 GitHub 等工程上下文（issues、PR、README、讨论）摄取进 Amazon OpenSearch 向量库，摄取时通过模块化提示词抽取客观实体（如 service、jira_key）与事实关系并索引为可查询字段，通过五个 MCP 工具（search_context、find_related、list_entities 等）供 AI agent 直接检索。以单个 AWS CDK 栈部署在隔离 VPC 内，嵌入与抽取使用自有 Bedrock，数据不出网络。不做评分、排序或结论判断。无 UI；SSO/RBAC 等企业功能通过 Interceptor 接缝以后续包形式提供；许可为 BSL 1.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub 上下文摄取进 OpenSearch 向量库，提取实体与关系并索引
- 五个 MCP 检索工具供 agent 语义搜索与关系遍历
- 单 CDK 栈部署至隔离 VPC，无公网端点，数据不出网络
- Interceptor 接缝设计，企业功能（SSO/RBAC/审计）作为独立包挂载

## 适用场景

- 为 AI agent 提供自有 VPC 内的工程知识检索层
- 部署前让 agent 汇聚与某服务相关的全部上下文
- 对 GitHub issues/PR 做语义索引供 agent 查询

## 场景标签

`语义搜索` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: An open-source, **in-VPC Context Lake** — neutral **infrastructure for AI agents**, not a
> L7: context (GitHub first) into an OpenSearch vector store and exposes a standard **MCP API** that
> L8: AI agents query directly. All inside your own VPC, deployable as a single CDK stack.

## 星数曲线

```mermaid
xychart-beta
    title "Senora-dev/aquifer-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `fc8bb88df4dc` · [字段定义](../../DATASET.md)*
