# 503496348-ops/barren-order

⭐ 19 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/503496348-ops/barren-order) · [官网](https://503496348-ops.github.io/atomcollide-product-matrix/) · 组织维护 · 中文 README

**飞书群内多 Bot 互相@协作的多 Agent 编排框架**

面向飞书（Lark）群聊场景的多 Agent 协作框架：通过 @mention 实现 Bot 间任务分发，采用主持者-执行者模式，配备 DAG 工作流引擎（条件分支/并行/重试）、四级作用域共享记忆（GLOBAL/AGENT/SESSION/WORKFLOW，TTL+快照恢复）、消息去重、manager-only 入口、审批硬暂停、熔断与健康验证等运行时机制。另含零 LLM 的团队桥接规划器与会前情报任务流脚本。以 pip 包与 install.sh 脚本形式交付，附 doctor/smoke/收敛门禁与测试验证。

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

- 飞书 @mention 的 Bot-to-Bot 通信与主持者-执行者分工
- DAG 工作流引擎：条件分支、并行执行、重试与降级
- 四级作用域共享记忆，TTL 过期与快照恢复
- manager-only 入口、消息去重、审批硬暂停、PID/心跳多层健康验证

## 适用场景

- 让多个飞书群 Bot 分工完成采集+分析、审查+部署等流水线
- 为常驻 Agent 团队做任务分发、回报与运行时拦截
- 编排会前调研等多线并行的 manager-worker 任务流

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L38: 多Bot协作解决方案 — 让两个或多个Hermes Bot在飞书群内通过互相@实现协作。
> L50: 荒原序列是一个多Agent协作框架，支持：

## 星数曲线

```mermaid
xychart-beta
    title "503496348-ops/barren-order 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5490cebe4297` · [字段定义](../../DATASET.md)*
