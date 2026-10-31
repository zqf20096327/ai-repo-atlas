# samuelhm/42Jobs

⭐ 14 · C# · AGPL-3.0 · 推送 2026-06-12 · [GitHub](https://github.com/samuelhm/42Jobs) · 个人维护

**面向初级软件工程师的求职平台：抓取职位并 AI 过滤与生成简历**

面向初级软件工程师的求职 Web 平台，已部署于 42jobs.xyz。通过 RapidAPI 的 LinkedIn Jobs API 按类目抓取职位，用 AI 过滤出适合初级者的岗位并提取技术/软技能关键词，再经 LLM 生成针对每个职位优化 ATS 的简历；另支持 GitHub 仓库导入生成项目条目、求职状态管线跟踪。AI 供应商（Gemini/OpenAI/DeepSeek）与职位来源均为可插拔设计，通过管理面板配置并加密存储，提示词存于数据库。后端 .NET 10 + ASP.NET Core，前端 React 19，数据库 PostgreSQL 16，Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LinkedIn 职位抓取 + AI 相关性与初级友好度过滤
- LLM 生成针对具体职位的 ATS 优化简历
- 可插拔 AI 供应商：Gemini / OpenAI / DeepSeek，提示词与响应 schema 存于数据库
- GitHub 仓库导入自动生成项目条目，求职状态管线跟踪

## 适用场景

- 初级工程师找工作时自动过滤适合初级的岗位
- 按目标职位的提取关键词定制 ATS 友好简历
- 把自己的 GitHub 项目自动整理进简历
- 跟踪投递状态：saved → CV sent → interview → hired/rejected

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L8: 42jobs is a job search platform tailored for **junior software engineers**. It fetches job offers from LinkedIn, fil
> L19: - **CV generation** — generates ATS-optimized CVs via LLM, customized per job offer

## 星数曲线

```mermaid
xychart-beta
    title "samuelhm/42Jobs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `df3a6e58d40a` · [字段定义](../../DATASET.md)*
