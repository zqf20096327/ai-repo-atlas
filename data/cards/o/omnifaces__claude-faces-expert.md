# omnifaces/claude-faces-expert

⭐ 28 · Shell · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/omnifaces/claude-faces-expert) · 组织维护

**面向编码 Agent 的 Jakarta Faces 知识库，随装随用**

由 BalusC（OmniFaces）基于其 Stack Overflow 回答整理的 Jakarta Faces（原 JSF）知识库，以规则与主题文件形式注入 Claude Code 等编码 Agent 的上下文，覆盖术语、view state、生命周期、转换校验、常见错误诊断决策树，并含 PrimeFaces 与 OmniFaces 专章。另附 /faces-review 与 /faces-migrate 两个技能（仅 Claude Code 与 Cursor 支持斜杠调用）。提供 curl 安装脚本与手动安装两种方式，并为 GitHub Copilot、Cursor、Codex、OpenCode、Antigravity 提供专属安装器；Copilot 与 Codex 因不解析文件引用而将规则内联。限制：需 git 与 POSIX shell（Windows 需 Git Bash 或 WSL）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心规则 + 8 个主题文件（配置/诊断决策树/PrimeFaces/OmniFaces/生命周期等）
- 两个技能：/faces-review 代码审查与 /faces-migrate 版本迁移
- 5 种第三方编码工具（Copilot/Cursor/Codex/OpenCode/Antigravity）专属安装器
- 安装幂等，重跑即更新，不改写已有 CLAUDE.md

## 适用场景

- 让 Claude Code 编写 Jakarta Faces 代码时遵循最佳实践
- 通过 /faces-review 审查已有 Faces 代码的常见错误
- 在 Cursor/Copilot 等 IDE Agent 中引入 JSF 领域知识

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Drop-in Jakarta Faces knowledge base for Claude Code, with installers for GitHub Copilot, Cursor, Codex, OpenCode an
> L9: Curated by BalusC based on his Stack Overflow answers to frequently asked Jakarta Faces questions.
> L23: |File|Description|

## 星数曲线

```mermaid
xychart-beta
    title "omnifaces/claude-faces-expert 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1135ed652513` · [字段定义](../../DATASET.md)*
