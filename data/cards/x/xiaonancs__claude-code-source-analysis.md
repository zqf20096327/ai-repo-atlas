# xiaonancs/claude-code-source-analysis

⭐ 95 · JavaScript · NOASSERTION · 推送 2026-05-27 · [GitHub](https://github.com/xiaonancs/claude-code-source-analysis) · 个人维护 · 中文 README

**Claude Code v2.1.88 源码逆向解析的研究文集（30 篇）**

基于逆向还原的 Claude Code v2.1.88 源码快照（1,884 个 TypeScript/TSX 文件、约 51 万行）撰写的系统性架构研究文集：30 篇文章、179 张架构图，按 Foundations（启动/上下文/记忆/缓存）、Execution（工具/权限/Agent/MCP/Hooks）、Infrastructure（特性开关/API/终端渲染）三大部组织为 23 个子系统章节，附 Skill/Plugin、LSP 等附录。参考社区文章调研与 Anthropic 官方工程博客，声明内容用于教育和研究目的。属系列研究之一，另有 Codex、Hermes Agent、OpenClaw 等姊妹篇。

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

- 覆盖 23 个子系统 / 179 张架构图 / 26,000+ 行研究文本
- 基于 v2.1.88 源码快照（1,884 个 TS 文件、513,216 行）的逆向还原分析
- 三层结构：Foundations / Execution / Infrastructure + 附录
- 参考 120+ 篇社区技术文章调研与 Anthropic 官方工程博客

## 适用场景

- 理解 Claude Code 作为 Agent 运行时的架构设计
- 研究 Agent Harness 的启动链路、上下文管理与权限体系实现
- 为自研 coding agent 借鉴可迁移的架构模式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: 基于逆向还原的 `v2.1.88` 源码快照，系统级工程视角重建 Claude Code 的完整 Agent Harness 实现。
> L6:  30 篇文章 / 23 个子系统 / 179 张架构图 / 26,000+ 行研究文本。

## 星数曲线

```mermaid
xychart-beta
    title "xiaonancs/claude-code-source-analysis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 93 --> 96
    line [94, 95, 95]
```

2026-10-18 94 → 2026-10-31 95（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `186ad5d28ece` · [字段定义](../../DATASET.md)*
