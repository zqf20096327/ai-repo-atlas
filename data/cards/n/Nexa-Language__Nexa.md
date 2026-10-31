# Nexa-Language/Nexa

⭐ 34 · Python · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/Nexa-Language/Nexa) · [官网](https://www.nexa-lang.com/) · 组织维护 · 中文 README

**Agent 原生编程语言与运行时：人和模型共同编写 .nx 程序**

面向开发者的编程语言及配套运行时：源码以 .nx 合同描述目标、实现、证据与修订；编译器可在预算内让模型求解 open 实现，OCI 执行器运行候选并执行验收检查，运行时在证据有效、权限满足时接纳新版本。保留 2.4 兼容入口，支持原生 Chat Completions/Responses/Anthropic 协议、工具审批、SQLite 持久化、MCP 连接与 Wasmtime 执行。需 Python 3.10+，执行候选需 Docker；提供 Python API、CLI 与 67 个登记示例。许可证 AGPL-3.0-or-later。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Open Programs：程序持有目标、实现、证据与修订，运行时按证据与权限接纳版本
- 编译器 JSON-RPC 协议提供诊断、澄清与取消，协作演进
- 原生 Chat Completions / Responses / Anthropic 协议与 MCP stdio/HTTP 连接
- 候选在 OCI 容器内执行，含预算、超时、审批与 SQLite checkpoint

## 适用场景

- 用一种语言编写由人和模型共同维护的 agent 程序
- 让模型在验收条件与预算约束内求解 open 实现
- 通过审批流程执行长任务与工具调用

## 场景标签

`Agent 框架` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Agent 原生语言与可靠运行时，供人和模型共同编写 .nx 程序。
> L11: - **编译包含求解**：`implementation open` 留下带类型与验收条件的目标；模型在预算内提出实现，OCI 执行器运行候选和固定检查。
> L22: 需要 Python 3.10+。3.0 运行时支持 Linux/macOS，执行候选需要 Docker Engine 或 macOS 上的 Docker Desktop / Colima。在虚拟环境中安装 3.0.0 Releas

## 星数曲线

```mermaid
xychart-beta
    title "Nexa-Language/Nexa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9093adaf80aa` · [字段定义](../../DATASET.md)*
