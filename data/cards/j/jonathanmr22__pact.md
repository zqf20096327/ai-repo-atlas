# jonathanmr22/pact

⭐ 15 · Python · MIT · 推送 2026-06-18 · [GitHub](https://github.com/jonathanmr22/pact) · 个人维护

**面向 AI 编码代理的治理框架：用钩子与检查点约束代理行为**

面向 Claude Code、Cursor、Copilot Workspace 等 AI 编码代理的模块化治理框架，由个人开发者维护、面向独立开发者。核心机制为三层执行：Shell 钩子机械拦截违规工具调用（如硬编码密钥、force-push）、行动前强制输出的八类结构化检查点、决策点自问的认知重定向。另提供本地向量记忆（numpy 回退后端，无需 API key）、多模型委托（Claude 编排、Arcee Trinity/MiniMax 执行）、实时仪表盘与项目分层治理。检测到已有记忆层或任务管理器时只补缺失部分。采用 MIT 许可，版本 0.14.0。

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

- 三层执行机制：机械钩子拦截 + 结构化检查点 + 认知重定向
- 八类必需检查点（bug_fix/solution_compare/package_verify 等）
- 本地向量记忆，numpy-only 后端可在受限主机运行，无需 API key
- 多模型委托：按任务路由到低价 worker 模型，钩子校验所有输出

## 适用场景

- 防止 AI 编码代理提交密钥、编辑未读文件等违规操作
- 让代理在行动前输出结构化分析，减少推理失误
- 独立开发者小团队缺少 code review 时获得治理保障

## 场景标签

`编码 Agent` `代码审查` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L29: PACT is a modular governance framework for AI coding agents (Claude Code, Cursor, Copilot Workspace, etc.). Use all
> L34: 1. **Mechanical Enforcement** — Shell hooks that block violations before they land.
> L43: - **Multi-Model Delegation** — Claude Opus costs $15/M input and $75/M output tokens. That's the right price for ar

## 星数曲线

```mermaid
xychart-beta
    title "jonathanmr22/pact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dd44f1321a97` · [字段定义](../../DATASET.md)*
