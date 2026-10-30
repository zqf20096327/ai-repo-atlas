# KristjanPikhof/Pi-Agents-Team

⭐ 17 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/KristjanPikhof/Pi-Agents-Team) · [官网](https://npmjs.com/package/pi-agents-team) · 个人维护

**Pi 编辑器的多 agent 扩展：主会话编排后台 RPC 工作进程**

为 Pi coding agent 提供的扩展：主会话作为协调者，将任务委托给后台 RPC 工作进程执行。协调者不读取 worker 完整转录，仅接收摘要与 `<final_answer>` 块；提供实时仪表盘监控成本、token、活动流，并有 7 个斜杠命令（/team、/team-steer、/team-stop 等）。内置 7 种角色（explorer/fixer/reviewer 等），worker 会话持久化到 Pi 的 JSONL 会话文件，支持恢复。通过 `pi install npm:pi-agents-team` 安装，依赖 Pi >=1.1.0、Node >=22.19.0 与 Git；不支持 Git 包直接安装（dist/ 未入库）。

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

- 主会话作协调者，后台 RPC worker 执行任务，仅回传摘要与 final_answer
- 7 个内置角色与 /team 系列操作命令、实时仪表盘（Workers/Inspect/Console/Cost）
- worker 状态以紧凑记录持久化到 Pi 会话 JSONL，支持重载恢复
- 上下文感知的 worker 复用（<50% 复用、>=80% 拒绝复用）

## 适用场景

- 在 Pi 编码会话中并行委派探索、修复、评审等多文件任务
- 通过仪表盘监控多 agent 成本、token 与运行状态
- 向运行中的 worker 发送引导消息或终止任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Pi Agents Team
> L3: Pi main session acts as the coordinator, while background RPC workers execute the tasks. The orchestrator does not v
> L85: For delegated work, the orchestrator **picks a role** from the loaded config (seven built-ins by default: explorer,

## 星数曲线

```mermaid
xychart-beta
    title "KristjanPikhof/Pi-Agents-Team 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a899dee166c` · [字段定义](../../DATASET.md)*
