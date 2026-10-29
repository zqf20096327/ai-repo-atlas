# AgentEra/Agently-Daily-News-Collector

⭐ 644 · Python · Apache-2.0 · 推送 2026-03-10 · [GitHub](https://github.com/AgentEra/Agently-Daily-News-Collector) · [官网](http://agently.tech) · 组织维护

**基于 Agently v4 的自动每日新闻收集工作流示例**

Agently 团队的应用示例项目：输入一个主题，自动执行大纲生成、搜索、筛选、浏览、摘要与分栏撰写，输出 Markdown 格式的多栏目新闻简报。基于 Agently v4 的 TriggerFlow 编排（父流+分栏子流，列与摘要并发执行），使用内置 Search/Browse 工具与 YAML 结构化输出契约，模型配置通过 ${ENV.xxx} 环境变量切换，需 OpenAI 兼容端点。要求 Python>=3.10 与 Agently>=4.0.8.3，默认启用 Playwright 浏览，v3 版本归档于 ./v3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入主题自动生成多栏目新闻简报，保存为 Markdown
- TriggerFlow 父流+分栏子流编排，列与摘要并发执行
- prompt 模板、tools 层、workflow 层分离，可独立替换
- 模型端点通过环境变量配置，兼容 OpenAI 风格 API

## 适用场景

- 输入主题自动收集当日新闻并生成简报
- 学习 Agently v4 TriggerFlow 工作流编排写法
- 在分栏简报基础上扩展自己的新闻采集流程

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L15: - Input a topic and generate a multi-column news briefing automatically
> L83: `outline -> search -> pick -> browse + summarize -> write column -> render markdown`

## 星数曲线

```mermaid
xychart-beta
    title "AgentEra/Agently-Daily-News-Collector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 642 --> 645
    line [643, 644, 644]
```

2026-10-18 643 → 2026-10-29 644（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b729245f8c8a` · [字段定义](../../DATASET.md)*
