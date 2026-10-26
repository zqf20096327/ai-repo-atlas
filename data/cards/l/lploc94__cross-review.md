# lploc94/cross-review

⭐ 153 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/lploc94/cross-review) · [官网](https://cross-review.tlelabs.com) · 个人维护

**跨模型代码审查技能包：一个 agent 编排、另一模型审查方案与代码**

面向 Claude Code 与 OpenAI Codex CLI 的技能包：工作时所在的 agent 作为编排者，由第二个模型（默认 Codex CLI，可选 Claude Code 或 Antigravity）审查其实现计划、代码与推理。提供 6 个技能（loop-plan、loop-implement、review-plan、review-impl、review-think、review-pr），通过共享 runner 与各 reviewer CLI 的适配器驱动，注册 MCP server，并附带本地 Web 仪表盘查看审查会话、计划进度与设置。要求 Node.js>=22 与至少一个 reviewer CLI 在 PATH 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个技能覆盖计划编写、TDD 分阶段执行、计划/实现/推理/PR 审查
- reviewer 可选 Codex/Claude Code/Antigravity，各自独立配置模型与 effort
- 注册 MCP server，提供 review_begin/wait/reply/end 工具与 CLI 回退路径
- 本地仪表盘实时展示审查会话轮次、issue 台账与计划进度，仅监听 127.0.0.1

## 适用场景

- 让另一个模型在编码前审查实现计划
- 提交/合并前审查未提交改动或分支
- 对他人 PR 做同行式审查
- 通过仪表盘跟踪审查会话与分阶段计划进度

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Cross-model review skills for Claude Code and OpenAI Codex CLI: the agent you work with orchestrates, and a second 
> L15: Six skills (Claude Code: `/name`, Codex: `$name`):
> L76: - The review skills use the MCP tools `review_begin`, `review_wait`, `review_reply`, `review_end`. Without MCP, or 

## 星数曲线

```mermaid
xychart-beta
    title "lploc94/cross-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-10-18 153 → 2026-10-26 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ea2c61dae3aa` · [字段定义](../../DATASET.md)*
