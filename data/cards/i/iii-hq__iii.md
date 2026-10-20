# iii-hq/iii

⭐ 18,847 · Rust · 推送 2026-10-18 · [GitHub](https://github.com/iii-hq/iii) · [官网](https://iii.dev) · 组织维护

**为后端开发者提供统一实时组合、扩展与观测服务的引擎**

iii 是一个以 Rust 引擎为核心的后端服务运行时，将队列、cron、HTTP、状态、可观测性、agent 与沙箱统一到一个实时系统面。一切能力映射为三个原语：Worker（注册到引擎的进程）、Trigger（触发函数运行的事件）与 Function（带稳定标识的工作单元）。各 worker 加入实时目录后互相可发现、可调用；agent 使用与开发者相同的目录与函数调用接口，可在运行时添加 worker。提供 Node.js/Python/Rust/Go SDK、开发者 Console 与可安装到第三方 harness 的 agent skills。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.8 天,年发版 100,54 位贡献者
- 涨星:近 1 天 **+3**(自 20261016 起算)
- 安装:npm 包 `iii-sdk` 月下载 153,107

## 能力要点

- Worker/Trigger/Function 三原语统一队列、cron、HTTP、状态与可观测性
- 实时目录：worker 注册后其他 worker 可立即发现并调用
- agent 与开发者共用同一函数目录，可运行时添加 worker 并追踪
- 提供 Node.js、Python、Rust、Go 四语言 SDK 与开发者 Console

## 适用场景

- 用一份 worker-compose.yaml 统一声明项目中的队列、定时任务与服务
- 让 agent 在运行中发现并调用后端已有函数能力
- 通过 Console 检查 workers、traces、日志与实时状态
- 为第三方 agent harness 安装 iii 的技能包

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L47: That is the agent story too: when a task needs a capability the system does not have, an agent can
> L87: Platform teams publish workers. Application teams register functions and declare triggers. Agents
> L55: **Workers** are processes that register with the iii engine and then register triggers and

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `05bf06d64888` · [字段定义](../../DATASET.md)*
