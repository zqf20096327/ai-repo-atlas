# rootflo/wavefront

⭐ 199 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/rootflo/wavefront) · [官网](https://rootflo.ai) · 组织维护

**企业级 AI 中间件平台：把企业数据接入生产级 AI 应用**

开源中间件平台 Wavefront，面向在生产环境构建 AI 应用的企业开发团队。以 YAML 定义 agent、多 agent 工作流、聊天机器人与电话语音 agent，基于自研 flo-ai 框架构建；提供数据源连接（BigQuery/PostgreSQL/S3 等）、行级权限与审计、pgvector+关键词的 RAG 检索、RBAC、OpenTelemetry 可观测性与 Web 控制台。每个应用独立部署（floware），由 floconsole 统一管理。AGPL-3.0 许可，Beta 阶段，自托管走 Docker，本地开发用脚本启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YAML 定义 agent 与多 agent 工作流，支持版本化与回滚
- 语音 agent 支持多语言、通话中工具调用与通话后评估
- 知识库 RAG：后台摄取与嵌入，pgvector 向量+关键词+重排
- 支持 OpenAI/Anthropic/Gemini/Groq/Ollama/vLLM 等模型统一配置

## 适用场景

- 在受控数据上构建带权限与审计的 agent 工作流
- 搭建企业内部知识库问答与 RAG 应用
- 部署电话催收/外呼场景的语音 agent

## 场景标签

 · 领域:企业 AI 中间件

## 证据(README 行号)

> L40: Wavefront AI is an open-source middleware platform for building production AI applications on enterprise data. It l
> L88:  OpenAI, Azure OpenAI, Anthropic, Google Gemini, Groq, Ollama and vLLM, managed centrally as reusable model configu

## 星数曲线

```mermaid
xychart-beta
    title "rootflo/wavefront 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 198 --> 200
    line [199, 199]
```

2026-10-18 199 → 2026-10-22 199（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a83291c63887` · [字段定义](../../DATASET.md)*
