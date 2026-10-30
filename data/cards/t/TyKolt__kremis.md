# TyKolt/kremis

⭐ 16 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/TyKolt/kremis) · [官网](https://kremis.mintlify.app) · 个人维护

**Rust 确定性知识图谱引擎与 MCP 服务器，供 AI 检索可溯源记忆**

用纯 Rust 编写的本地单二进制知识图谱引擎，提供 CLI、HTTP API 与 MCP 三种接口，供 AI 助手接入作为可验证记忆层：记录、关联、检索真实摄入的信号，缺失数据返回显式 not found，不生成无据内容。核心机制包括无浮点与无随机性的确定性输出、redb 嵌入式 ACID 事务、全图 BLAKE3 哈希校验、确定性二进制快照导出（KREX）与可复现的查询证书（KVQC，含事实存在与缺失的证明）。零预置知识，初始为空图。自声明 Alpha 阶段，v1.0 前可能有破坏性变更；CLI 与 HTTP 服务器不能同时运行（redb 独占锁）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI / HTTP API / MCP 三接口共享同一确定性图引擎
- BLAKE3 全图状态哈希与 KREX 确定性快照导出
- POST /certify 返回可复现的可验证查询证书（含缺失证明）
- redb 嵌入式数据库提供 ACID 崩溃安全事务

## 适用场景

- 给 Claude、Cursor 等 MCP 兼容助手加可溯源的长期记忆
- 摄入自有数据后对 LLM 生成的声明做事实核对
- 合规场景下导出图谱快照并证明某时点数据存在与否

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A deterministic knowledge graph MCP server. Local, single binary, no LLM in the loop.
> L37: - **CLI + HTTP API + MCP bridge** — Three interfaces to the same engine: terminal, REST, and AI assistants
> L198: |**apps/kremis-mcp**|MCP server bridge for AI assistants (rmcp, stdio)|

## 星数曲线

```mermaid
xychart-beta
    title "TyKolt/kremis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f39a9667d8e0` · [字段定义](../../DATASET.md)*
