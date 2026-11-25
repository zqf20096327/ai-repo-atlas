# mas-bandwidth/nova-tools

⭐ 22 · Go · MIT · 推送 2026-11-23 · [GitHub](https://github.com/mas-bandwidth/nova-tools) · [官网](https://github.com/mas-bandwidth/nova-tools/blob/main/docs/README.md) · 个人维护

**跨模型 AI 团队共享工具与机器机群的工具包**

nova-tools 是面向多个模型上运行的 AI agent 的工具包，提供能力包括：跨模型/harness 的 AI 之间消息通信、基于 Tailscale 连接机群、在机群上运行 GitHub CI runner、自动部署密钥到机群、共享机器的协调、在沙箱中运行不可信任务、跨会话保留记忆。各工具可独立使用，notes 和 reservations 无需服务器，messaging 需要 Redis。作者为 Glenn Fiedler 与 Rowan Claude。README 未给出具体安装命令，指引用 AI 阅读 docs。

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

- 跨模型与 harness 的 AI 间通信
- 基于 Tailscale 的机器机群管理与共享
- 不可信任务沙箱执行与跨会话记忆

## 适用场景

- 让不同模型上的多个 AI agent 协同通信
- 搭建并管理分布式机器机群运行 CI 与密钥部署
- 在隔离沙箱中运行不可信工作负载

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: One toolkit for a team of AIs on different models.
> L9: * Talk to each other across models and harnesses

## 星数曲线

```mermaid
xychart-beta
    title "mas-bandwidth/nova-tools 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-25"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-11-08 21 → 2026-11-25 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `404b8188457e` · [字段定义](../../DATASET.md)*
