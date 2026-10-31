# earayu/treadstone

⭐ 34 · Python · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/earayu/treadstone) · [官网](https://treadstone-ai.dev/) · 个人维护 · 中文 README

**面向 agent 的沙箱基础设施：在 Kubernetes 上运行隔离的全能运行时**

开源、可自托管、基于 Kubernetes 的 agent 沙箱平台。每个沙箱为一体化运行时，包含代码执行、shell、文件系统、浏览器自动化、MCP 访问与长驻进程/可选持久存储。提供两种用法：把 agent 放进沙箱运行，或将沙箱作为 agent 按需调用的工具。控制面（CLI/REST API/Python SDK）管理账号、认证、生命周期、用量与浏览器接管；数据面经 proxy/MCP/web URL 暴露沙箱内服务。内置 5 档 AIO 模板，支持冷快照与多租户边界。

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

- 一体化沙箱运行时：shell/文件/浏览器/MCP/HTTP/长驻进程
- 控制面（CLI、REST API、Python SDK）+ 数据面双平面架构
- 浏览器会话可交接给人工审查或接管
- 五档内置模板（0.25–4 vCPU），支持持久存储与冷快照

## 适用场景

- 让 agent 在隔离环境中长期执行需要文件、浏览器和状态的任务
- 把沙箱作为工具供外部 agent 经 MCP/REST 按需创建和驱动
- 自托管带用量计量与多租户边界的沙箱平台

## 场景标签

 · 领域:AI 基础设施/沙箱运行时

## 证据(README 行号)

> L6: **Treadstone is an agent-native sandbox platform for longer-running AI work.** You can run agents inside isolated sa
> L19: Treadstone treats the sandbox itself as a first-class primitive. The platform gives you the lifecycle, auth, routin
> L173: - a Kubernetes-backed sandbox orchestration layer built around the `agent-sandbox` controller

## 星数曲线

```mermaid
xychart-beta
    title "earayu/treadstone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `09ab8246a2d1` · [字段定义](../../DATASET.md)*
