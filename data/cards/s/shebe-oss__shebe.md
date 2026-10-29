# shebe-oss/shebe

⭐ 35 · Rust · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/shebe-oss/shebe) · [官网](https://gitlab.com/rhobimd-oss/shebe) · 组织维护

**面向 AI 编码代理的本地 BM25 代码全文搜索工具**

Rust 实现的本地代码搜索工具，基于 BM25 对本地克隆的仓库建立索引，提供 search_code、find_references 等 14 个 MCP 工具供 Claude Code、Codex 等编码代理调用，也提供 CLI 二进制。无需嵌入、GPU 或云端，官方数据为 2ms 查询延迟、每查询 200-700 tokens、支持 UTF-8 与多语言混合代码库。限制：不支持远程 URL 索引、无语义相似度匹配。通过 Homebrew 或手动下载二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个 MCP 工具（search_code、find_references、read_file 等）供编码代理调用
- BM25 本地索引：官方数据 2ms 查询、2k-12k files/sec 索引速度
- 无需嵌入/GPU/云端，全 UTF-8 支持（含 CJK）
- CLI 与 MCP 两个二进制，各约 8MB

## 适用场景

- 让 Claude Code 等编码代理在大代码库中做代码搜索和引用查找
- 重构前用 find_references 枚举受影响的代码位置
- 在不联网环境下为代理提供本地代码检索能力

## 场景标签

 · 领域:开发者工具/代码检索

## 证据(README 行号)

> L28:  - 14 MCP tools for coding agents (claude, codex etc) (reference)
> L9: Shebe is a fast and simple local code-search tool powered by BM25. No embeddings,

## 星数曲线

```mermaid
xychart-beta
    title "shebe-oss/shebe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3a8753586883` · [字段定义](../../DATASET.md)*
