# simonecamerano/italy-job-hunter

⭐ 18 · JavaScript · 推送 2026-05-27 · [GitHub](https://github.com/simonecamerano/italy-job-hunter) · 个人维护

**面向意大利科技岗位的多模型 AI 求职自动化流水线**

基于 Node.js 的自动化求职工具，含两条流水线：Hunt 模式经 Tavily 网络搜索抓取意大利岗位，用 Groq 上的 llama-3.1-8b-instant 做布尔初筛，再由 DeepSeek-V3 对照用户 CV（data/cv.md）生成匹配报告，推送到 Telegram；Scout 模式发现目标公司并生成个性化冷邮件草稿。需自备 Tavily/Groq/DeepSeek/Telegram Bot 四项 API key，搜索词与模型名集中在 src/config.js，可改配置适配其他市场。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两条自动化流水线：岗位搜索匹配报告 + 公司 scouting 冷邮件生成
- 多模型分工：Groq 快速布尔初筛，DeepSeek-V3 做 CV 匹配分析
- 结果以格式化报告推送到 Telegram
- 修改 config.js 与 cv.md 即可适配其他市场/技术栈

## 适用场景

- 我在意大利找工作，想让 AI 每天自动筛岗位并推送匹配报告到 Telegram
- 我想自动发现目标公司并获得可直接发送的冷邮件草稿
- 我想低成本跑大量岗位筛选（20 条岗位成本低于 1 美分）

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L11: **Hunt mode** — finds active job listings targeting the Italian market, runs a fast boolean AI triage, analyzes eac
> L13: **Scout mode** — discovers target companies in Italy and generates a personalized cold-outreach pitch for each one,

## 星数曲线

```mermaid
xychart-beta
    title "simonecamerano/italy-job-hunter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `823181c1ce87` · [字段定义](../../DATASET.md)*
