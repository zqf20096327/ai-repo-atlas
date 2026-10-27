# opendatahub-io/ai-helpers

⭐ 39 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/opendatahub-io/ai-helpers) · [官网](https://opendatahub-io.github.io/ai-helpers/) · 组织维护

**面向 Claude Code/Codex/Cursor 等 AI 编码工具的技能与插件集合**

OpenDataHub 维护的协作仓库，收录按领域组织的 AI 插件（Skills、Agents、Hooks）与 Gemini Gems，用于扩展和自动化编码助手的工作流。当前支持 Claude Code（通过其 plugin marketplace 安装 odh-* 插件）、Codex CLI、OpenCode.ai（仅 skills）、Cursor 与 Gemini 平台。每个 plugins/<plugin>/ 目录是可独立安装的插件，提供含 Claude Code 与 Cursor Agent CLI 的容器镜像（ghcr.io），并附带 make lint 校验、agentskills.io 格式规范与伦理指南。旧 odh-ai-helpers 伞形插件已弃用，建议安装独立 odh-* 插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按领域组织的插件目录，每个插件可独立安装（Skills/Agents/Gems 三类工具）
- 支持 Claude Code marketplace、Codex CLI、OpenCode.ai skills、Cursor 与 Gemini Gems 多平台接入
- 提供预装全部插件的 Claude Code 与 Cursor Agent CLI 容器镜像及 CI 流式输出模式
- make update/lint 构建校验流程，含 agentskills.io 规范 lint

## 适用场景

- 为 Claude Code / Codex CLI 安装现成的领域技能与 agent
- 在容器或 CI 中以非交互方式运行带插件的 AI 编码助手
- 参考现有 SKILL.md 格式示例开发并贡献自己的 AI 插件

## 场景标签

 · 领域:AI 编码助手/开发者工具

## 证据(README 行号)

> L3: This repository is a collaborative place hosting collections of AI plugins to automate and assist with various tasks
> L6: > Right now the focus is to support Claude Code, Codex CLI, OpenCode.ai, Gemini Gems, and Cursor AI.
> L54: Tools are organized into per-domain plugins under `plugins/`. Each `plugins/<plugin>/`

## 星数曲线

```mermaid
xychart-beta
    title "opendatahub-io/ai-helpers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-27 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9f2fd0643c3d` · [字段定义](../../DATASET.md)*
