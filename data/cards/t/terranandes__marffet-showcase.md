# terranandes/marffet-showcase

⭐ 19 · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/terranandes/marffet-showcase) · [官网](https://marffet.zeabur.app) · 个人维护 · 中文 README

**台湾股票 ETF 投资模拟与持仓管理 Web 应用，含 AI 助手**

面向台湾市场投资人的 Web 应用（PWA），提供 20 年以上回测的 Mars 策略模拟器（DuckDB 向量化计算，含 TWSE/上柜/债券 ETF/可转债）、复利计算器、真实持仓追踪（即时损益、到价通知）、个人竞赛动画、ROI 排行榜、主动式 ETF 折溢价看板与筛选器等。AI 部分为基于 Google Gemini 的 Mars AI Copilot 投资助手（免费版/付费版人格与侧重不同）。需 Google 登录，访客模式可浏览模拟器；部分功能按 Guest/FREE/PREMIUM/VIP 分层开放。以托管网址提供，未见本地部署安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mars 策略模拟器覆盖 TWSE/上柜/债券 ETF/可转债，200ms 内出结果
- 主动式 ETF 折溢价看板：NAV 与市价同源同日抓取，无法配对则显示 '—'
- 持仓追踪含即时损益、到价通知、涨跌停色块与手机推送（VIP）
- 基于 Google Gemini 的投资 AI Copilot，免费/付费两档人格与建议侧重

## 适用场景

- 回测并比较台湾股市长期投资策略
- 追踪自己的 ETF 与股票持仓及配息落点
- 查看主动式 ETF 折溢价与筛选基金
- 与其他用户比较 ROI 排名

## 场景标签

`金融量化` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: Marffet is a web-based investment simulation and portfolio management tool that **proves "time in the market beats 
> L147: ### 10. Mars AI Copilot 🤖
> L148: An intelligent investment assistant powered by Google Gemini.

## 星数曲线

```mermaid
xychart-beta
    title "terranandes/marffet-showcase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `923478a67883` · [字段定义](../../DATASET.md)*
