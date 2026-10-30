# LeonTing1010/tap

⭐ 18 · JavaScript · MIT · 推送 2026-08-09 · [GitHub](https://github.com/LeonTing1010/tap) · [官网](https://taprun.dev/) · 个人维护 · 中文 README

**浏览器自动化 MCP：AI 编译一次任务，之后零 token 确定性重放**

面向 Claude Code、Cursor 等 MCP 宿主的本地优先浏览器自动化工具：AI 检查页面一次，将 URL×自然语言意图编译为 .flow.json 确定性程序（18 操作封闭词表），此后每次执行为纯数据分发、零 LLM token。在用户已登录的真实 Chrome（扩展桥接）或 Playwright 上运行，凭据留在本机。支持 tap verify 快照等价性校验检测页面漂移，提供 Playwright/Puppeteer/Stagehand 适配器转换既有脚本，forge 阶段可 BYOK Claude/OpenAI/DeepSeek 或本地 Ollama。注意引擎为闭源专有，仅 spec 与适配器包开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次 AI 编译为 .flow.json，后续重放零 token 且结果确定
- 复用本机已登录 Chrome 会话，凭据不出本机
- tap verify 快照等价谓词 + 多臂判定检测页面漂移
- Playwright/Puppeteer/Stagehand 脚本转换适配器

## 适用场景

- 让编码 agent 抓取登录墙后的网站数据而不反复烧 token
- 把一次性编写的浏览器操作转为可 cron 调度的确定性任务
- 监控网页变更并在漂移时获得精确 diff 报告

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L27: Works with Claude Code, CodeBuddy, Cursor, Cline, Windsurf, and any MCP host — install straight from the chat windo
> L25: Every other browser agent re-runs a live LLM — and re-burns tokens — on every execution. Taprun's AI agent inspects
> L214:                         ┌─ Chrome extension  (your real browser sessions)

## 星数曲线

```mermaid
xychart-beta
    title "LeonTing1010/tap 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4f16a6b449c6` · [字段定义](../../DATASET.md)*
