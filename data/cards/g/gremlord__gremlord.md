# gremlord/gremlord

⭐ 15 · Go · MIT · 推送 2026-09-28 · [GitHub](https://github.com/gremlord/gremlord) · [官网](https://runagentic.dev) · 个人维护

**给开发者的 Claude Code 本地多模型路由器：带预算与花费追踪**

gremlord 是一个用 Go 编写的本地路由器，包裹未修改的 Claude Code：通过 ANTHROPIC_BASE_URL 网关把会话路由到 Anthropic、OpenAI、xAI 或任何 OpenAI 兼容后端（Ollama、vLLM、OpenRouter、DeepSeek、Groq），也可把任务委托给本地登录的 Codex 或 Grok CLI。每个 API token 被计量计价，支持日/周/月硬停预算、gremlord cost 命令与实时状态栏。提供基于 LLM 分类器的 auto 分层路由与任务级映射。无守护进程，单个静态 Go 二进制，首个会话绑定端口并服务其他会话。面向单个开发者，非团队网关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 ANTHROPIC_BASE_URL 网关在不修改 Claude Code 的前提下切换任意 OpenAI 兼容模型
- 逐 token 计量计价，日/周/月硬停预算与 gremlord cost 花费查询
- LLM 分类器 auto 分层路由（deep/standard/light）+ 7 种任务标签映射
- 无守护进程的静态 Go 二进制，领导者选举自动接管端口

## 适用场景

- 继续用 Claude Code 界面但把日常编码切到便宜模型
- 限制每天/每周的 API 花费并查看花费去向
- 让分类器按任务难度自动在重/中/轻模型间切换

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: gremlord wraps Claude Code in a thin local router. Your sessions look and feel exactly like `claude` — same TUI, sa
> L34: gremlord answers both without touching Claude Code itself. Claude Code officially supports pointing at a gateway vi

## 星数曲线

```mermaid
xychart-beta
    title "gremlord/gremlord 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `f147eee0a670` · [字段定义](../../DATASET.md)*
