# Galileo-Agent-Labs/eval-engineer

⭐ 43 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/Galileo-Agent-Labs/eval-engineer) · [官网](https://galileo.ai/blog/introducing-eval-engineer-bringing-eval-expertise-to-claude-and-codex) · 组织维护

**将 Galileo 评测工作流注入 Claude Code 与 Codex 的技能包**

以可安装技能（skills）形式为 Claude Code 和 Codex 等编码代理提供 Galileo 评测工作流：代理可检查 Galileo traces 与指标、生成 debug packet、按失败契约选指标、做根因分析、提出最小改动并通过前后验证确认改进。安装通过 uvx 从 git 仓库运行 installer，将技能写入项目或用户目录；宿主代理提供代码访问与执行能力，技能本身不含执行环境。首个示例为工具调用支持代理，设计上面向代理、RAG 应用等多种场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为编码代理提供 inspect→diagnose→bounded fix→verify 的评测循环技能
- 将 Galileo URL/ID 转为本地 debug packet 并做前后对比验证
- uvx 一键安装，同时支持 Codex 与 Claude Code 项目级/用户级作用域

## 适用场景

- 让 Claude Code 或 Codex 基于 Galileo 证据诊断 AI 应用失败并验证修复
- 在代理/RAG 项目中建立带前后验证的评测工作流
- 对比基线与验证运行的指标与成本

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Eval Engineer routes Galileo evidence into coding-agent RCA and verification
> L149: The host agent provides repo access, command execution, and code edits. The

## 星数曲线

```mermaid
xychart-beta
    title "Galileo-Agent-Labs/eval-engineer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a0bbce735b50` · [字段定义](../../DATASET.md)*
