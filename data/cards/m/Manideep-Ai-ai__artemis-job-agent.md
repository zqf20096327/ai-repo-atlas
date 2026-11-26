# Manideep-Ai-ai/artemis-job-agent

⭐ 3 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Manideep-Ai-ai/artemis-job-agent) · [官网](https://manideep-ai-ai.github.io/artemis-job-agent/) · 个人维护

**本地运行的求职/接单 Agent：找职位、找招聘人、写并发送跟进邮件**

基于 Python/FastAPI 的本地求职代理：从 Greenhouse/Lever 等公司招聘板、Remotive、Hacker News Who is hiring、Freelancer.com 等来源抓取线索，按简历技能与城市/预算匹配并给出理由，通过网页搜索定位招聘负责人，用 AI 或模板撰写个性化邮件，经用户批准后从 Gmail 发送（默认每天最多 10 封、仅工作时段），并在第 4/7 天同线程跟进。默认 practice 模式只存 .eml 不发送；数据存本地 SQLite，MIT 许可，无服务器与遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抓取多来源职位与自由职业线索并解释匹配理由
- 网页搜索定位招聘人，邮箱地址标注 posted/verified/likely/guessed
- Gmail 发送带安全限制：用户逐封批准、每日上限 10 封、bounce/reply 后停止
- practice 模式将邮件保存为本地 .eml 供检查

## 适用场景

- 我想让 AI 帮我筛选匹配的职位并起草给招聘人的冷邮件
- 我接自由职业项目时想按最低时薪自动匹配报价提案
- 我希望发送记录、回复标签和 Pipeline 看板都在本地管理

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: Give it your resume. It finds matching jobs and client projects, finds the right person to contact, writes the email
> L8: proposal, sends it from your own Gmail after you approve it, and follows up until they answer.
> L33: |**Sends**|From your Gmail, resume attached, working hours only, **max 10 a day**, only after you approve|Same|
> L73: |**AI writing**|More personal emails and proposals|Gemini, Groq, or Ollama offline|

## 星数曲线

```mermaid
xychart-beta
    title "Manideep-Ai-ai/artemis-job-agent 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-29 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `05b2d65f5ba9` · [字段定义](../../DATASET.md)*
