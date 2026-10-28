# kannamma-labs/nirdosha

⭐ 22 · Rust · MIT · 推送 2026-10-01 · [GitHub](https://github.com/kannamma-labs/nirdosha) · [官网](https://github.com/kannamma-labs/nirdosha/wiki) · 组织维护

**供 AI 代理安全编写后端代码的系统级编程语言**

Nirdosha 是一门编译型系统语言，面向由 AI 编码代理编写和维护、无人工逐行审查即可运行的后端服务场景。语言无 GC、无 mutex 原语（从语法上排除锁序死锁），构建时用 Z3 证明无数据竞争、整数/缓冲区溢出及 Hoare 契约；LL(1) 文法导出为 GBNF 供受限解码，emit-ast 输出结构化 AST 供自修复循环使用。编译器自身用 Rust 实现，经 LLVM 生成原生代码，可从 struct 生成类型检查的 UI。限制：无 Rust 式借用检查器，不声明 FIPS 140-3 合规；部分功能仅为设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LL(1) 文法导出 GBNF，约束 LLM 生成的每个 token 合法
- Z3 构建时证明：数据竞争、溢出、Hoare 前后置条件
- 语言中不存在 mutex 原语，无法表达锁序死锁
- 结构化诊断与 emit-ast 供代理自修复循环使用

## 适用场景

- 让 AI 代理生成并运行经形式化验证的后端服务
- 在无人工逐行审查的场景下部署代理生成的 CRUD/合规服务
- 通过 GBNF 受限解码约束代理输出的语法合法性

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L95: Nirdosha targets one specific problem: **a backend service written and maintained by an AI coding agent, with no hu
> L3:  A systems language designed so your AI agent can't write the bugs AI agents always write.

## 星数曲线

```mermaid
xychart-beta
    title "kannamma-labs/nirdosha 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8b6ee22f6559` · [字段定义](../../DATASET.md)*
