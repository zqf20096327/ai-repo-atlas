# EpicStaff/EpicStaff

⭐ 513 · Python · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/EpicStaff/EpicStaff) · [官网](https://www.epicstaff.com/) · 组织维护

**给运营团队自托管构建 AI Agent 流程的可视化编排平台**

Source-available 的自托管平台，用于构建 AI agent 流程：拖拽式可视化编辑器运行在 Django 后端之上，节点可注入自定义 Python 逻辑，通过 MCP 和 Python 连接内部系统。内置基于 Redis/PostgreSQL 的跨流程持久化 agent 记忆与用户/组织变量状态管理。平台提供 session ledger、沙箱执行、按 agent 的权限控制与审计追踪，使运营团队能查看、编辑和复核 agent 决策。安装方式为 git clone 加 docker compose 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽式可视化编辑器，节点内可注入自定义 Python 逻辑
- 基于 Redis/PostgreSQL 的跨会话持久化 agent 记忆
- 通过 MCP 与 Python 连接内部系统
- 发布镜像经 Sigstore cosign 无钥签名并附带 SPDX SBOM

## 适用场景

- 让运营团队无需工程介入即可查看和修改 agent 流程
- 自托管部署中为 agent 执行提供权限控制与审计追踪
- 以低代码方式构建多 agent 编排流程

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L18:  EpicStaff is a platform for building AI agent flows that operations teams own.
> L20: The deployment model is self-hosted and source-available. Engineers connect EpicStaff to your internal systems thro
> L43: * **Django Multi-Agent Backend:** Powered by Django for robust, low-latency, and production-ready Pythonic agent or

## 星数曲线

```mermaid
xychart-beta
    title "EpicStaff/EpicStaff 星数(近 12 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-28", "2026-11-06", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-25"]
    y-axis "stars" 343 --> 532
    line [359, 358, 359, 358, 360, 517, 516, 517, 515, 516, 515, 513]
```

2026-10-23 359 → 2026-11-25 513（+154）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `c3ceb7a59187` · [字段定义](../../DATASET.md)*
