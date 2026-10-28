# jiawei686/jev-ultrafast-mcp

⭐ 20 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/jiawei686/jev-ultrafast-mcp) · [官网](https://pypi.org/project/jev-ultrafast-mcp/) · 个人维护 · 中文 README

**把整个浏览器任务一次性交给服务端决策模型执行的 MCP 服务器**

面向 MCP 客户端（Claude Code、Cursor、Codex CLI 等 9 种）的浏览器自动化服务器：agent 通过一次 browser_goal 调用交付 URL、目标与校验条件，循环由服务端的 Jev 决策模型（TypeSafe）驱动，模型从页面自带元素表中选择 ref 而非自写选择器，服务端拒绝页面上不存在的目标。browser_assert 用代码校验页面结果；录制的宏重放零模型调用、无需 key。基于 Chrome DevTools Protocol 直连已有 Chrome，不依赖 Playwright/Selenium。需要 Python ≥ 3.10 与 Chromium 系浏览器，仅 browser_goal 需要模型 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- browser_goal 一次调用完成多步浏览器任务，循环在服务端运行
- 模型从页面 ref 元素表中选目标，服务端拒绝不存在的元素
- 宏重放零模型调用，browser_assert 用代码校验页面结果
- 直连 CDP，无需 Playwright/Selenium，无截图流水线

## 适用场景

- 让 agent 用一次调用完成表单填写、搜索提交等浏览器流程
- 重复性浏览器任务录制为宏后零模型成本重放
- 以代码断言校验 agent 的浏览器操作结果

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: **Hand the browser work off — an MCP server that drives the page for your agent.**
> L134: runs here, server-side, with Jev — TypeSafe's decision model — choosing each step. The model never
> L152: Everything *except* `browser_goal` — `browser_open`, `browser_observe`, `browser_act`,

## 星数曲线

```mermaid
xychart-beta
    title "jiawei686/jev-ultrafast-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `451280e0b9d4` · [字段定义](../../DATASET.md)*
