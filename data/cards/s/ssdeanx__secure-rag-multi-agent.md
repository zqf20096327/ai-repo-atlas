# ssdeanx/secure-rag-multi-agent

⭐ 19 · TypeScript · NOASSERTION · 推送 2025-12-27 · [GitHub](https://github.com/ssdeanx/secure-rag-multi-agent) · [官网](http://deanmachines.com) · 个人维护

**带层级 RBAC 安全 RAG 的多 Agent AI 编排平台（Mastra+Next.js）**

基于 Mastra AI 框架与 Next.js 构建的多 Agent 编排平台，提供带访问控制的安全 RAG（公开/内部/机密文档分级、按权限过滤的向量检索、引用与审计日志）、多阶段研究工作流、网页抓取与内容评估、语音交互及 MCP 集成。含 20+ 专职 Agent、12 个工具与多条工作流，采用 JWT 认证（Supabase）、Cedar 策略、PostgreSQL/PgVector 存储。面向需要在企业知识权限管控下进行 AI 问答与研究的场景；自建部署需 Node.js>=20.9.0、Docker 与模型 API key，配置步骤较多。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 层级 RBAC 与文档密级分类，按用户权限过滤的向量检索（PgVector）
- 20+ 专职 Agent 与 12 个工具，含身份/策略/检索/重排/回答/校验的 RAG 管线
- 多阶段研究工作流：查询分解、网页抓取、内容评估、报告生成
- MCP 集成与 A2A Agent Card 暴露，支持 Gemini/OpenAI/OpenRouter

## 适用场景

- 企业内部知识库做权限隔离的 AI 问答与引用溯源
- 组织研究团队自动化执行多来源调研并生成带引用的报告
- 需要审计与合规校验的企业级 RAG 与 Agent 工作流搭建

## 场景标签

`多智能体` `RAG` `文档问答` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L22: A comprehensive multi-agent AI orchestration platform featuring secure Retrieval-Augmented Generation (RAG), advanc
> L28: A comprehensive multi-agent AI orchestration platform that combines secure Retrieval-Augmented Generation (RAG) wit
> L38: - **Secure RAG**: Enterprise-grade retrieval with access controls and audit trails

## 星数曲线

```mermaid
xychart-beta
    title "ssdeanx/secure-rag-multi-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `45c967b8ab3a` · [字段定义](../../DATASET.md)*
