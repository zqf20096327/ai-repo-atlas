# Ouro-labs/ouroboros-plugins

⭐ 16 · JavaScript · MIT · 推送 2026-08-15 · [GitHub](https://github.com/Ouro-labs/ouroboros-plugins) · 组织维护

**Agent OS Ouroboros 的 23 个参考插件与 UserLevel 插件契约**

为 Ouroboros（自称 Agent OS）提供 UserLevel 插件契约草案与 23 个参考插件包，覆盖自动研究、GitHub PR 操作、护栏评测、Langfuse 可观测性、Jira/Linear 同步等域工作流；并含 Anthropic/OpenAI Agent Skills 同化参考插件与外部仓库能力同化机制。插件通过 `ouroboros plugin add` 命令安装，核心负责原语（账本、权限、审计、运行时抽象），插件组合为领域工作流。仓库自述为 Draft 状态，尚非注册服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 定义 UserLevel 插件契约 MVP（manifest、命名空间、权限、来源/审计要求）
- 23 个参考插件：autoresearch、github-pr-ops、guardrails-eval、langfuse-observability 等
- Anthropic/OpenAI Agent Skills 同化参考插件
- contract-validation GitHub Actions 校验插件契约

## 适用场景

- 为 Ouroboros 安装领域工作流插件（如自动研究、PR 操作）
- 参照契约开发自定义 UserLevel 插件
- 了解外部技能目录如何被同化为受权限与审计约束的插件

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: 23 reference plugins for Ouroboros, the Agent OS — autoresearch, github-pr-ops, guardrails-eval, langfuse-observabil
> L7: Ouroboros core should provide stable OS primitives. Plugins and first-party
> L42: - MCP tool surfaces

## 星数曲线

```mermaid
xychart-beta
    title "Ouro-labs/ouroboros-plugins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c1b8ba74ee22` · [字段定义](../../DATASET.md)*
