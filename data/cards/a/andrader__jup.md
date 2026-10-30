# andrader/jup

⭐ 17 · Python · 推送 2026-08-08 · [GitHub](https://github.com/andrader/jup) · [官网](https://andrader.github.io/jup/) · 个人维护

**跨 AI 助手安装与同步 agent 技能的命令行工具**

Python 编写的 CLI 工具 jup，面向使用多个 AI 编程助手的开发者：从含 skills/ 目录的 GitHub 仓库或本地路径安装 agent 技能，以 lockfile 记录来源并集中管理，通过 jup sync 以符号链接（或复制）方式同步到 Gemini、Copilot、Claude、Codex 等助手的技能目录；支持从 skills.sh 注册表搜索、更新检查与实验性 TUI 仪表盘，可自定义 harness 提供方。经 PyPI（uv/pip）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- lockfile 集中管理技能来源与更新状态
- 默认符号链接同步到多个 AI 助手的技能目录，可切换为复制
- 支持 skills.sh 注册表搜索与交互式安装（jup find --interactive）
- 可添加使用标准 skills/ 目录结构的自定义 harness 提供方

## 适用场景

- 在多个 AI 编程助手中复用同一套 agent 技能
- 团队通过 lockfile 统一技能来源并跟踪更新
- 本地编写技能后同时链接到 Claude、Gemini、Copilot 目录

## 场景标签

 · 领域:AI 开发者工具/agent 技能管理

## 证据(README 行号)

> L3: `jup` is a small command-line tool for installing and syncing agent skills across the local skill directories used b
> L16: - **Multi-Harness Support**: Sync skills for Gemini, Copilot, Claude, and Codex.
> L209: Skills are placed directly into the harness's skill folder (e.g., `~/.gemini/skills/my-skill/`), ensuring they are

## 星数曲线

```mermaid
xychart-beta
    title "andrader/jup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4fc03a0cc55c` · [字段定义](../../DATASET.md)*
