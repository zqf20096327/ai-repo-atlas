# hoangsonww/AI-News-Briefing

⭐ 44 · Shell · MIT · 推送 2026-10-18 · [GitHub](https://github.com/hoangsonww/AI-News-Briefing) · [官网](https://hoangsonww.github.io/AI-News-Briefing/) · 个人维护

**每日自动搜集 AI 新闻并生成简报投递到 Notion/Slack 的流水线**

运行在 macOS（launchd）或 Windows（Task Scheduler）上的定时流水线：每天触发脚本，调用 Claude Code、Codex、Gemini 或 Copilot CLI（无头模式，按序自动回退）作为研究 agent，对 9 个 AI 主题做网络搜索，编译成 TL;DR+完整报告的两层简报，通过 Notion MCP 写入数据库，可选发布到 Obsidian（含 wikilink 图谱）、Teams 和 Slack。另有 Custom Brief 模式，用 5 个并行 agent 按需做任意主题深度研究。安装方式为 git clone 源码并配置平台定时任务，需预装至少一个 AI CLI 与 Notion MCP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 4 种 AI CLI 引擎并按序自动回退
- Custom Brief 模式用 5 个并行 agent 做深度研究
- 投递渠道覆盖 Notion、Obsidian、Teams、Slack
- 通过环境变量配置时区、引擎、模型与每次运行预算上限

## 适用场景

- 每天早上在 Notion/Slack 里收到自动生成的 AI 新闻简报
- 对指定主题发起多角度并行深度研究
- 在 Obsidian 中以图谱形式浏览简报间的主题关联

## 场景标签

`网页抓取` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L47: Automated daily AI news research agent that searches the web, compiles a structured briefing, publishes it to Notio
> L54: AI News Briefing is a fully automated pipeline that runs every morning on your machine. It supports four AI CLI eng
> L58: **Custom Brief** extends this with on-demand deep research: pick any topic, and 5 parallel research agents investig

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/AI-News-Briefing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `00f435afb17c` · [字段定义](../../DATASET.md)*
