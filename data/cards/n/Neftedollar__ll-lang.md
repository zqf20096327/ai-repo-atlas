# Neftedollar/ll-lang

⭐ 10 · F# · NOASSERTION · 推送 2026-06-01 · [GitHub](https://github.com/Neftedollar/ll-lang) · [官网](https://neftedollar.com/ll-lang/) · 个人维护

**面向 LLM 代码生成的静态类型函数式语言，编译到五种目标语言**

ll-lang 是一种静态类型函数式编程语言，提供端到端编译器 `lllc`，可将同一份源码编译为 F#、TypeScript、Python、Java、C#（另有实验性 LLVM 后端）。语言设计围绕 LLM 代码生成：精简语法（15 个关键字）、Hindley-Milner 类型推断、编译期捕获标签违规等错误、机器可读的单行错误码格式。自带 10 个模块的自托管标准库，已完成 bootstrap 自举，并通过内置 MCP server（30 个工具）接入 Claude Code/Cursor/Zed 等 LLM 客户端。提供安装脚本、浏览器 Playground 与源码构建路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次编译输出 fs/ts/py/java/cs 多目标代码
- 内置 MCP server 提供 30 个结构化工具（编译/诊断/修复/符号导航）
- 机器可读错误码格式（EXXX line:col），供 LLM 直接解析
- 自举完成：编译器由 ll-lang 自身编写并通过 fixpoint 验证

## 适用场景

- 让 LLM agent 生成可在编译期捕获类型错误的代码
- 同一份业务逻辑产出多种语言的目标代码
- 通过 MCP 将编译器工具接入 Claude Code/Cursor/Zed 工作流

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: > **A statically-typed functional language designed for LLM code generation.** Token-efficient syntax, compiled = wo
> L343: ll-lang is not a general-purpose language. It is optimized for one use case: **LLM agents writing correct code on 
> L198: ll-lang ships a built-in MCP server. Wire it to Claude Code, Cursor, or Zed — your LLM client gains structured too


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `3129c6ed0a72` · [字段定义](../../DATASET.md)*
