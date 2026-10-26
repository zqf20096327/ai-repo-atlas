# jxoesneon/mempalace-rs

⭐ 38 · HTML · MIT · 推送 2026-10-11 · [GitHub](https://github.com/jxoesneon/mempalace-rs) · [官网](https://crates.io/crates/mempalace-rs) · 个人维护

**Rust 编写的本地离线 AI 记忆系统，为 agent 提供长期记忆**

面向 AI agent 的本地优先记忆系统：从本地代码库与对话中挖掘内容，构建 SQLite + usearch 向量存储的四层记忆栈（L0-L3），提供 AAAK 压缩（约 30x token 缩减）、带时间有效期的知识图谱、agent 日记与语义搜索。通过 20 个 MCP 工具（stdio）接入 Claude Code、Cursor、Windsurf 等 15+ 客户端，另提供 CLI（init/mine/search 等）。需 Rust 1.70+ 从源码构建，Crates.io 安装标注即将推出；支持 Termux/ARM64（需脚本安装 onnxruntime）。为 Python 版 mempalace 的功能移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- L0-L3 四层记忆栈，SQLite + usearch 向量存储，零网络嵌入式
- AAAK 压缩实现约 30x token 缩减
- 20 个 MCP 工具（mempalace_ 前缀）供 agent 交互
- 带 valid_from/valid_to 的时间性知识图谱与 agent 日记

## 适用场景

- 给 Claude Code/Cursor 等 agent 客户端挂载长期记忆后端
- 挖掘本地代码库与会话记录并做语义搜索
- 以 MCP server 形式运行，为 agent 提供知识图谱与日记工具

## 场景标签

`Agent 记忆` `知识图谱` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L11: A high-performance, local, offline-first memory system built in Rust. Gives agents long-term retention by mining lo
> L18: - **20 MCP Tools**: Full Model Context Protocol integration for agent interaction
> L159: The project exposes 20 tools via Model Context Protocol (all prefixed with `mempalace_`):

## 星数曲线

```mermaid
xychart-beta
    title "jxoesneon/mempalace-rs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-26 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5321a8c6f359` · [字段定义](../../DATASET.md)*
