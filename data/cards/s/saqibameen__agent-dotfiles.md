# saqibameen/agent-dotfiles

⭐ 14 · TypeScript · MIT · 推送 2026-03-08 · [GitHub](https://github.com/saqibameen/agent-dotfiles) · [官网](https://agent-dotfiles.saqib.dev) · 个人维护

**把 AGENTS.md/CLAUDE.md 规则同步到各编码 agent 的 CLI 工具**

面向同时使用多个 AI 编码 agent 的开发者：读取已有的 AGENTS.md 或 CLAUDE.md 规则文件与 skills 目录，将其同步到 Command Code、Claude Code、Cursor、Copilot、Codex、OpenCode 共 6 种 agent 的对应位置。同步时跳过原生已读取源文件的 agent，只为 Claude Code 生成 CLAUDE.md。提供 copy/symlink 两种写入方式与 skip/overwrite/merge 三种策略，支持 dry-run 预览与全局规则同步，通过 npx 免安装运行，MIT 许可。

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

- 支持 6 种编码 agent 的规则与 skills 同步
- 自动跳过原生已读取源文件的 agent（如 Cursor 读 AGENTS.md）
- skip/overwrite/merge 三种冲突策略与 copy/symlink 写入方式
- npx 免安装运行，支持 --dry-run 预览

## 适用场景

- 项目已有 AGENTS.md，想让 Claude Code 也遵循同一套编码规则
- 把一套 skills 目录同步到多个编码 agent
- 跨 agent 统一维护全局编码规则（~/.claude/CLAUDE.md）

## 场景标签

 · 领域:开发者工具/AI 编码 agent 配置

## 证据(README 行号)

> L7: Most developers already have an `AGENTS.md` or `CLAUDE.md` in their projects. **agent-dotfiles** reads your existing
> L102: `agent-dotfiles` is a **propagator**, not a creator. It reads your existing rules files and syncs them to agent-sp

## 星数曲线

```mermaid
xychart-beta
    title "saqibameen/agent-dotfiles 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f7310ba83af4` · [字段定义](../../DATASET.md)*
