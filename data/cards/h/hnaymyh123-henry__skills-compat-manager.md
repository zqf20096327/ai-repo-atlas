# hnaymyh123-henry/skills-compat-manager

⭐ 84 · Python · MIT · 推送 2026-05-29 · [GitHub](https://github.com/hnaymyh123-henry/skills-compat-manager) · [官网](https://github.com/hnaymyh123-henry/skills-compat-manager) · 个人维护 · 中文 README

**AI agent 技能的跨平台兼容层：执行前依赖预检与 MCP 分发**

面向使用 Claude Code、Cursor、Codex CLI、OpenCode 等 AI agent 的开发者：将技能（SKILL.md）集中到单一库并通过 MCP server 分发给各平台。核心机制是在技能加载时扫描运行环境（Python 包、CLI 工具、环境变量、平台能力），计算 Delta 差异并注入到技能内容顶部（OK/DEGRADED/BLOCKED 协议）。可用 AI 从 SKILL.md 推断生成 COMPAT.yaml（OpenAI→Anthropic→规则三级回退），并提供带安全白名单的 fix 命令与 CI 可用的 verify 退出码。限制：不校验包版本、不验证 API key 有效性、不做沙箱，是咨询层而非防护层。以 pip 从 GitHub 安装，需 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 技能加载前扫描包/CLI/环境变量/平台能力并注入兼容性 Delta 协议
- MCP server 统一分发技能，自动检测 5 个 agent 平台并配置
- AI 推断生成 COMPAT.yaml，三级 provider 自动回退（含无 API key 的规则模式）
- fix 命令经 allowlist/denylist 沙箱执行修复路径，verify 提供退出码可接入 CI

## 适用场景

- 多个 AI agent 工具共用一套技能库，避免跨配置复制
- 技能执行前发现缺失依赖，避免任务中途失败浪费 token
- 在 CI 中用 verify 检查技能兼容性后再部署

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L29: 🗂️ **One library, every agent.** Drop your skills into a single folder. Claude Code, Cursor, Codex CLI, OpenCode — 
> L81: Skills Compat Manager scans your skills **before** the agent runs them, computes a structured **Delta** (gap analys
> L158: The MCP server is the primary runtime interface. When an agent calls `get_skill`:

## 星数曲线

```mermaid
xychart-beta
    title "hnaymyh123-henry/skills-compat-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 82 --> 85
    line [83, 84]
```

2026-10-18 83 → 2026-10-27 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `41010ed91d20` · [字段定义](../../DATASET.md)*
