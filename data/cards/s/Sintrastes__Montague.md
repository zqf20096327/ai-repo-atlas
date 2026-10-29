# Sintrastes/Montague

⭐ 18 · Rust · AGPL-3.0 · 推送 2026-05-28 · [GitHub](https://github.com/Sintrastes/Montague) · 个人维护

**将自然语言表达式非确定性解析为结构化形式的库与 DSL**

以 Richard Montague 命名的库与领域专用语言：基于带子类型的 Lambek 演算与用户提供的词典，将自然语言字符串（可能非确定地）解析为特定类型的项，供分析或推理使用；通过子类型与语义类别（如 person <: noun）剪枝搜索空间，产出可转换为逻辑格式（如类型化逻辑编程查询）的结构化表示。提供 Rust 与 Haskell API 及 .mont 模式文件语法，另有 montague-reflex 网页与移动界面。项目从 Haskell 原型重写为 Rust，作者自述处于早期阶段，类型系统尚不支持量词等特性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 带子类型的 Lambek 演算 + 用户词典做非确定性解析
- 提供 .mont DSL 定义特定领域的解析模式，附 Rust/Haskell API
- 结构化输出可转换为类型化逻辑编程语言查询
- 提供 montague-reflex 网页与移动界面

## 适用场景

- 将自然语言查询解析为结构化逻辑形式以做推理
- 在 LLM 前置流程中先尝试确定性解析以降低资源消耗
- 定义特定领域语法模式进行受控自然语言理解

## 场景标签

 · 领域:自然语言处理/计算语言学

## 证据(README 行号)

> L17: Montague (named in honor of mathematician and philosopher Richard Montague) is a library and domain specific langua
> L48: I think that one way we might work to address these concerns, but still build useful AI systems for everyday people
> L50: Moving forward, I think Montague (or something like it) could prove incredibly useful as a "first pass" for AI-base

## 星数曲线

```mermaid
xychart-beta
    title "Sintrastes/Montague 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `62fd09964e61` · [字段定义](../../DATASET.md)*
