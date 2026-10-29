# Squid-Proxy-Lovers/ccp

⭐ 25 · Rust · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/Squid-Proxy-Lovers/ccp) · [官网](https://spl.team/ccp) · 组织维护

**为协作 AI agent 提供共享持久上下文的 Rust 客户端-服务器协议**

Rust 实现的客户端-服务器协调协议：服务器以 session→shelf→book→entry 层级存储文本与追加历史，多个 agent 通过 CLI 或 Python MCP 桥接创建、搜索和交换上下文，用于研究协作、并行评审与任务交接。客户端流量使用 mTLS 与个体证书，权限由服务器端执行；SQLite 与 journal 在重启后保留状态。支持 Droplet（JSON 包）在会话间导入导出上下文。安装经 shell 脚本安装预编译二进制，客户端可为 Claude、Cursor、Codex 配置 MCP。AGPL-3.0-or-later 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- session→shelf→book→entry 层级的共享持久上下文存储
- mTLS 个体证书认证与服务器端权限执行
- Python MCP 桥接供 agent 调用（CLI 保留破坏性操作）
- Droplet JSON 包在会话间导出/导入上下文

## 适用场景

- 多个 agent 协作研究时共享同一份持久上下文
- 并行评审与任务交接时交换中间结果
- 为 Claude/Cursor/Codex 等客户端接入统一的上下文服务器

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L2:  A Rust-based client-server coordination protocol for agentic systems.
> L19: context through the CLI or Python MCP bridge.
> L34: The client installer configures MCP for supported Claude, Cursor, and Codex hosts.

## 星数曲线

```mermaid
xychart-beta
    title "Squid-Proxy-Lovers/ccp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-29 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1dec2442ce3f` · [字段定义](../../DATASET.md)*
