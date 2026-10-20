# wanshuiyin/Auto-claude-code-research-in-sleep

⭐ 17,728 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) · 个人维护 · 中文 README

**给 ML 研究者提供跨模型审查循环的 Markdown 技能集**

ARIS 是一套纯 Markdown 的技能/工作流方法，用于自主 ML 研究：由执行模型驱动、独立模型（默认 Codex MCP）做跨模型审查，覆盖想法发现、实验自动化与审查循环。定位为方法论而非平台，可安装到 Claude Code、Codex CLI、Cursor、OpenClaw 等 agent 环境，也提供独立 CLI（ARIS-Code）与各平台插件发行，含 82-83 个技能；README 说明 codex-cli 0.154 移除 mcp-server 后改用 codex exec 桥接，替代模型组合无需 Claude 或 OpenAI API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.0 天,年发版 46,84 位贡献者
- 涨星:近 1 天 **+62**(自 20261016 起算)
- 安装:npm 包 `@google/gemini-cli` 月下载 1,647,448
- 平台:WINDOWS / MACOS · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 跨模型审查循环：执行者驱动，独立模型（默认 Codex MCP）审查
- 纯 Markdown 技能形式，82-83 个技能，无框架依赖
- 提供独立 CLI（ARIS-Code）及 Claude Code / Codex CLI / DeepSeek Harness 插件
- 支持 ModelScope 托管模型的替代模型组合，无需 Claude/OpenAI API

## 适用场景

- 让 agent 在夜间自主推进 ML 研究实验与审查循环
- 在 Claude Code / Codex CLI / Cursor 等环境中安装研究工作流技能
- 为想法发现与实验自动化配置跨模型审查门控

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: 🌱 *ARIS is a methodology, not a platform. What matters is the research workflow — take it wherever you go.*
> L11: 💡 *Use ARIS as a skill-based workflow in Claude Code / Codex CLI / Cursor / Trae / Antigravity / GitHub Copilot CLI
> L13: 📦 *Those are the skills installed directly. Want it in one command? ARIS also ships as a standalone CLI and as plug

## 星数曲线

```mermaid
xychart-beta
    title "wanshuiyin/Auto-claude-code-research-in-sleep 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 17617 --> 17738
    line [17627, 17728, 17728]
```

2026-10-18 17,627 → 2026-10-20 17,728（+101）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 low · 依据 README sha `9ccdb46e5f5a` · [字段定义](../../DATASET.md)*
