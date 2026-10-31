# StudentTraineeCenter/edu-agent

⭐ 24 · TypeScript · MIT · 推送 2025-12-30 · [GitHub](https://github.com/StudentTraineeCenter/edu-agent) · [官网](https://app-eduagent-dev-swc-web-yq6q81.azurewebsites.net/) · 组织维护

**面向学生与教育者的 AI 个性化学习平台（RAG+Agent）**

基于 FastAPI + React 的教育平台：用户上传 PDF/DOCX/TXT/RTF 课程材料，系统经 Azure Content Understanding 做文本提取与语义分段，用 pgvector 做向量检索，基于 LangGraph 的 ReAct 模式 Agent 在对话中主动生成测验、闪卡、思维导图，并按成绩（重点针对正确率<70% 的主题）生成个性化学习计划。文档问答带来源引用，声称试点评估中 15 条测试查询取得 93% 检索成功与 0% 幻觉。技术栈深度绑定 Azure（OpenAI GPT-4o、Blob Storage、Key Vault、Terraform 部署）与 Supabase 认证，本地运行需 Docker、Python 3.12+、Node.js 18+、pnpm、Terraform。

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

- 上传文档自动生成测验、闪卡、思维导图与个性化学习计划
- LangGraph ReAct Agent 在对话中主动生成学习材料
- pgvector 语义检索，回答带来源引用
- Terraform 一键配置 Azure 与 Supabase 基础设施

## 适用场景

- 把自己的课程资料变成可对话、可测验的学习环境
- 按薄弱知识点获得自适应学习计划备考
- 用闪卡与主动回忆法记忆概念

## 场景标签

`文档问答` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: EduAgent is a cutting-edge, AI-powered educational platform designed to transform how you learn. By combining advan
> L22: - **🧠 Personalized Study Plans** - AI identifies your weak spots based on performance (focusing on topics where suc
> L23: - **🤖 Proactive AI Tutor (LangGraph)** - Chat with an intelligent agent that uses a **ReAct pattern** to proactivel
> L25: - **🔍 Semantic Search & RAG** - Ask questions grounded in your specific materials. Uses **pgvector** for high-preci

## 星数曲线

```mermaid
xychart-beta
    title "StudentTraineeCenter/edu-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 21 --> 25
    line [22, 23, 24, 24]
```

2026-10-18 22 → 2026-10-31 24（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `853ceba582ac` · [字段定义](../../DATASET.md)*
