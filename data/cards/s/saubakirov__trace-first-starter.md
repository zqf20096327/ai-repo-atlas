# saubakirov/trace-first-starter

⭐ 30 · HTML · MIT · 推送 2026-10-12 · [GitHub](https://github.com/saubakirov/trace-first-starter) · [官网](https://tfw.saubakirov.kz/) · 个人维护

**人机协作工作流方法论：以可检视 Trace 保存决策与上下文的启动套件**

Trace-First Workflow（TFW）是一套面向人与 AI agent 协同工作的方法论及仓库启动套件：通过精选的持久上下文（Trace）保存目的、决策、被否方案、证据、限制与续作状态，使下一位授权的人或 agent 可检视并继续工作。提供 Assisted 与 Full 两个版本，Full 含完整 HL→RES→TS→ONB→RF→REVIEW 生命周期、模板、工作流与工具适配器（Claude Code、Cursor、Antigravity、Codex），通过 git sparse-checkout 安装到项目根目录。声明不承诺自动生成文档或 agent 独立权限。

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

- Assisted/Full 双版本，含模板、11 类工作流与工具适配器
- 以版本化 Trace 保存决策、证据、限制与续作状态
- 提供 /tfw-plan、/tfw-handoff、/tfw-review 等命令集
- 通过 git sparse-checkout 获取最新 release 并复制入项目根目录

## 适用场景

- 团队在人员或 AI 会话更替后保留并接续工作决策
- 研究者留存每次迭代的前提、发现与限制以备核验
- 工程师将架构决策与被否方案保存在代码附近

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L21: Trace-First Workflow (TFW) makes that work inspectable and continuable. **TFW is a methodology for joint human–AI w
> L23: This repository is the complete TFW starter: choose an Edition, place it in a project, and use its files and workfl
> L163: TFW is tool-agnostic. Adapters translate the same repository-local workflow into a tool's project entry point:

## 星数曲线

```mermaid
xychart-beta
    title "saubakirov/trace-first-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `66fed21e2505` · [字段定义](../../DATASET.md)*
