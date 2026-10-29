# zircote/rlm-rs

⭐ 62 · Rust · MIT · 推送 2026-10-23 · [GitHub](https://github.com/zircote/rlm-rs) · [官网](https://zircote.com/rlm-rs/) · 个人维护

**面向 Claude Code 的 Rust CLI：分块+递归子 LLM 处理超长文档**

实现递归语言模型（RLM）模式的 Rust 命令行工具，基于 arXiv:2512.24601 论文，用于处理超出上下文窗口的长文档（可达窗口约 100 倍大小）。核心机制：多种分块策略（semantic/code/fixed/parallel）、BGE-M3 自动嵌入、混合语义+BM25 检索（RRF 融合）、SQLite 状态持久化、dispatch/aggregate 命令支持并行子代理处理。面向使用 Claude Code 的开发者，通过 cargo/Homebrew/源码安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种分块策略（semantic/code/fixed/parallel），code 模式支持 9 种语言的函数/类边界切分
- BGE-M3 自动嵌入与混合语义+BM25 检索（RRF 融合）
- SQLite 状态持久化与 pass-by-reference 按 ID 取块
- dispatch/aggregate 支持并行子代理工作流

## 适用场景

- 让 Claude Code 分析远超上下文窗口的大型文档或代码库
- 对加载的文档做语义/正则混合检索
- 拆分任务给并行子代理再聚合结果

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: Recursive Language Model (RLM) CLI for Claude Code - handles long-context tasks via chunking and recursive sub-LLM 
> L13: Based on the RLM pattern from arXiv:2512.24601, enabling analysis of documents up to 100x larger than typical conte
> L127: rlm-cli is designed to work with the rlm-rs Claude Code plugin, implementing the RLM architecture:

## 星数曲线

```mermaid
xychart-beta
    title "zircote/rlm-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-29 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e18833d23f21` · [字段定义](../../DATASET.md)*
