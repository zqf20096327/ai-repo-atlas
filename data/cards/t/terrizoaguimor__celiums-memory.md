# terrizoaguimor/celiums-memory

⭐ 23 · Rust · Apache-2.0 · 推送 2026-08-23 · [GitHub](https://github.com/terrizoaguimor/celiums-memory) · [官网](https://celiums.ai) · 个人维护

**供 AI agent 嵌入的认知记忆引擎：持久记忆+日志+伦理引擎**

以 Rust 实现的认知记忆引擎（非应用，无 UI），通过 MCP（stdio/Streamable HTTP）与 REST v1 供 Claude Code、Cursor 等 MCP 客户端及自有软件嵌入，提供 remember/recall 混合检索（向量+全文+PAD 情感）、重要性评分与生命周期衰减、哈希链式第一人称日志、四层伦理评估引擎（A 词典/B CVaR/C 哲学/K 判例语料可选）、按用户的昼夜节律调制、forage 知识检索、加密检查点与租户隔离。引擎不绑定 LLM/embedding 供应商（BYO，含本地确定性 embedder）。dev 分支为 Rust/Cloudflare 迁移工作线，自述未生产就绪，稳定线在 main。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP 服务器形态提供 19 个工具：记忆、日志、伦理、知识检索
- 混合检索：向量+全文+情感 PAD 共振，含昼夜节律调制
- 四层伦理引擎，判例语料 Layer K 为可选 release 资产，缺失时干净弃权
- provider 中立：不绑定 LLM/embedding，支持自带模型或本地确定性 embedder

## 适用场景

- 给 MCP 客户端（Claude Code/Cursor 等）接入持久记忆与自动上下文引导
- 为 agent 构建带审计链的第一人称日志
- 在 agent 输出前经过可审计的伦理评估层

## 场景标签

 · 领域:LLM 基础设施/agent 记忆

## 证据(README 行号)

> L13: Celiums Memory is an **engine**, not an app — no UI, no dashboard to log
> L16: speaks **MCP** (Model Context Protocol) so any compatible client

## 星数曲线

```mermaid
xychart-beta
    title "terrizoaguimor/celiums-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `de0eabf03bfd` · [字段定义](../../DATASET.md)*
