# MeherBhaskar/agent-rigor

⭐ 41 · Shell · MIT · 推送 2026-07-11 · [GitHub](https://github.com/MeherBhaskar/agent-rigor) · 个人维护

**给 AI 编程助手的工程纪律技能库：18 个 Agent Skill 约束代理行为**

纯 Markdown 构成的 Agent Skills 框架，将克隆到项目 .agents/ 目录后，通过 SYSTEM_CORE.md 由 Apex Kernel 路由到 6 个阶段（任务综合、执行、验证、认知持久、接口、自适应）共 18 个技能，为 AI 编程代理提供可验证步骤、状态检查点、回归测试等约束。平台无关，适配 Claude Code、Cursor、Gemini CLI、Aider、GitHub Copilot 等工具。配套 RigorBench（arXiv:2606.22678）在 100 任务上评测，并维护 RigorScore 排行榜。

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

- 18 个技能按 6 阶段组织，按需加载以节省上下文
- 纯 Markdown，兼容 Cursor/Claude Code/Gemini CLI/Aider/GitHub Copilot
- 配套 RigorBench 评测与 RigorScore 实时排行榜

## 适用场景

- 让 AI 编程代理遵循规划、测试、验证的工程流程
- 防止代理陷入 doom loop 或范围蔓延
- 对比各代理在流程纪律维度的表现

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L36: **Agent Rigor** is a framework of modular Agent Skills designed to encourage mature, battle-tested software enginee
> L56: Agent Rigor is pure markdown. It works natively with standard AI tools:

## 星数曲线

```mermaid
xychart-beta
    title "MeherBhaskar/agent-rigor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-27 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e03336400681` · [字段定义](../../DATASET.md)*
