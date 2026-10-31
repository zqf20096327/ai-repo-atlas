# r-Larch/OpenAi.JsonSchema

⭐ 16 · C# · MIT · 推送 2026-05-12 · [GitHub](https://github.com/r-Larch/OpenAi.JsonSchema) · 个人维护

**为 OpenAI Structured Outputs 生成 JSON Schema 的 C# 库**

面向 .NET 开发者的轻量库：从 C# 的 class/record/struct 或 Fluent 构建器生成符合 OpenAI JSON Schema 子集的 schema，供 OpenAI 模型 Structured Outputs 功能使用。机制上读取 System.ComponentModel.DescriptionAttribute 生成描述，处理 Nullable 类型，自动管理 $defs/$ref，支持 System.Text.Json 特性与多态类型（JsonPolymorphicAttribute）。通过 NuGet 以包形式分发，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 class/record/struct 静态生成符合 OpenAI 子集的 JSON Schema
- 读取 DescriptionAttribute 与 System.Text.Json 特性控制 schema
- 自动管理 $defs 与 $ref，支持多态类型
- Fluent API 动态构建自定义 schema

## 适用场景

- 在 C# 项目中为 OpenAI 结构化输出定义响应格式
- 用注解驱动方式维护 schema 与模型定义的一致性
- 为 JsonElement/object 类型属性定义部分字段的 schema

## 场景标签

 · 领域:LLM 集成开发/.NET 库

## 证据(README 行号)

> L5: **OpenAi-JsonSchema** is a lightweight library for generating valid JSON Schema for OpenAI's Structured Outputs feat
> L12: - Ensures compatibility with OpenAI's JSON Schema format for structured outputs.

## 星数曲线

```mermaid
xychart-beta
    title "r-Larch/OpenAi.JsonSchema 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ecea8bb72822` · [字段定义](../../DATASET.md)*
