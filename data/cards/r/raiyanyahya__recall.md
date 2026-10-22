# raiyanyahya/recall

⭐ 762 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/raiyanyahya/recall) · [官网](https://recallplugin.dev) · 个人维护

**给 Claude Code/OpenCode 的本地会话记忆插件**

面向 Claude Code（OpenCode 可选支持）的插件：通过 Stop/SessionEnd 钩子把每轮会话追加写入 .recall/history.md，用本地 TF-IDF + TextRank 抽取式摘要器（纯 Python，numpy 可选加速）生成 1-2K token 的 context.md，供下次会话恢复上下文。全程无 LLM 调用、无网络请求、无 API key。Claude Code 经插件市场安装，OpenCode 通过一次性 installer 脚本接入，两种 harness 共享同一份 markdown 记忆。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话活动自动追加记录到 .recall/history.md
- 本地 TF-IDF + TextRank 生成摘要，无 LLM 调用与网络请求
- context.md 约 1-2K token，作为恢复点加载到新会话
- 支持 Claude Code 与 OpenCode 共享同一份项目记忆

## 适用场景

- 每个新会话让 Claude Code 记得上次做到哪里
- 减少重复解释项目背景消耗的 token
- 团队提交 .recall/ 目录作为共享项目记忆

## 场景标签

 · 领域:开发者工具/AI 编码助手

## 证据(README 行号)

> L11: > Claude Code starts every session cold. Recall keeps a local log of your
> L78: |**During the session**|The `Stop` / `SessionEnd` hooks append new activity to `.recall/history.md`. Capture is inc
> L83: There is no LLM call anywhere — the summary is produced by **TF-IDF + TextRank**

## 星数曲线

```mermaid
xychart-beta
    title "raiyanyahya/recall 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 758 --> 763
    line [759, 761, 762]
```

2026-10-18 759 → 2026-10-22 762（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `39d06d7d30c4` · [字段定义](../../DATASET.md)*
