# powroom/flins

⭐ 39 · TypeScript · MIT · 推送 2026-04-06 · [GitHub](https://github.com/powroom/flins) · [官网](https://flins.tech/) · 组织维护

**面向 AI 编程代理的统一技能/命令安装管理 CLI**

开源命令行工具 flins，用于在 42 种支持技能的编程代理（Claude Code、Cursor、GitHub Copilot、Cline 等）之间统一安装、更新、列出与卸载 agent 技能和命令。采用符号链接优先架构：源文件存于 .agents/ 单一副本，各代理通过 canonical 项目文件夹共享；默认本地安装写入 universal 共享目录。技能遵循 Agent Skills 开放标准（SKILL.md），支持从 GitHub/GitLab/Codeberg、自带目录及 Cloudflare Well-Known Skills Discovery RFC 域名安装，通过 skills.lock 文件追踪安装状态。命令安装功能仍为实验性，仅限 claude-code、opencode、droid。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一管理 42 种代理集成的技能与命令
- 符号链接优先架构：单一源文件副本，更新一次全代理生效
- 支持 Cloudflare Well-Known Skills Discovery RFC 域名安装
- skills.lock 锁文件用于团队一致性同步

## 适用场景

- 在多个编程代理间一次性安装和更新同一套技能
- 团队通过提交 skills.lock 并运行 flins update 同步技能
- 从任意支持 Agent Skills RFC 的域名直接安装技能

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L5: Install, manage, and update skills and commands across 42 supported agent integrations from one CLI.
> L13: **flins** is an open-source CLI that provides a unified interface for managing agent skills and commands across all

## 星数曲线

```mermaid
xychart-beta
    title "powroom/flins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `23d9608ec8f3` · [字段定义](../../DATASET.md)*
