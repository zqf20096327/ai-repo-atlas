# Shaurya-Sethi/nightshift

⭐ 14 · Rust · MIT · 推送 2026-10-09 · [GitHub](https://github.com/Shaurya-Sethi/nightshift) · 个人维护

**让 AI 编程代理自动处理 GitHub issue 的 Rust CLI 编排器**

Rust 编写的命令行工具，围绕一个 GitHub 父 issue 的子 issue 依次驱动编码代理自主完成分支、实现、PR、合并的循环，直到全部子 issue 关闭。工作选择基于 GitHub 原生子 issue 关系与 blockedBy 依赖及 ready-for-agent 标签，不解析 issue 正文。开箱支持 7 种代理（Claude Code、Codex CLI、Cursor、Copilot 等），可通过 YAML recipe、dry-run、TUI Watch Board 配置运行；随附 3 个代理技能用于生成父上下文与子 issue。依赖 Rust、Git 与 gh CLI，子 issue 须为原生 sub-issue 并带标签。

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

- 按原生父子 issue 关系与 blockedBy 依赖自动挑选并循环处理 issue
- 开箱支持 7 种编码代理（claude/codex/antigravity/cursor/pi/opencode/copilot）
- YAML recipe、--dry-run、TUI Watch Board 三种运行配置方式
- 随附 3 个代理技能用于发布父上下文与创建带依赖的子 issue

## 适用场景

- 下班后让编码代理自动消化 GitHub 上的 bug 或功能积压
- 围绕一次迁移或功能集批量拆分子 issue 并自动逐个完成
- 用不同代理/模型/推理力度按 issue 粒度编排执行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: nightshift autonomously works through your GitHub issues while you are afk. Point it at a parent issue describing th
> L49: |`--agent`|yes*|n/a|Whole-run default agent: `claude`, `codex`, `antigravity`, `cursor`, `pi`, `opencode`, `copilot
> L78: ## Supported Agents

## 星数曲线

```mermaid
xychart-beta
    title "Shaurya-Sethi/nightshift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `00f35ffe8f57` · [字段定义](../../DATASET.md)*
