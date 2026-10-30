# PanisHandsome/ai-rules-sync

⭐ 101 · JavaScript · MIT · 推送 2026-06-03 · [GitHub](https://github.com/PanisHandsome/ai-rules-sync) · [官网](https://panishandsome.github.io/ai-rules-sync/) · 个人维护

**为开发者同步各 AI 编码代理规则文件的 CLI 工具**

agentsync 是一个零依赖的 npm CLI 工具，解决多个 AI 编码代理规则文件（AGENTS.md、CLAUDE.md、.cursorrules、Copilot 指令等 9 种格式）需手工保持同步的问题。核心机制：各格式解析为统一中间表示再渲染为目标格式；支持以单一源文件生成其余文件、--auto 双向同步、merge 合并既有文件、扫描项目生成 AGENTS.md，并可安装 git pre-commit 钩子与 CI 检查。同一引擎驱动 CLI 与纯客户端浏览器 playground。限制：无法翻译的工具特有结构（如 Cursor globs、Claude @path 导入）以警告形式提示。

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

- 支持 9 种 AI 编码代理规则格式的相互转换（Codex/Claude Code/Cursor/Copilot/Windsurf/Cline/Aider/Gemini/Qwen Code）
- 零依赖，同一引擎同时驱动 CLI 与浏览器 playground
- 单一源文件生成其余文件，或 --auto 追踪任意文件编辑并双向同步
- pre-commit 钩子与 sync --check CI 模式保证提交时文件一致

## 适用场景

- 我同时用多个 AI 编码工具，想让规则文件只维护一份
- 在 CI 中检查规则文件是否失去同步
- 把已有的多个规则文件合并成一个 AGENTS.md
- 在浏览器里快速转换或生成一份规则文件

## 场景标签

 · 领域:开发者工具/AI 编码代理

## 证据(README 行号)

> L15: Codex reads `AGENTS.md`. Claude Code reads `CLAUDE.md`. Cursor reads `.cursorrules`.
> L17: tedious and they drift. `agentsync` **converts between all of them** — or
> L20: Zero dependencies. The exact same engine (`src/core/agentsync.js`) powers both the

## 星数曲线

```mermaid
xychart-beta
    title "PanisHandsome/ai-rules-sync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-30 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b0d740b86b6d` · [字段定义](../../DATASET.md)*
