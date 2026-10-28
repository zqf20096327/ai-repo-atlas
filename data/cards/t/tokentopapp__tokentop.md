# tokentopapp/tokentop

⭐ 77 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/tokentopapp/tokentop) · [官网](https://tokentop.app) · 组织维护

**终端实时监控 LLM token 用量与花费的 TUI 工具**

面向使用 AI 编程代理的开发者的终端仪表盘（htop 风格）：轮询 11 家 provider 的用量 API 并本地解析 Claude Code、Cursor 等 8 种编程代理的会话文件，实时计算 token 数、成本、燃烧率；支持预算告警、按模型/项目/代理的费用拆分、7/30/90 天趋势图。凭据自动发现（OAuth/环境变量），数据存本地 SQLite，无遥测。通过 Homebrew/Scoop/npm/独立二进制安装，npm 方式需 Bun 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 11 家 provider + 8 种编程代理的实时 token 与成本监控
- 预算告警（日/周/月限额与可视化提醒）
- 凭据自动发现，数据存本地 SQLite，无遥测
- 插件系统（provider/agent/主题/通知），沙箱权限声明

## 适用场景

- 在终端里实时查看各 AI 编程工具的花费与燃烧率
- 设置预算上限，避免账单超支
- 按项目/模型/代理维度分析 AI 成本构成

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: Real-time terminal monitoring of LLM token usage and spending across providers and coding agents.
> L221: 1. **Provider API polling** — Fetches usage data directly from provider APIs (Anthropic, OpenAI, etc.) on a config
> L222: 2. **Local session parsing** — Watches your coding agent's session files on disk via `fs.watch`, computing token d

## 星数曲线

```mermaid
xychart-beta
    title "tokentopapp/tokentop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-28 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b59f2222d405` · [字段定义](../../DATASET.md)*
