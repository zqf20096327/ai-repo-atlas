# gelleson/codemerge

⭐ 24 · Rust · 推送 2026-02-28 · [GitHub](https://github.com/gelleson/codemerge) · 个人维护

**Rust CLI：合并代码文件供 LLM 作上下文并统计 token**

用 Rust 编写的命令行工具，面向需要将代码库喂给 AI 代码生成模型的开发者。提供 merge（按 glob 过滤合并多文件为单一输出，支持 token 预算上下限）、tree（带 token 计数的文件树）、tokens（token 计数，基于 gpt-tokenizer 库估算 LLM 成本）与 cache 子命令；遵循 .gitignore（含嵌套），缓存可选 SQLite、RocksDB 或禁用。安装方式为一行安装脚本或从源码 cargo 构建；早期 Go 版本位于 /go 分支且不再维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多文件合并为单一输出，支持 glob 过滤与 token 预算上下限
- tree/tokens 命令输出带 token 计数的文件树与成本估算
- 遵循 .gitignore（含嵌套目录多文件）
- SQLite/RocksDB/none 三种缓存策略

## 适用场景

- 把项目代码合并成单文件喂给 LLM 生成上下文相关的代码
- 估算代码库 token 数以预估 LLM 调用成本
- 生成带 token 计数的项目文件结构视图

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: CodeMerge is a command-line interface (CLI) tool built with Rust for merging and analyzing codebases. It leverages R
> L9: - **Token Counting:** Calculates the number of tokens in files using the `gpt-tokenizer` library, useful for estimat
> L96: Count tokens in files, which is useful when estimating costs for large language model interactions:

## 星数曲线

```mermaid
xychart-beta
    title "gelleson/codemerge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9b1e22cce497` · [字段定义](../../DATASET.md)*
