# google/ax

⭐ 13,930 · Go · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/google/ax) · [官网](https://agentexecutor.io) · 组织维护

**集群级 agent 工作负载的声明式编排运行时**

AX 是一个声明式编排器，用于在集群上运行大规模自主 agent 工作负载，基于 Agent Substrate 提供沙箱执行。核心原语包括 Task（隔离沙箱运行不可信 agent 代码，含 CPU/内存限制）、Workspace（预置 Git 仓库、MCP 服务器与技能包）和 Model（配置平台所用 LLM 及凭据）。全部以 ax.io/v1alpha1 YAML 清单表达，CLI 采用 kubectl 风格命令，支持 suspend/resume 断点续跑与 ax ssh 进入运行中任务。依赖 Kubernetes 集群、Go、kubectl、ko 与容器镜像仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.5 天,年发版 7,22 位贡献者
- 涨星:近 1 天 **+188**(自 20261016 起算)
- 平台:— · 协议:MCP

## 能力要点

- Task/Workspace/Model 三原语的声明式 YAML 清单（ax.io/v1alpha1）
- ax suspend/ax resume 支持暂停后从原状态恢复
- kubectl 风格 CLI，跟随 kubectx 上下文切换集群
- 基于 Agent Substrate 的沙箱执行，带 CPU/内存限制

## 适用场景

- 在集群上批量运行需要隔离的自主 agent 任务
- 预配置 Git 仓库与 MCP 服务器让 agent 启动即就绪
- 运维人员通过 kubectl 式命令管理 agent 生命周期

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: AX is a high-throughput, declarative orchestrator to run billions of autonomous agent workloads in a cluster. It ru
> L30: Agents are a new kind of workload. They are neither stateless microservices nor run-to-completion batch jobs. They 
> L34: |Run untrusted agent code in an isolated sandbox with CPU/memory limits|**`Task`**|

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `2338f005ef12` · [字段定义](../../DATASET.md)*
