# simota/agent-skills

⭐ 95 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/simota/agent-skills) · [官网](https://simota.github.io/agent-skills/) · 个人维护

**面向 Claude Code/Codex/Antigravity CLI 的 90 个专业 AI agent 技能集**

遵循 Anthropic Agent Skills 规范（SKILL.md 格式）的技能集合：90 个全局可复用 agent 覆盖编排、调查规划、安全、设计、测试、FinOps、合规等领域，另有 3 个仓库本地扩展（orbit/lore/darwin）。Nexus 编排器负责任务分析与 agent 链设计，另含 49 个 Recipes 与 11 个 Skill Packs。通过 make link 以符号链接方式安装到 ~/.claude/skills、~/.agents/skills 与 ~/.gemini/antigravity-cli/skills，使多个 CLI 共享同一工作树，git pull 即可全部更新；已存在文件不被覆盖。技能本身与模型无关，实际可用性需运行时验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 90 个全局 agent + 3 个仓库本地扩展，按类别组织
- Nexus 编排器分析任务并设计最小可行 agent 链
- make link 将技能符号链接至三个 CLI 目录，单一 git pull 更新全部
- 平台无关：支持 Claude Code、Codex CLI、Antigravity CLI

## 适用场景

- 为 Claude Code 等 CLI 安装一套覆盖开发、测试、合规等领域的专业 agent
- 通过 Nexus 让多个专业 agent 协同完成一个功能交付
- 多 CLI 环境下共享同一份技能工作树统一维护

## 场景标签

`多智能体` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: A skill collection that enables collaborative development with a team of specialized AI agents.
> L13: - **Platform Agnostic** - Works with Claude Code, Codex CLI, Antigravity CLI, and others
> L27: `make link` symlinks each skill directory into `~/.claude/skills`, `~/.agents/skills`, and

## 星数曲线

```mermaid
xychart-beta
    title "simota/agent-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 92 --> 96
    line [93, 95, 95]
```

2026-10-18 93 → 2026-10-25 95（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `5e37e52dbfa6` · [字段定义](../../DATASET.md)*
