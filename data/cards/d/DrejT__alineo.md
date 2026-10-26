# DrejT/alineo

⭐ 39 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/DrejT/alineo) · [官网](https://alineo.tech) · 个人维护

**沙箱化 AI agent 集群的控制平面：运行/分叉/暂停/审计多个 agent**

面向多 agent 编排的基础设施：以 TypeScript SDK、daemon（alineod）和 CLI 组成，让每个 agent 在独立的 OpenSandbox 容器中运行。支持从运行中的沙箱分叉子 agent（继承磁盘上的 checkout 与已安装包）、中途转向或暂停 agent、通过 ledger 回放使 daemon 崩溃后恢复集群、对高危工具调用与网络出口设置人工审批，并将所有执行与工具调用写入 SQLite/Postgres 持久账本。给需要在本地运行并管控多个编码 agent 的开发者使用；Apache 2.0，本地运行无需账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从运行中的沙箱分叉子 agent，继承已有环境
- 中途转向/暂停/恢复 agent，无需重启
- daemon 崩溃后通过 ledger 回放恢复集群
- 高危操作人工审批与 SQLite/Postgres 审计账本

## 适用场景

- 编排多个沙箱化编码 agent 协作完成代码审查等任务
- 对 agent 的工具调用与网络访问做审批和审计
- 需要可分叉、可恢复的长期 agent 集群运维

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A control plane for swarms of sandboxed agents.**
> L73: Agent products give you one agent. Sandbox providers give you a box. alineo is the layer between them: it runs many

## 星数曲线

```mermaid
xychart-beta
    title "DrejT/alineo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7e8252cc583b` · [字段定义](../../DATASET.md)*
