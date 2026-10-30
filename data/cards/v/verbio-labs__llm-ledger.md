# verbio-labs/llm-ledger

⭐ 27 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/verbio-labs/llm-ledger) · 组织维护

**由 LLM 维护的可验证、带时间感的 markdown 知识账本**

基于 Claude Code 实现的知识管理系统，延续 Karpathy 的 LLM Wiki 模式：以原子 claim 为单位积累知识，每条带来源、置信度与有效期，事实只被 supersede/contest 而不覆盖，支持 as-of 时间点查询。提供 /ingest、/compile、/query、/audit、/timeline 等命令，四层目录结构（inbox/raw/ledger/schema），全部写入由 LLM 完成。附零依赖校验器并通过 CI 强制检查，另有 MCP server 供任意 AI 客户端复用同一记忆。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原子 claim 带 provenance/confidence/valid_from/valid_until，支持 as-of 查询
- append-only：事实被 supersede 或标 contested，历史不丢失
- 零依赖校验器（ledger.py check）随 CI 每次推送强制校验
- 通过 MCP 暴露 ledger_search/timeline/add_claim 等工具，供任意 MCP 客户端使用

## 适用场景

- 让 LLM 长期维护一个可溯源的个人知识库
- 查询某个时间点上为真的历史事实（如 2005 年冥王星）
- 跨 Claude Code/Cursor 等 AI 工具共享同一份可验证记忆

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L24: A permanent markdown knowledge base that an LLM synthesizes and maintains for you —
> L30: and the asking; the LLM does every write, every verification, and every cross-reference.
> L80: 2. **Ledger it** — `/compile` **extracts claims** from the source, assigns provenance / confidence / validity,

## 星数曲线

```mermaid
xychart-beta
    title "verbio-labs/llm-ledger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8e2620de9945` · [字段定义](../../DATASET.md)*
