# iam-epiphany/resume-agent

⭐ 31 · Python · 推送 2026-08-16 · [GitHub](https://github.com/iam-epiphany/resume-agent) · 个人维护 · 中文 README

**个人简历 RAG 问答系统：面试官对话式追问简历内容**

面向“面试官 × 简历主人公”场景的 RAG 问答系统：将简历、项目说明、证书等材料加工为 Markdown 知识文档、人物档案与结构化事实（Fact Ledger）后入库，面试官可对简历任意提问，系统以第一人称作答。机制上包含七类意图路由、Dense+关键词混合检索与 RRF 融合、分级重排、多轮指代消解、硬事实 grounding 校验、证据不足时明确拒答或标注推测，并有统一时间预算。技术栈为 FastAPI + React + Qdrant + BGE 系列，LLM 走 OpenAI 兼容 API（默认 DeepSeek），CPU 部署，Docker Compose 启动，附 30 题评测集与 480 项 Mock 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Fact Ledger 结构化事实与生成后事实归属校验，降低跨项目混淆
- Dense+关键词混合检索、RRR 融合与 BGE 分级重排
- 硬事实 grounding 校验，证据不足时明确拒答而非编造
- 人物 Skill 导出：可迁移到其他支持 Skills 的 Agent 环境

## 适用场景

- 求职者搭建自己的简历问答站，供面试官对话式追问
- 项目经历、证书、荣誉等资料统一入库后做事实一致性问答
- 对 RAG 简历问答系统做检索与拒答效果的离线评测

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L14: ResumeMind 是一个面向个人简历场景的 RAG 问答系统。
> L16: 和传统的「上传 PDF 后直接问答」不同，ResumeMind 会先把简历、项目说明、证书和个人经历等材料整理为结构化知识，再进行检索和生成。
> L220: - **LLM**：OpenAI 兼容 Chat Completions API（默认 DeepSeek）

## 星数曲线

```mermaid
xychart-beta
    title "iam-epiphany/resume-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-28"]
    y-axis "stars" 28 --> 32
    line [29, 30, 31, 31]
```

2026-10-18 29 → 2026-10-28 31（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0c6ac194ef47` · [字段定义](../../DATASET.md)*
