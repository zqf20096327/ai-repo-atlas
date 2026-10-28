# hraness/algal

⭐ 21 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/hraness/algal) · [官网](https://algal.computer) · 个人维护

**面向长期运行 agent 的编程语言：可审批暂停、断点续跑、离线重放**

ALGAL 是一种以数据形式表达 agent 程序的编程语言：程序为带类型的步骤/模型调用/工具图，宿主可检查、哈希并运行。程序可暂停等待人工审批，重启后跨机器恢复而不重复已完成工作；所有模型调用与工具结果被记录，可在离线、无凭据状态下重放验证。程序可通过候选生成、在声明的用例上评测、择优采纳的方式演化。提供 TypeScript 与 Rust 双运行时（共享程序与记录格式），原生 CLI 支持 macOS Apple silicon 与 Linux x86_64/arm64，当前为预发布版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 程序即数据：带类型步骤图，宿主可检查、哈希、运行
- 暂停等待审批、重启后跨机器恢复、避免重复已完成工作
- 记录全部模型调用与工具结果，支持离线无凭据重放验证
- 程序可通过评测择优自我演化；TypeScript 与 Rust 运行时共享格式可互续

## 适用场景

- 构建需人工审批且要长期存活的 agent 流程
- 为 agent 执行历史生成可离线验证的便携证据文件
- 跨 TypeScript/Rust 运行时保存并恢复 agent 运行状态

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 🌱 ALGAL is a programming language for agents that run for weeks. A program is
> L13: ALGAL is a programming language for agents that run for weeks. An ALGAL program
> L14: is data: a typed graph of steps, model calls, and tools that a host can inspect,

## 星数曲线

```mermaid
xychart-beta
    title "hraness/algal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4def355726a6` · [字段定义](../../DATASET.md)*
