# nexi-lab/nexus

⭐ 194 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/nexi-lab/nexus) · [官网](https://nexi-lab.github.io/nexus/) · 组织维护

**面向多智能体系统的分布式 VFS 与共享上下文基础设施**

Nexus 是为多智能体系统提供共享存储、权限、消息与协调的分布式虚拟文件系统（VFS）基础设施层，定位在 LangGraph/CrewAI 等 agent 框架之下。内核为纯 Rust 的约 5MB 静态二进制，提供 14 个系统调用；通过 hook 层透明接管 Node.js fs 与 Python open 的文件 I/O。功能包括 ReBAC 权限、语义搜索（BM25S + pgvector）、持久化记忆、MCP 工具挂载、Docker 沙箱、Raft 联邦与加密存储等 30+ 运行时服务。支持 pip 安装、Docker 镜像（GHCR）与嵌入式单进程模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 内核提供 14 个系统调用的分布式 VFS
- hook 层透明接管 agent 的文件 I/O，无需改代码
- ReBAC 权限、区域隔离与 AES-256-GCM 加密存储
- 与 Claude Agent SDK、LangGraph、CrewAI 等框架的集成示例

## 适用场景

- 让多个 agent 在节点间共享存储与协作
- 为 agent 队伍设置权限边界与执行沙箱
- 跨数据中心联邦部署 agent 基础设施

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: ### Distributed VFS for multi-agent systems
> L21: Agent harnesses (LangGraph, CrewAI, AutoGen) decide **what** agents do — tool calls, chains, memory loops. Nexus is

## 星数曲线

```mermaid
xychart-beta
    title "nexi-lab/nexus 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 192 --> 195
    line [193, 194, 194]
```

2026-10-18 193 → 2026-10-24 194（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b753b3d72559` · [字段定义](../../DATASET.md)*
