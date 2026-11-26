# google/ax

⭐ 14,896 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/google/ax) · [官网](https://agentexecutor.io) · 组织维护

**面向开发者的声明式 agent 工作负载集群编排运行时**

AX 是 Google 开源的 agentic 编排运行时，以 Kubernetes 风格的 YAML 清单（ax.io/v1alpha1）声明 agent 任务，在 Agent Substrate 之上提供沙箱化执行，支持单集群运行数百万个 agent 工作负载。核心原语包括 Task（隔离沙箱与资源限制）、Workspace（预配置 Git 仓库、MCP 服务器与技能包）、Model 与 Gateway（凭据注入与网络策略）；提供 apply/resume/suspend/ssh/describe 等 kubectl 形状的 CLI 命令及本地 Web UI（ax-studio）。README 明确警告项目处于重度开发阶段，稳定版前可能出现重大破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.5 天,年发版 7,22 位贡献者
- 涨星:近 1 天 **+188**(自 20261016 起算)
- 安装:github 包 `release-assets` 月下载无数据
- 平台:— · 协议:MCP

## 能力要点

- 声明式 YAML 清单（Task/Workspace/Model/Gateway）管理 agent 工作负载
- 沙箱化隔离执行，含 CPU/内存限制与主机访问策略
- kubectl 形状 CLI，支持 suspend/resume 断点续跑与 ax ssh 调试
- 本地 Kind 集群快速启动，兼容 kubectx 切换集群

## 适用场景

- 在集群中批量运行需要隔离与状态管理的 agent 任务
- 为 untrusted agent 代码提供资源受限沙箱并控制其网络出口
- 本地 Kind 起步后无缝迁移到远程 GKE 集群运行 agent
- 通过 web UI 启动、观察并 shell 进入运行中的 agent 任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: AX is a highly efficient, declarative orchestrator to run millions of autonomous agent workloads in a cluster. It r
> L31: Agents are a new kind of workload. They are neither stateless microservices nor run-to-completion batch jobs. They 
> L150: AX is aiming to grow into an agentic platform that covers session management, memory, multi-task coordination, inp

## 星数曲线

```mermaid
xychart-beta
    title "google/ax 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 13956 --> 14981
    line [14041, 14054, 14059, 14076, 14103, 14120, 14277, 14343, 14378, 14402, 14431, 14059, 14568, 14609, 14625, 14638, 14697, 14716, 14745, 14764, 14791, 14809, 14823, 14837, 14850, 14863, 14896]
```

2026-10-23 14,041 → 2026-11-26 14,896（+855）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `717ef0534c2e` · [字段定义](../../DATASET.md)*
