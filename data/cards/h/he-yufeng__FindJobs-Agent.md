# he-yufeng/FindJobs-Agent

⭐ 243 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/he-yufeng/FindJobs-Agent) · 个人维护 · 中文 README

**求职者用的全栈求职助手：爬岗位、LLM 分析、简历匹配与 AI 模拟面试**

面向求职者的全栈求职工具：爬取腾讯、字节、网易、Amazon 等公司公开招聘 API 的职位，用 LLM 抽取学历/专业要求、给技能标签打分并归类职位族；解析 PDF/Word 简历并计算与职位的匹配百分比；任一职位描述可驱动的多轮 AI 模拟面试并给实时反馈。后端为 Python（Flask API + SQLite），前端 React。提供无需 API key 的离线 Demo 模式（确定性 stub LLM + 54 条样例职位），任务源可通过 JobSource 接口插件式扩展（含 freehire.me、Remotive 免 key 数据源）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取→LLM 分析→技能差距→模拟面试的完整闭环
- 简历解析与职位匹配百分比计算
- 多轮 AI 模拟面试，含实时反馈与追踪看板
- FINDJOBS_DEMO=1 离线演示模式，stub LLM 不联网
- JobSource 接口支持插件式接入自定义职位源

## 适用场景

- 爬取目标公司职位并自动结构化技能要求
- 上传简历查看与各职位的匹配度和技能差距
- 针对具体职位描述进行模拟面试练习
- 在申请看板上追踪各职位投递状态

## 场景标签

 · 领域:求职/招聘工具

## 证据(README 行号)

> L12: A full-stack job search assistant that crawls postings from major tech companies, analyzes them with LLMs, parses y
> L43: - **AI mock interview** — generates questions from any job description and runs a multi-turn interview with real-ti

## 星数曲线

```mermaid
xychart-beta
    title "he-yufeng/FindJobs-Agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 242 --> 245
    line [243, 244, 243]
```

2026-10-18 243 → 2026-10-22 243（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `30852ad85881` · [字段定义](../../DATASET.md)*
