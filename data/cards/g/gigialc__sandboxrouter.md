# gigialc/sandboxrouter

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/gigialc/sandboxrouter) · [官网](https://www.sandboxrouter.ai) · 个人维护

**为 AI agent 统一接入 30+ 代码沙箱供应商的路由器**

一个开源路由层，为 AI agent 提供运行模型生成代码的一次性沙箱：用同一套 API（create、流式 exec、文件、清理）接入 30+ 个沙箱供应商及本地 Docker，按价格、启动速度或能力选择供应商，并在供应商宕机或限流时自动回退到下一个。路由基于自测的真实账单价与启动计时，提供 maxHourlyUsd 价格上限与 quote() 报价；本地账本记录已启动沙箱，sandboxrouter gc 可清理崩溃脚本遗留。提供 TypeScript、Python、HTTP API 与 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套 API 接入 30+ 沙箱供应商及本地 Docker
- 按实测价格/速度路由，宕机或限流自动回退
- sbx.native 保留供应商自有 SDK 功能（如快照、卷）
- 提供 TypeScript/Python/HTTP/CLI 及本地沙箱清理工具

## 适用场景

- 为 AI agent 选择最低价或最快的代码执行沙箱
- 在多个沙箱供应商之间做故障回退与限流兜底
- 用本地 Docker 免费跑 agent 代码执行
- 清理崩溃脚本遗留的沙箱实例

## 场景标签

 · 领域:AI agent 基础设施/沙箱编排

## 证据(README 行号)

> L3: **One API for every sandbox.** A free, open-source router for the places an AI agent can run code: Agent37, Alibaba 
> L29: AI agents need a disposable computer to run code a model wrote: install packages, run tests, do an RL rollout. Doze
> L37: - **TypeScript, Python, HTTP and a CLI.** Plus desktops and phones for computer-use models.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9b45487e7e82` · [字段定义](../../DATASET.md)*
