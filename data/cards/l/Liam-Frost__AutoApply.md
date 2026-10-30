# Liam-Frost/AutoApply

⭐ 56 · Python · NOASSERTION · 推送 2026-08-02 · [GitHub](https://github.com/Liam-Frost/AutoApply) · 个人维护 · 中文 README

**求职者的本地求职自动化工作台：发现岗位、评分、生成材料、人工把关提交**

面向个人求职者的本地优先求职自动化工作台，包含 Vue/FastAPI 控制台、PostgreSQL 岗位/申请记录、Redis/Celery 后台任务、可审计的 agent 轨迹，以及支持 OpenAI、Anthropic、Gemini、DeepSeek、Ollama 等十余家提供商的 LLM 层。功能覆盖岗位发现与规范化、硬规则+语义匹配的契合度评分、简历/求职信生成、自动化计划与申请追踪；所有提交动作须人工审批，agent 在受限工具注册表内运行。浏览器表单填写/点击提交、申请状态同步为未实现路径。许可为 PolyForm Noncommercial，商业使用需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- provider 无关的 LLM 层，支持 OpenAI/Anthropic/Gemini/DeepSeek/Ollama 等及自定义 OpenAI 兼容端点
- 提交动作全部经人工审批门控，agent 运行于受限工具注册表
- 硬规则+语义匹配+新鲜度检查的契合度评分，含拒因可解释性
- 统一本地启动器 autoapply start 用 Docker Compose 起 Postgres/Redis 并应用迁移

## 适用场景

- 集中发现、评分并追踪求职岗位申请
- 按 JD 生成定制的简历与求职信
- 设定周期性自动搜索、抓取、准备材料的任务计划
- 在保留人工审批控制的前提下自动化求职流程

## 场景标签

`AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L16: AutoApply is a local-first job application automation workspace. It helps a job seeker discover roles, score fit, g
> L18: The product combines a Vue/FastAPI operator console, PostgreSQL-backed job and application records, Redis/Celery ba

## 星数曲线

```mermaid
xychart-beta
    title "Liam-Frost/AutoApply 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-30 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3a24227c2007` · [字段定义](../../DATASET.md)*
