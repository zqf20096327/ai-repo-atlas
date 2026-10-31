# anton-abyzov/vskill

⭐ 48 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/anton-abyzov/vskill) · [官网](https://verified-skill.com) · 个人维护

**面向 53 个 agent 平台的 AI 技能安装器：装前安全扫描+评测**

AI 技能（SKILL.md）的包管理器与本地开发环境：通过 npx 运行，支持将技能安装到 Claude Code、Cursor、Copilot、Ollama 等 53 个 agent 平台。每次安装执行三级扫描（58 种模式+隐藏内容检查→黑名单→LLM 意图分析），不可跳过；Skill Studio 提供 localhost 工作台，支持 AI 辅助编写技能、A/B 评测（盲评 LLM 裁判）与跨模型基准测试；另有 WebMCP 工具审计与 GitHub Device Flow 认证。提供 macOS/Windows/Linux 桌面应用（Tauri 2）。

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

- 每次安装执行三级安全扫描（模式匹配→黑名单→LLM 意图），不可跳过
- Skill Studio 本地工作台：编写、A/B 盲评、跨模型基准（含 Ollama/LM Studio）
- 一个技能覆盖 53 个 agent 平台（Claude Code、Cursor、Copilot、Codex 等）
- WebMCP 站点工具审计（headless Chromium，9 条规则，SARIF/JSONL 输出）

## 适用场景

- 为我的 Claude Code/Cursor 等 agent 安全地安装社区技能
- 编写技能并用 A/B 评测验证它是否真的提升模型表现
- 审计网站暴露的 WebMCP 工具的安全风险

## 场景标签

`模型评测` `网络安全` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  The package manager for AI skills.
> L46: - **Trust** — every install runs a 3-tier scan (58 patterns + hidden-content checks → blocklist → LLM intent). No `
> L48: - **Reach** — one skill, 53 agents (Claude Code, Cursor, Copilot, Codex, Windsurf, Zed, Gemini CLI, Ollama, …).

## 星数曲线

```mermaid
xychart-beta
    title "anton-abyzov/vskill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-31 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f84d14e56869` · [字段定义](../../DATASET.md)*
