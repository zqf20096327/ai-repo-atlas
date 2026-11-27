# marcusquinn/aidevops

⭐ 473 · Shell · MIT · 推送 2026-11-26 · [GitHub](https://github.com/marcusquinn/aidevops) · [官网](https://www.aidevops.sh) · 个人维护

**OpenCode 的 AI DevOps 插件框架：从意图到验证交付的自动化**

基于 OpenCode 的插件与 AI DevOps 框架，提供 17 个主 agent、2,250+ 子 agent、2,210+ 辅助脚本与 111 条 slash 命令，覆盖软件、基础设施、业务、营销、内容、研究与创意生产等场景。机制上按需加载上下文、模型路由分 simple/standard/thinking 三档、隔离工作区、对高风险操作设门控、保留证据并将经验沉淀为知识；Pulse 调度器每 2 分钟派发 headless worker，实现 24/7 自主运行。支持 Tabby 终端与多 provider 账号池轮换。

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

- 17 个主 agent、2,250+ 子 agent、111 条 slash 命令的完整 DevOps 体系
- Pulse 每 2 分钟调度 headless worker，标注 auto-dispatch 的 issue 自动认领
- 提供商中立的模型路由（simple/standard/thinking 三档）与多账号速率轮换
- 秘密管理、提示注入防护、源访问审批与审计轨迹等安全门控

## 适用场景

- 通过自然语言发起一次对话，让 agent 自主完成从实现到 PR 验证的交付
- 让 Pulse worker 持续无人值守地处理仓库中被标记的 issue
- 为团队沉淀任务、计划、决策与证据等仓库级知识
- 统一管理多个模型 provider 账号并在限速时自动轮换

## 场景标签

`编码 Agent` `多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L5: **aidevops.sh** is an OpenCode
> L167: - **Recommended runtime:** OpenCode; Claude Code and Codex CLI are supported interactive runtimes
> L170: - **Routing:** provider-neutral `simple`, `standard`, and `thinking` workload tiers

## 星数曲线

```mermaid
xychart-beta
    title "marcusquinn/aidevops 星数(近 20 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-28", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-27"]
    y-axis "stars" 416 --> 478
    line [421, 422, 423, 425, 434, 435, 421, 441, 445, 451, 452, 454, 455, 456, 467, 468, 469, 470, 471, 473]
```

2026-10-25 421 → 2026-11-27 473（+52）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `491b4a8799c6` · [字段定义](../../DATASET.md)*
