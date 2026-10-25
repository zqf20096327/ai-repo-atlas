# AltimateAI/claude-consensus

⭐ 33 · MIT · 推送 2026-08-25 · [GitHub](https://github.com/AltimateAI/claude-consensus) · [官网](https://altimate.ai/) · 组织维护

**Claude Code/Codex 的多模型共识代码与方案评审插件**

以插件形式接入 Claude Code 与 Codex 的评审工具：由宿主模型担任主评（Claude Code 中 Claude 主导，Codex 中 Codex 主导），多个外部模型独立评审代码、实现计划、文档或技术提案，经结构化综合与批准轮次收敛为共识结论。支持可配置法定人数（quorum）、模型不可用时降级跳过、各模型独立评审避免交叉污染，评审产物存于 /tmp/ 供审计。模型接入方式包括 OpenRouter（经 pi CLI 单密钥路由）与各原生 CLI，面板覆盖 Claude、GPT、Gemini、Kimi、Grok、GLM、Qwen、DeepSeek 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型独立评审后结构化综合收敛的共识机制
- Claude Code 与 Codex 双宿主，宿主模型担任主评
- 可配置 quorum 与不可用模型降级跳过
- 经 pi CLI 用单个 OpenRouter API key 路由多模型

## 适用场景

- 提交代码前让多个模型交叉评审暂存改动
- 实现复杂功能前对技术方案做多模型共识评审
- 对架构文档等一般性材料做多模型评审

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: **Multi-model code review, plan review, and general review for Claude Code and Codex**
> L8: Multiple AI models independently review code, implementation plans, documents, or technical proposals, then converge
> L64: |pi CLI|Recommended|Routes OpenRouter models with one API key|

## 星数曲线

```mermaid
xychart-beta
    title "AltimateAI/claude-consensus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8494676df3f0` · [字段定义](../../DATASET.md)*
