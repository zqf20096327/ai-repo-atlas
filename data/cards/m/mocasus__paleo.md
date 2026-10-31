# mocasus/paleo

⭐ 21 · Python · MIT · 推送 2026-07-25 · [GitHub](https://github.com/mocasus/paleo) · [官网](https://github.com/mocasus/paleo) · 个人维护 · 中文 README

**给 LLM agent 省_token 的技能集：压缩输出、裁剪上下文、限定预算**

由 7 个可组合 SKILL.md 技能组成的 agent 省_token 工具：paleo 主技能压缩输出（基准中位节省 53.8%，代码/命令/术语保持逐字不变），另有按任务硬预算（paleo-budget）、上下文裁剪（paleo-trim-context）、会话历史压缩（paleo-converse）、工具输出摘要与 JSON 压缩，以及自动启用技能的 paleo-auto。通过自然语言短语触发，无需 slash 命令，不改动用户代码与 system prompt，无 API key 或外部服务依赖。兼容 Claude Code、Codex、Gemini CLI、Cursor 等 40+ agent。

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

- 7 个可组合技能：输出压缩、上下文裁剪、硬预算、会话压缩、摘要、JSON 压缩、自动检测
- 基准报告：claude-sonnet-4.5 上 6 任务中位输出节省 53.8%，提供可复现测试脚本
- 自然语言短语触发，无需注册命令，不改动用户代码与 system prompt
- 兼容开放 Agent Skills 标准，支持 40+ agent 安装

## 适用场景

- 长会话 agent 任务中降低 token 开销与延迟
- 为工具输出/日志/JSON 密集的任务做摘要与压缩
- 按任务设置硬 token 预算并在超限时摘要收尾

## 场景标签

 · 领域:LLM agent 工具/成本优化

## 证据(README 行号)

> L7: > Token-saving skills for LLM agents — cut output & context tokens without choking the model.
> L36: - [x] **Cross-agent** — open Agent Skills standard: Claude Code, Codex, Gemini CLI, Qwen Code, OpenCode, Cursor, Gi
> L45: |`paleo`|Terse output mode — cut output tokens ~50–70%, keep code/terms exact.|`paleo mode` · `be brief` · `save to

## 星数曲线

```mermaid
xychart-beta
    title "mocasus/paleo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1c098b6cafc5` · [字段定义](../../DATASET.md)*
