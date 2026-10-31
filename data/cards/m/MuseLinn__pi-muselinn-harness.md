# MuseLinn/pi-muselinn-harness

⭐ 17 · TypeScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/MuseLinn/pi-muselinn-harness) · [官网](https://muselinn.github.io/pi-muselinn-harness/) · 个人维护

**为 Pi 编码代理补齐子代理/计划/待办等编排功能的扩展包**

面向 Pi coding agent 的编排扩展包（pi package/extension），以 Kimi Code 的子系统行为为参照，补充 Pi 未内置的能力：并行子代理 Swarm（真实 max_concurrency 并发、后台运行）、计划模式（先探索审批后执行）、目标生命周期与三重预算、18 级权限链、后台任务与 cron、[[hooks]] 事件引擎、技能扫描与 TUI 编辑器界面。兼容 pi 0.81.x–0.83.x，macOS/Ubuntu/Windows CI 测试，单包安装、无需配套扩展。

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

- Swarm 并行子代理：并发上限、后台运行、/steer 运行时注入、转写记录
- 计划模式与 18 级权限链（auto/yolo/manual）、破坏性命令与 .env 守卫
- Goal 生命周期与 token/turn/wall-clock 三重预算、完成条件校验
- 后台任务 + cron 调度、[[hooks]] 事件引擎（16 事件、可阻断）

## 适用场景

- 让 Pi 编码代理并行派出子代理执行拆分任务
- 编码前进入计划模式做只读探索并审批后再执行
- 为长任务设置目标与预算，跟踪待办与定时触发

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Kimi Code-style agent orchestration for the Pi coding agent** — Swarm · Goal · Plan · Permission · Ask · Task · Cr
> L7: Compatible with pi 0.81.x–0.83.x on macOS, Ubuntu, and Windows · Node 24/26 · CI-tested on macOS + Ubuntu + Windows.
> L33: pi install npm:pi-muselinn-harness     # or: pi install git:github.com/MuseLinn/pi-muselinn-harness

## 星数曲线

```mermaid
xychart-beta
    title "MuseLinn/pi-muselinn-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `548f6311da0e` · [字段定义](../../DATASET.md)*
