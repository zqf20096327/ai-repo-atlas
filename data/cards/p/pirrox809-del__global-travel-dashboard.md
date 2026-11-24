# pirrox809-del/global-travel-dashboard

⭐ 3 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/pirrox809-del/global-travel-dashboard) · [官网](https://global-travel-dashboard.vercel.app) · 个人维护

**面向旅行者的 250 国数据仪表盘，附 AI 生成国家指南**

基于 Next.js 16 的全栈旅行仪表盘，覆盖 250 个国家：通过 3D 地球选国，展示天气、汇率、旅行警示、地震与 GDP 等实时数据。LLM 在首次访问时生成国家简介（文化、美食、地点、价格估算），写入预填充的 SQLite 数据库后持久化，并由 Vercel Cron 每日轮换刷新最旧的 2 条。AI 功能依赖 OpenAI 兼容端点凭据，未配置时实时数据与预生成简介仍正常工作，仅聊天禁用。支持 4 种界面语言与深浅主题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成的国家简介首次访问后持久化，后续即时加载
- 每日轮换机制：cron 刷新 2 条最旧简介并提交回仓库触发重新部署
- 未配置 AI 凭据时实时数据与 250 国预生成简介继续可用
- 3D 地球选国、随机国家、地球测验、国家对决等交互功能

## 适用场景

- 出行前在一个页面查看目的国的天气、汇率与安全警示
- 快速了解某国的文化习俗、美食与推荐地点
- 通过地球测验和国家对决学习地理知识

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L10: A travel dashboard for **250 countries — none excluded**. Live weather, exchange rates, travel advisories, earthqua
> L92: Without the AI variables nothing breaks: live data and all 250 pre-generated briefs keep working — the chatbot just
> L100: - Travel AI needs LLM credentials: either a `.z-ai-config` file or `ZAI_BASE_URL` + `ZAI_API_KEY` environment vari

## 星数曲线

```mermaid
xychart-beta
    title "pirrox809-del/global-travel-dashboard 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a9a4da833bdd` · [字段定义](../../DATASET.md)*
