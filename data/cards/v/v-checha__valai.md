# v-checha/valai

⭐ 22 · TypeScript · MIT · 推送 2025-12-11 · [GitHub](https://github.com/v-checha/valai) · 个人维护

**面向 LLM 输出校验的 TypeScript 验证库**

TypeScript schema 验证库，针对 LLM 输出、function calling 与结构化生成场景设计：提供 parseLLM 解析模式，内置 JSON 修复（尾逗号、单引号、未闭合括号、注释等）、Markdown 代码块提取、LLM 模式下的类型自动转换与失败时返回部分数据。支持导出 JSON Schema、OpenAI、Claude、Gemini 格式，并提供 .describe()/.examples() AI 元数据与完整 TypeScript 类型推断。通过 npm 安装，MIT 许可。

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

- parseLLM 模式内置 JSON 修复、Markdown 提取与类型转换
- 一键导出 OpenAI / Claude / Gemini / JSON Schema 格式
- .describe() 与 .examples() 提供 LLM 引导元数据
- 解析失败时返回已解析的部分数据供重试

## 适用场景

- 校验并修复 LLM 返回的格式不合规 JSON
- 为 OpenAI/Claude/Gemini function calling 生成工具 schema
- 结构化生成场景中做带类型推断的数据校验

## 场景标签

 · 领域:LLM 基础设施/数据校验

## 证据(README 行号)

> L3: **AI-native TypeScript validation library** optimized for LLM outputs, function calling, and structured generation.
> L14: - **LLM-First Design** - Built specifically for validating AI/LLM outputs
> L227: |`.parseLLM(data, options?)`|LLM-friendly parse with repair|

## 星数曲线

```mermaid
xychart-beta
    title "v-checha/valai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `472b19635a99` · [字段定义](../../DATASET.md)*
