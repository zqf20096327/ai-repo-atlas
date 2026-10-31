# AbhishekMandapmalvi/AutoApply

⭐ 21 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/AbhishekMandapmalvi/AutoApply) · [官网](https://github.com/AbhishekMandapmalvi/AutoApply/wiki) · 个人维护

**本地运行的求职自动化桌面应用：搜索评分并代投职位**

面向求职者的全自动求职申请工具：用 Playwright 抓取 LinkedIn 与 Indeed 职位，按偏好对职位打分（0–100），调用 LLM（Anthropic/OpenAI/Google/DeepSeek 可选）生成针对单个职位的简历与求职信，并在 LinkedIn Easy Apply、Indeed Quick Apply、Greenhouse、Lever、Workday、Ashby 六个平台自动填表提交。全部数据保存在本机 ~/.autoapply/，无云端与遥测。后端为 Flask + SQLite，前端 Electron 桌面壳。README 声明自动化操作可能违反第三方平台服务条款，仅供教育和个人用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 职位搜索—打分过滤—AI 生成文档—自动投递—追踪的完整流水线
- 支持 6 个 ATS 平台自动填表与提交，含 full_auto/review/watch 三种模式
- 多 LLM 提供商可选，知识库支持零 API 调用组装简历
- 全本地运行，数据存于 ~/.autoapply/，1385 项测试

## 适用场景

- 批量搜索并按匹配度筛选 LinkedIn/Indeed 职位
- 为每个职位自动生成定制简历与求职信并投递
- 用日程调度让投递任务定时自动运行

## 场景标签

`浏览器自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L5: AutoApply searches LinkedIn and Indeed, scores each job against your preferences, generates tailored resumes and cov
> L15: - **AI-powered documents** — Generates tailored resumes (PDF) and cover letters per job using your choice of AI pro

## 星数曲线

```mermaid
xychart-beta
    title "AbhishekMandapmalvi/AutoApply 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-25", "2026-10-31"]
    y-axis "stars" 17 --> 22
    line [18, 19, 20, 21, 21]
```

2026-10-18 18 → 2026-10-31 21（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1bb4f7232176` · [字段定义](../../DATASET.md)*
