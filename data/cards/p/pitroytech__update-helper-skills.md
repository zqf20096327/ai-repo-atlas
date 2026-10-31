# pitroytech/update-helper-skills

⭐ 16 · 推送 2026-05-18 · [GitHub](https://github.com/pitroytech/update-helper-skills) · 个人维护 · 中文 README

**让 AI agent 安全更新既有代码的技能/协议包**

面向 Cursor、Cline、Claude 等 AI 编程 agent 的 SKILL.md 技能：提供一套更新现有代码的工作协议（先搜索锚点、只读 40-160 行关键区间、区分 SOURCE/GENERATED/REFERENCE 文件、保留 BOM/编码、维护 .bak 回滚路径、验证通过后才清理备份）。含 Lite 与 Full Protocol 两档，按触发词（fix this/refactor 等）自动激活。安装方式：让 agent 自行 clone 仓库、Claude Desktop 内置 Skill Manager 导入 .skill 文件，或手动粘贴到系统提示词。README 声称 MIT 许可、v5。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 技能包，兼容 Cursor/Cline/Windsurf/Antigravity/OpenClaw/Claude
- 锚点搜索+有界读取（40-160 行）替代全文件加载
- 文件分类 SOURCE/GENERATED/REFERENCE，编码与 BOM 保护
- 备份回滚与验证通过后的安全清理门控

## 适用场景

- 让新会话的 AI agent 接手中途项目继续安全打补丁
- 防止 agent 直接改生成文件或误删备份
- 大文件（万行级）与含越南语/CJK/emoji 文件的安全更新

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: The safe, smart way for AI agents to update existing code.
> L59: ### 1. Agentic IDEs & Local Agents (Cursor, Cline, Windsurf, Antigravity, OpenClaw)
> L66: The agent will automatically clone the repo and copy it to the correct location (e.g., `.cursorrules`, `AGENTS.md`,

## 星数曲线

```mermaid
xychart-beta
    title "pitroytech/update-helper-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `197422103bf8` · [字段定义](../../DATASET.md)*
