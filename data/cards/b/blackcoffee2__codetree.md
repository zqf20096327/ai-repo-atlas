# blackcoffee2/codetree

⭐ 15 · TypeScript · MIT · 推送 2026-07-17 · [GitHub](https://github.com/blackcoffee2/codetree) · 个人维护

**CLI 工具：用 Tree-sitter 将代码库生成为 LLM 用的结构化快照**

面向开发者的命令行工具，基于 Tree-sitter 解析代码库，生成两种快照：compact 结构索引（列出各文件的函数、类、导入、导出等符号）与 raw 全量源码拼接，供大语言模型读取整个项目；示例中约 26.5k tokens 源码压缩至 900 tokens 以下。配套 code 命令按模型返回的文件清单提取完整源码，tree prompt / code prompt 生成配套提示词。通过 npm 全局安装，需 Node.js 20 及以上；语法树经 web-tree-sitter 以 WebAssembly 加载，无需本地编译。支持 JS/TS/Python/Java/Kotlin/Go/Rust/C/C++/Dart/Swift 等 13 类语言的结构摘要，其他语言按纯文本纳入。

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

- compact 结构索引与 raw 全源码两种快照格式
- code 命令按模型指定的文件清单提取完整源码
- 自动读取 .gitignore 并固定排除 .git、lockfiles 等文件
- Tree-sitter 语法树以 WebAssembly 加载，无需本地编译

## 适用场景

- 把大型代码库压缩成 token 友好的结构图交给 LLM 分析
- 让模型基于紧凑索引指出所需文件，再提取这些文件的完整源码
- 生成解释快照格式的提示词，配合任意 LLM 使用

## 场景标签

 · 领域:开发者工具/代码分析

## 证据(README 行号)

> L3: A command-line tool that uses Tree-sitter to turn a codebase into a single, token-efficient snapshot you can hand to
> L51: 2. `codetree tree prompt` to copy a short prompt that explains the snapshot's layout to the model. Paste the prompt

## 星数曲线

```mermaid
xychart-beta
    title "blackcoffee2/codetree 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `04cd50d3e560` · [字段定义](../../DATASET.md)*
