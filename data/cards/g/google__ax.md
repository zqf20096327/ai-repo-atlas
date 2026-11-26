# google/ax

⭐ 14,896 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/google/ax) · [官网](https://agentexecutor.io) · 组织维护

**Google 开源的 agent 编排运行时，集群级运行海量自治任务**

AX 是 Google 开源的声明式 agent 编排运行时，用于在集群上运行大规模自治 agent 工作负载。它以 ax.io/v1alpha1 YAML 清单定义 Task、Workspace、Model、Gateway 四种原语，提供沙箱隔离、资源限制、Git 仓库与 MCP 服务器预接线、凭证注入、挂起/恢复与 ssh 调试；CLI 采用 kubectl 风格，附带本地 Web UI（ax-studio）与端到端 tour 脚本。运行依赖 Agent Substrate 底层，可本地 Kind 集群启动或部署到 Kubernetes 1.37+ 集群。项目处于早期开发，可能引入破坏性变更。

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

- Task/Workspace/Model/Gateway 四原语以 YAML 清单声明
- 沙箱隔离执行、挂起/恢复与快照续跑、ax ssh 调试
- kubectl 风格 CLI 与本地 Web UI（ax-studio）
- 基于 Agent Substrate，可本地 Kind 或远程 Kubernetes 集群运行

## 适用场景

- 在集群中批量调度并隔离运行不可信的 agent 代码
- 为 agent 预配置代码仓库、MCP 服务器与工具凭证
- 挂起空闲 agent 并从原状态恢复继续执行
- 通过 Web UI 或 CLI 观测、调试运行中的 agent 任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Declare an agentic task with workspaces and model specifications. AX sandboxes it, wires up its workspace, and hel
> L11: AX is a highly efficient, declarative orchestrator to run millions of autonomous agent workloads in a cluster. It r
> L162: AX is aiming to grow into an agentic platform that covers session management, memory, multi-task coordination, inp

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `07ab4f656db6` · [字段定义](../../DATASET.md)*
