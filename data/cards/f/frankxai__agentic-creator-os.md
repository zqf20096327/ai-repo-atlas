# frankxai/agentic-creator-os

⭐ 13 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/frankxai/agentic-creator-os) · [官网](https://frankx.ai/products/agentic-creator-os) · 个人维护

**面向创作者工作流的可复用 AI 技能/命令/代理目录与本地安装工具**

ACOS 是一个可本地安装的开源 AI 工作流仓库：包含 176 个技能模块、85 个斜杠命令、81 个代理配置、9 个 shell hook 与 32 条激活规则，通过 install.sh 复制到 CLAUDE_HOME 或生成 Cursor/Windsurf/Gemini/Grok 等平台的适配文件，也可作为 Claude Code marketplace 插件安装 creator-os-core（含五个实践技能与 /acos 命令）。另含九个“Generals”代理模板编译脚本与本地实践回执检查器（HTTP/MCP）。自述为实验性状态，需操作者与外部 harness 才能运行，非托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 176 个技能模块 + 85 个命令 + 81 个代理配置，install.sh 一键安装到 Claude 配置目录
- 支持 claude/cursor/windsurf/gemini/grok 等多平台 flag 生成适配文件
- creator-os-core 插件提供五个实践技能与 /acos 命令
- 本地回执检查器提供 HTTP 与 MCP 两种接口（127.0.0.1:8787）

## 适用场景

- 为 Claude Code 等 harness 批量安装技能、命令与代理配置
- 以插件形式引入五个创作者实践（安全启动、diff 审查、检查运行等）
- 基于模板编译自己的多代理（Generals）实例

## 场景标签

`多智能体` `精选清单` · 领域:Agent 开发

## 证据(README 行号)

> L26: |Non-empty skill modules|176|Non-empty `.claude/skills/**/SKILL.md` files|
> L29: |Top-level agent profiles|81|`.claude/agents/*.{md,json}`, excluding the directory context file|
> L62: The Claude path copies the repository's skill groups, top-level commands, agent profiles, shell hooks, hook configu

## 星数曲线

```mermaid
xychart-beta
    title "frankxai/agentic-creator-os 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `bad7bd14ef43` · [字段定义](../../DATASET.md)*
