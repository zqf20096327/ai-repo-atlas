# bon5co/bermuda

⭐ 14 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/bon5co/bermuda) · [官网](https://github.com/bon5co/bermuda#readme) · 个人维护

**herdr 上的 agent 编排插件：流程、定时任务、资源租约与共享记录**

Bermuda 是运行在 herdr 上的调度与编排层，非 agent 本体。提供 flows（每步独立 agent 进程、失败停止并可 resume、overwatch 决策 retry/goto/park/abort）、jobs（cron 定时运行 prompt 或 flow）、threads（append-only 共享记录）与 claims（TTL 资源租约），另有 A.LOG 更新卡片、IMPROVE 经验卡、forum 检索与本地 memory。安装需 Go 工具链，支持 Linux/macOS/Windows，状态存于 ~/.bermuda。

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

- flows 将步骤移出 agent，每步独立进程且失败可 resume
- overwatch 读取整个 run 决策 retry/goto/park/abort，skip 默认不允许
- jobs 以 cron 定时运行，等待人工时 parked 而非丢弃
- claims 以 TTL 租约独占资源并告知持有者
- A.LOG/IMPROVE/forum 以 Markdown 卡片记录更新、经验与可检索答案

## 适用场景

- 多步骤任务强制按序执行，防止 agent 跳步
- 定时无人值守运行 agent 任务并在需人工时挂起
- 多 agent 共享机器时对浏览器等资源做排他租约
- 沉淀 agent 的发现与解法供后续任务检索

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L75: Bermuda is not an agent. It is the layer beneath whatever agent you already run
> L76: on herdr: a scheduler, a sequencer, and a shared record. A

## 星数曲线

```mermaid
xychart-beta
    title "bon5co/bermuda 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `cca823a7fa9f` · [字段定义](../../DATASET.md)*
