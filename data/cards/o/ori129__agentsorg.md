# ori129/agentsorg

⭐ 14 · Python · NOASSERTION · 推送 2026-06-30 · [GitHub](https://github.com/ori129/agentsorg) · [官网](https://agentsorg.ai) · 个人维护

**面向企业的 ChatGPT Enterprise 资产治理与分析平台**

自托管的开源平台，通过 OpenAI Compliance API 自动发现 ChatGPT Enterprise 工作区内的全部 Custom GPT 与 Project，用 LLM 从系统提示中提取 9 个语义信号并生成质量/采用/风险三项复合评分与象限标签。提供采用度会话分析、工作流覆盖分析、重复建设聚类检测、学习发展模块、员工门户，以及 OIDC SSO、TOTP MFA 等安全机制。技术栈为 React + FastAPI + PostgreSQL/pgvector，以 Docker Compose 三服务部署，支持无 API key 的演示模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 OpenAI Compliance API 自动发现工作区全部 Custom GPT 与 Project
- LLM 提取 9 个语义信号并生成质量/采用/风险复合评分与象限标签
- 会话智能、工作流覆盖与重复建设聚类（pgvector + 中心点聚类 + LLM 验证）
- OIDC SSO、TOTP MFA、角色门控与加密密钥轮换等安全机制

## 适用场景

- 盘点企业内全部 Custom GPT 并识别风险与僵尸资产
- 追踪 AI 资产的采用度与业务流程覆盖情况
- 发现多团队重复建设的工具并选定组织标准
- 基于评分缺口为 GPT 构建者推荐课程

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3:  Open-source AI governance platform for ChatGPT Enterprise
> L16: AgentsOrg.ai connects to the **OpenAI Compliance API** and gives your organization a complete picture of every Cust
> L61: - **Workflows** — Business process coverage analysis. Shows which workflows are covered by AI assets (with conversa

## 星数曲线

```mermaid
xychart-beta
    title "ori129/agentsorg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e3b43acc6a7a` · [字段定义](../../DATASET.md)*
