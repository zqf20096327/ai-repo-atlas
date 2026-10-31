# ai-lingnan/econai-agent-platform

⭐ 39 · Python · AGPL-3.0 · 推送 2026-07-17 · [GitHub](https://github.com/ai-lingnan/econai-agent-platform) · [官网](https://ai-lingnan.github.io/econai-agent-platform/) · 组织维护 · 中文 README

**多租户课程作业平台：AI 双 Agent 并行评审自动批改作业**

面向经济金融课程的多租户作业管理平台：超级管理员管理教师与邀请码，教师创建班级、发布作业（评分标准支持 AI 生成）、配置 AI 模型；学生通过文本/文件/图片提交作业，由双 Agent 并行评审（标准审查+亮点发现）产出分数、维度得分、总评、改进建议与亮点。内置 Agent Loop 架构的 AI 助教（12 工具、2 技能、Tavily 搜索）、课程分享投票、MinIO 数据库备份。技术栈为 FastAPI + PostgreSQL + React，支持 OpenAI/Anthropic 适配器，Docker Compose 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双 Agent 并行评审产出结构化批改反馈（分数/维度得分/改进建议/亮点）
- AI 助教：Agent Loop 架构，12 个工具与 2 个技能，搜索结果沉淀为学习资源
- 教师端支持模型管理（API Key/Base URL/适配器类型）
- Docker Compose 一键部署，首次启动自动迁移并创建管理员

## 适用场景

- 教师发布作业并由 AI 自动批改，查看班级提交统计
- 学生在线提交作业并获取维度化的批改反馈
- 通过自然语言让 AI 助教查询班级数据、设计作业、分析成绩

## 场景标签

 · 领域:教育/AI 批改平台

## 证据(README 行号)

> L9: 多租户课程作业管理平台 — 教师发布作业，学生在线提交，AI 双 Agent 并行评审产出结构化反馈。内置 AI 助教、学习资源管理、课程分享投票、数据库备份。
> L68: |AI 批改反馈|双 Agent 并行评审（标准审查 + 亮点发现），产出结构化反馈：分数、维度得分进度条、总评、改进建议、亮点|
> L151: |AI 批改|双 Agent 并行评审（标准审查 + 亮点发现），OpenAI / Anthropic 适配器|

## 星数曲线

```mermaid
xychart-beta
    title "ai-lingnan/econai-agent-platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-31 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f8451717d546` · [字段定义](../../DATASET.md)*
