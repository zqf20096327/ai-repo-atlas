# staticroostermedia-arch/engram

⭐ 19 · Rust · AGPL-3.0 · 推送 2026-08-07 · [GitHub](https://github.com/staticroostermedia-arch/engram) · [官网](https://glama.ai/mcp/servers/staticroostermedia-arch/engram) · 个人维护

**给 AI agent 的本地持久几何记忆后端，经 MCP 接入**

Rust 编写的本地记忆基座：以 256KB 全息块（.leg3，8192D q/p、BLAKE3 Merkle、CRS 完整性校验）存储结构化记忆，通过 MCP 协议（101 个 mcp_engram_* 工具 + 4 个语言计算工具，精简路径默认 8 个）供任意 LLM agent 作为后端使用。提供 session_start 唤醒恢复、session_end 会话交接、harness 注入、thought tile 与 tensor 双写、NVMe/GPU 加速召回及只读 LEG Browser 本地查看器。明确声明非向量数据库。当前版本 0.7.0-beta.12，需从源码 cargo 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP 接入任意 LLM（Grok/Claude/Llama），注册 105 个工具、精简路径 8 个
- 256KB 全息块 + BLAKE3 Merkle + CRS ≥ 0.74 完整性校验的持久记忆
- session_start/end 唤醒—交接闭环与 harness 注入，跨冷关机保持连续性
- NVMe/cuFile GPU 加速召回与只读 LEG Browser 本地查看器

## 适用场景

- 长时运行 agent 系统需要跨会话连贯记忆
- 游戏中的持久 LLM 角色与个性化 AI 伴侣
- 编辑代码前获取文件级记忆上下文（context_for_edit）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Engram is a local, hardware-native memory substrate that gives AI agents coherent, long-term memory with structure-
> L18: It is designed as a drop-in backend for any LLM (Grok, Claude, Llama, etc.) via the Model Context Protocol (MCP) an
> L118: Fixed **256KB HolographicBlocks** (.leg3): 8192D phase (q), momentum (p), CRS lawfulness, BLAKE3 Merkle, spatial A

## 星数曲线

```mermaid
xychart-beta
    title "staticroostermedia-arch/engram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b5bca370ffe3` · [字段定义](../../DATASET.md)*
