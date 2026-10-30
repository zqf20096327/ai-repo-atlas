# wchisasa/rabbit

⭐ 19 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/wchisasa/rabbit) · 个人维护

**浏览器自主 agent 的 Python SDK，用于网页研究分析工作流**

面向开发者的 Python SDK，将浏览器自动化、记忆、任务规划与 LLM 编排组合，构建跨网页的结构化研究与自动化分析工作流。提供核心 agent 循环运行器、模块化 LLM 服务层与可扩展的工具结构，附情绪分析与加密资产分析两个示例脚本。默认配置使用 Gemini（gemini-2.0-flash），通过 .env 配置 API key；浏览器层使用 Playwright/Puppeteer。测试套件为小型确定性回归测试，路线图显示 OpenAI 与 Claude 支持尚未实现。

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

- 浏览器自动化与 agent 工作流编排运行时
- 模块化 LLM 服务层，默认 Gemini、可配 .env 切换
- 记忆与多步任务规划抽象
- 确定性回归测试覆盖关键行为

## 适用场景

- 构建自动打开多个网页并汇总分析的研究工作流
- 在自有工具链中集成浏览器自动化 agent
- 跑通示例脚本做网页内容情绪分析与摘要

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: Rabbit is a Python SDK for browser-based autonomous agents. It combines browser automation, memory, task planning, a
> L13: - LLM integration with a modular service layer

## 星数曲线

```mermaid
xychart-beta
    title "wchisasa/rabbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6c8ac3398885` · [字段定义](../../DATASET.md)*
