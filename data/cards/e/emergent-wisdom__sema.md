# emergent-wisdom/sema

⭐ 14 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/emergent-wisdom/sema) · 组织维护

**面向 AI agent 的内容寻址语义词汇表与 MCP 服务器**

通过 hash(canonical(definition)) 为协调协议、推理模式等概念生成内容寻址标识，供多 agent 系统作为可验证的语义引用。以 MCP 服务器形式接入 Claude Code、Cursor 等任意 MCP 客户端，提供 sema_search、sema_handshake、sema_mint 等 16 个工具；另有 CLI 与 Python API。支持自建私有词汇库、打包发布到 semahash.org，内置 Physics/Mind/Society/Infrastructure 四层词汇，握手失败即 HALT（fail-closed），并附 Lean 4 形式化验证试点与可复现实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hash(canonical(definition)) 内容寻址：同一哈希即同一含义，定义改变即词改变
- 16 个 MCP 工具，含 sema_handshake 失败即停的语义校验与 sema_mint 新建模式
- 自建私有词汇库、打包为 GitHub Release 并发布/安装到 semahash.org
- Lean 4 形式化验证试点覆盖握手决策内核与规范化类型标签

## 适用场景

- 让多个 AI agent 在共享概念上做哈希级语义对齐与握手校验
- 为 agent 工作流建立可验证、可复用的协调协议与推理模式词汇库
- 通过 MCP 客户端搜索、铸造、引用内容寻址的概念模式
- 发布团队私有词汇库供他人和其他 agent 按名安装

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: Sema is a content-addressed reference system for reasoning and communication. Participants encode and hash informat
> L84: Your agent now has access to `sema_search`, `sema_lookup`, `sema_handshake`, and 9 more tools. Any MCP-compatible c
> L224: When running as an MCP server (`sema mcp`), these tools are available:

## 星数曲线

```mermaid
xychart-beta
    title "emergent-wisdom/sema 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `63fb11660c57` · [字段定义](../../DATASET.md)*
