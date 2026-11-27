# open-covenant/covenant

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/open-covenant/covenant) · [官网](https://opencovenant.org) · 组织维护

**为长期自主编程 agent 提供能力签权、审计与记忆的 Rust 运行层**

位于 agent 应用与宿主操作系统之间的 Rust 守护进程层，通过 CLI/IPC/HTTP/MCP/A2A 接口以八个原语（意图、运行时、记忆、身份、权限、通信、组合器、结算）管理 agent 的状态、权限与问责。核心机制包括 ed25519 签名能力（授予/过期/撤销/分发时作用域强制）、SQLite 三层记忆（工作/情景/长期）、仅追加哈希链审计日志与 commit 级溯源信封，并集成 Solana/Base 等链上结算与 x402 付费。沙箱化执行与多节点组网仍在路线图中；提供源码构建、Web 控制台、TUI、TypeScript SDK 及在线沙箱演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 签名能力的完整生命周期管理与分发时作用域强制
- 仅追加 JSONL 审计日志与本地哈希链完整性验证
- SQLite 三层项目记忆，带漂移报告与修复
- MCP 适配器、A2A 邮箱原语与 x402（HTTP 402）付费集成

## 适用场景

- 为长期运行的自主编程 agent 提供权限边界与审计追溯
- 在本地守护进程上编排多 agent 的意图分发与预算控制
- 为 agent 动作生成 commit 级溯源与完整性证明
- 构建需要链上结算与 x402 计费的 agent 服务

## 场景标签

`多智能体` `Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Covenant sits below agent applications and above the host operating system. It owns the state, authority, and accou
> L79: - **Execution:** daemon-mediated runtime dispatch with budget enforcement and sandbox-aware agent manifests.
> L105: - Rust daemon and CLI for local agent orchestration.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `32afad10bede` · [字段定义](../../DATASET.md)*
