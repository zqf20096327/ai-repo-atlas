# ChukarAI/Vibe_Assembly

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/ChukarAI/Vibe_Assembly) · 组织维护

**多智能体编码工作台：小 agent 分工维护大项目不超上下文**

纯 Rust 实现的多智能体编码 harness，让多个聚焦角色（Boss/Code/Debug/Judge/Chat/Hermes）通过 `.ai/` 目录下的受控 markdown 状态通信，避免单一聊天上下文耗尽。每次编辑经确定性、哈希锚定的执行 harness 验证，提供 CLI、TUI 与 GPUI 桌面仪表盘。运行需要 Rust 稳定版工具链与本地 OpenAI 兼容 router，离线 mock 运行无需 router；不带浏览器运行时与 Node/npm 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六种 planner 角色经 `.ai/` 契约协作，任务按小 ticket 设计
- 哈希锚定补丁与确定性 judge 门控、会话 DAG 支持回滚
- 提供 CLI、TUI 与 GPUI 桌面（Liquid Glass / Paper & Ink）三种界面
- 支持 Rust/C/Python/TS/Go 语言视角与验证命令配置

## 适用场景

- 在单个聊天上下文放不下的大型项目中继续编码
- 让 agent 编辑经哈希校验与验证门控后落盘
- 本地 router 环境下零成本运行编码 agent

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L11: Vibe Assembly lets small, focused agents build and maintain large software
> L14: hash-anchored execution harness.
> L71: - A local OpenAI-compatible router for live runs. Offline mock runs need no router.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `57e340e2dfa6` · [字段定义](../../DATASET.md)*
