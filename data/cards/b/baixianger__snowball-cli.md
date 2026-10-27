# baixianger/snowball-cli

⭐ 24 · TypeScript · 推送 2026-04-03 · [GitHub](https://github.com/baixianger/snowball-cli) · [官网](https://www.npmjs.com/package/snowball-cli) · 个人维护 · 中文 README

**雪球股票数据 CLI：30 条命令输出 JSON 供 AI agent 调用**

封装雪球（Xueqiu）API 的命令行工具，提供 30 条命令覆盖 A 股、港股、美股与基金的实时行情、K线、财报、股东、资金流、7x24 新闻、热帖/KOL、选股器与基金净值等数据，统一输出 JSON 供 AI agent 与脚本消费。认证通过终端二维码、Chrome 扫码或粘贴 cookie 获取 token，可在机器间导出/导入；部分命令无需登录。npm 全局安装，基于 Bun，附 VPS/Docker 部署指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 条命令覆盖行情、财报、资金流、社交与基金数据
- 统一 JSON 输出，面向 AI agent 与脚本
- 二维码/浏览器/cookie 三种登录方式，token 可跨机器迁移
- 支持 A 股、港股、美股与基金，含 KOL 文章与 7x24 新闻

## 适用场景

- 让 AI agent 获取 A 股/港股/美股行情与财报数据
- 自动化生成每日市场简报（指数+要闻+热帖）
- 脚本化拉取资金流、龙虎榜与基金净值数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L16: A CLI that wraps Xueqiu (雪球) APIs into JSON for AI agents and scripts.
> L6:  30 commands | A-shares, HK, US stocks & funds | JSON output

## 星数曲线

```mermaid
xychart-beta
    title "baixianger/snowball-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dc9dfa357774` · [字段定义](../../DATASET.md)*
