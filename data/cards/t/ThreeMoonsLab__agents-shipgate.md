# ThreeMoonsLab/agents-shipgate

⭐ 90 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/ThreeMoonsLab/agents-shipgate) · [官网](https://threemoonslab.com/agents-shipgate/) · 组织维护

**本地静态审查 AI agent 权限变更的合并门禁 CLI 与 GitHub Action**

开源 CLI 与 GitHub Action，在合并前对 AI 生成的 agent 能力变更做本地静态 Tool-Use Readiness 审查：读取 MCP、OpenAPI、OpenAI Agents SDK、Anthropic Messages API、Google ADK、LangChain/LangGraph、CrewAI、Codex 配置、n8n 等工件，输出确定性的差异报告与合并裁决（blocked/需人工）。默认无 manifest 可直接对比 PR 中的权限与配置变更；不执行 agent、不调用工具/LLM、不联网。自身声明处于 advisory 阶段，静态分析无法枚举动态构建的工具面时返回 insufficient_evidence 转人工。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- diff 命令无 manifest 对比 PR 中权限/MCP 配置变更
- 确定性裁决引擎，报告与 PR 评论、CI 输出为同一决定的不同投影
- 对 agent 删除门禁自身的行为有 suppression-immune 检查
- 静态分析覆盖不足时返回 insufficient_evidence 而非给出错误结论

## 适用场景

- 在 CI 中审查 coding agent 修改 agent 权限的 PR
- 合并前查看工具面变更（新增工具、scope 扩大）
- 防止 agent 通过删除 CI 门禁使自身 PR 通过

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L17: Agents Shipgate is an open-source CLI and GitHub Action for local-first, static
> L18: Tool-Use Readiness review. It scans MCP, OpenAPI, OpenAI Agents SDK, Anthropic
> L21: deterministic **Tool-Use Readiness Report** before your agent gets

## 星数曲线

```mermaid
xychart-beta
    title "ThreeMoonsLab/agents-shipgate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-24 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d7b4cb2c49aa` · [字段定义](../../DATASET.md)*
