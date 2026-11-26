# noxred-research/browserx

⭐ 3 · Rust · AGPL-3.0 · 推送 2026-11-22 · [GitHub](https://github.com/noxred-research/browserx) · [官网](https://browserx.dev) · 组织维护

**面向授权安全研究的 Rust 浏览器池与会话托管服务**

单一 Rust 服务进程管理本机 Chromium 进程池，以租约形式向自动化客户端交付会话：租约带 TTL、fencing 代数与控制令牌，状态存于 SQLite（多 worker 可用 PostgreSQL/MariaDB）。支持三种持久化契约（ephemeral/snapshot/profile）、崩溃恢复与一次调用的会话交接，并在每次接入时报告 outcome。内置 MCP 服务器让 AI agent 在操作员设定的能力门控内监视与驱动浏览器池；租约、恢复与出口策略为确定性代码，无模型配置时全部功能可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 租约式会话管理：TTL、fencing 代数、每所有者配额与准入队列
- 三种持久化模式（ephemeral/加密 snapshot/profile）并在每次 attach 报告 outcome
- 内置 MCP 服务器，capability 门控工具、哈希链审计日志与人工审批动作门
- 每会话回环转发器支持直连或上游 http/socks5 代理，凭据不进入浏览器参数与日志

## 适用场景

- 授权安全测试中为自动化客户端分配、恢复和交接浏览器会话
- 让 MCP 客户端在签名规则范围内监视与操作浏览器池
- 多 worker 场景下用 PostgreSQL/MariaDB 共享租约注册表

## 场景标签

`网络安全` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: One Rust service supervises local Chromium processes, leases them to automation clients as sessions, keeps the state
> L64: - **The data path is deterministic.** Leases, fencing, recovery, egress policy and the host-protection relay policy


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `443dbe2aa6b8` · [字段定义](../../DATASET.md)*
