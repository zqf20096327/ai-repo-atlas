# otomachiiii/DevSonar

⭐ 37 · TypeScript · MIT · 推送 2026-02-13 · [GitHub](https://github.com/otomachiiii/DevSonar) · 个人维护

**本地开发用运行时错误监控工具，错误送 Claude 分析**

面向本地开发环境的运行时错误监控工具：CLI 包裹应用进程，通过 node --import 钩子捕获 Node.js 未捕获异常，或从 stderr 检测 Python/Go/Ruby/Java/Rust 的错误模式；浏览器端通过导入包自动挂载错误监听与 fetch 包装。错误汇总至端口 9100 的 relay 服务器，经 Claude Code CLI 或 Agent SDK 分析并给出修复建议。提供 npm/pip/Go 模块三种安装途径及独立 reporter 包，支持 Django/Flask/Express 集成；relay 服务器依赖 Node.js ≥18 与 Claude Code CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 包裹进程自动捕获错误，Node.js 用 --import 钩子，非 Node 进程靠 stderr 模式检测
- 错误经 relay 服务器送 Claude（Agent SDK 或 Claude Code CLI 两种模式）分析
- 支持 Node.js/Python/Go/Ruby/Java/Rust 六种语言的错误捕获
- 提供零依赖独立 reporter 包及 Django/Flask/Express/Go HTTP 中间件集成

## 适用场景

- 本地开发时自动捕获前后端运行时错误并获取 AI 修复建议
- Turborepo 单体仓库中统一监控后端与前端错误
- 在 Python/Go 项目中通过 stderr 或语言 reporter 上报异常

## 场景标签

 · 领域:开发者工具/可观测性

## 证据(README 行号)

> L3: AI-powered runtime error monitoring for local development. Automatically captures errors from your application and s
> L43: - **Claude Code CLI** (`claude` command available) — required for the relay server

## 星数曲线

```mermaid
xychart-beta
    title "otomachiiii/DevSonar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `920fbd879b64` · [字段定义](../../DATASET.md)*
