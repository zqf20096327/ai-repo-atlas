# wm94i/Work-Review

⭐ 1,839 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/wm94i/Work-Review) · [官网](https://aiqst.com) · 个人维护 · 中文 README

**本地优先的个人工作回顾工具：记录活动并生成日报**

本地优先的个人工作回顾工具，自动记录前台应用、浏览器页面、窗口标题、使用时长及可选截图与 OCR，汇总为可查看的时间线；基于本地记录生成日/周/月报告并支持 Markdown/Obsidian 导出。AI 默认关闭，配置自有模型后可用于问答与摘要，支持 Ollama、LM Studio、OpenAI 兼容接口等多种服务；数据默认存于本地 SQLite，提供关键词过滤、匿名化、锁定暂停等隐私控制。仅面向个人使用，README 明确不用于员工监控。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动记录前台应用、页面、窗口标题、时长与可选截图/OCR
- 基于本地记录的问答与日/周/月报告生成
- 支持 Ollama、LM Studio、DeepSeek 等多种模型服务，模型调用使用用户自有 API key
- 个人 Agent 工作流：技能、定时任务与 MCP 工具调用审批

## 适用场景

- 回顾今天实际做了什么、时间花在哪里
- 快速汇总生成每日工作报告
- 按项目规则统计任务耗时与上下文切换
- 通过 Telegram/飞书/钉钉/企业微信远程查询记录与生成报告

## 场景标签

 · 领域:生产力/时间追踪工具

## 证据(README 行号)

> L5:  A local-first personal work review tool that records context, helps you review your day, and generates daily report
> L41: - **Privacy-first and locally controllable** — Data is stored in local SQLite by default; AI is optional, and model
> L164: The core of Work Review is always **local recording**. AI's role is to make records easier to read and review, not

## 星数曲线

```mermaid
xychart-beta
    title "wm94i/Work-Review 星数(近 17 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-28"]
    y-axis "stars" 1809 --> 1841
    line [1812, 1816, 1818, 1819, 1817, 1811, 1825, 1827, 1828, 1831, 1829, 1830, 1831, 1834, 1833, 1837, 1839]
```

2026-10-26 1,812 → 2026-11-28 1,839（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `49a801e409dd` · [字段定义](../../DATASET.md)*
