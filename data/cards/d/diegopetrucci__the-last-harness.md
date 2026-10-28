# diegopetrucci/the-last-harness

⭐ 37 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/diegopetrucci/the-last-harness) · 个人维护

**基于 Pi 构建的开发者 coding agent 编排框架**

`tlh` 是构建在 Pi 之上的 coding agent 编排框架（TypeScript/CLI），核心机制为 architect-first 工作流：用户只与 architect 对话规划，随后由 developer/reviewer 等子代理自动执行与预审，支持 oracle/contrarian 在不同 provider 上运行以提供独立二次意见。提供 5 种主代理人格（architect/rush/product/bug-hunter/disabled）、子代理运行预算、技能/提示/扩展自定义及 Claude Code 目录兼容。通过 curl 安装脚本分发，声明自身默认较慢且 token 开销较高。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- architect-first 工作流：规划后由子代理自动执行并预审
- oracle/contrarian/reviewer 可运行在与主会话不同的 provider 上
- 5 种主代理人格（architect/rush/product/bug-hunter/disabled）
- 支持用户级与仓库级技能、提示、扩展与自定义子代理

## 适用场景

- 把探索规划与实现执行分离，减少对 agent 的手动看护
- 让独立 provider 上的第二意见代理复核方案
- 通过追加 Markdown 文件为各角色注入项目规范

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: `tlh` (The Last Harness) is an opinionated harness built on top of Pi.
> L81: Subagent orchestration is first-party TLH functionality: the runtime, prompts, and supervision ship in the root pac
> L93: TLH treats Anthropic, OpenAI Codex, and xAI as first-class direct providers. Its bundled xAI defaults use Grok 4.6 

## 星数曲线

```mermaid
xychart-beta
    title "diegopetrucci/the-last-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f7685a7a8cd0` · [字段定义](../../DATASET.md)*
