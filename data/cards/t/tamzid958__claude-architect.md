# tamzid958/claude-architect

⭐ 76 · Shell · 推送 2026-03-03 · [GitHub](https://github.com/tamzid958/claude-architect) · 个人维护

**为 Claude Code CLI 提供项目生成与开发命令协议的框架**

一套安装到 ~/.claude/ 目录的 Markdown 命令与配置框架，配合 Claude Code CLI 使用：包含全局 CLAUDE.md 默认规则、15 个命令（/scaffold、/plan、/review、/debug 等）及覆盖 12 个生态、32 个框架的约定文件（Next.js、Django、Spring Boot、Flutter 等）。框架文件采用三层继承（全局→语言 base→框架 delta-only）以降低 token 消耗；README 给出按任务划分的 Sonnet/Opus 模型使用建议与 token 预算表。通过 install.sh 安装，重复运行可更新，/onboard 只生成文档不改源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个 Claude Code 斜杠命令（scaffold/plan/review/debug/migrate 等）
- 32 个框架约定文件、12 个语言生态，三层继承仅存增量内容
- 澄清分级（1-3 级）与分阶段执行、构建/测试质量门
- install.sh 一键安装/更新，自动备份现有 CLAUDE.md

## 适用场景

- 让 Claude Code 按 /scaffold 协议从规格生成新项目
- 用 /onboard 分析既有项目并生成 CLAUDE.md 约定
- 按 Sonnet/Opus 分工建议组织规划与执行工作流

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A plug-and-play framework for generating projects with Claude Code CLI — optimized for speed, token efficiency, and 
> L14: |`scaffold.md`|`~/.claude/commands/scaffold.md`|Full scaffolding protocol (`/scaffold`)|
> L91: claude

## 星数曲线

```mermaid
xychart-beta
    title "tamzid958/claude-architect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-29 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `46b8704a3feb` · [字段定义](../../DATASET.md)*
