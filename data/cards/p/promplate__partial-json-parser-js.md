# promplate/partial-json-parser-js

⭐ 246 · TypeScript · MIT · 推送 2026-06-01 · [GitHub](https://github.com/promplate/partial-json-parser-js) · [官网](https://npmx.dev/partial-json) · 组织维护

**解析 LLM 流式输出的不完整 JSON 的 JS 库**

轻量级纯 JavaScript 库，用于解析 LLM 流式生成过程中尚未完结的 JSON 字符串，使数据可在收到最后 token 前流式交付。提供 parse 函数，行为与内置 JSON.parse 一致，另接受 allowPartial 参数（Allow 常量按位或组合）控制字符串、数字、数组、对象等类型的部分解析容忍度，默认 Allow.ALL。畸形 JSON 抛出 MalformedJSON 错误。同时提供 CommonJS 与 ESM 构建，测试使用 Vitest，另有 Python 实现版本。

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

- 解析未完结的部分 JSON 字符串，支持流式输出场景
- Allow 常量按位或控制各类值的部分解析容忍度
- 支持特殊值（NaN、±Infinity）的部分解析
- 纯 JavaScript 实现，同时提供 CommonJS 与 ESM 构建

## 适用场景

- 流式展示 LLM 生成的结构化 JSON 数据
- 在收到完整响应前提前消费部分字段
- 在 agent 流程中边生成边解析结构化输出

## 场景标签

 · 领域:LLM 开发工具/解析库

## 证据(README 行号)

> L3: Sometimes we need **LLM (Large Language Models)** to produce **structural information** instead of natural language.
> L5: But before receiving the last token of response, the JSON is broken, which means you can't use `JSON.parse` to decod

## 星数曲线

```mermaid
xychart-beta
    title "promplate/partial-json-parser-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 245 --> 247
    line [246, 246]
```

2026-10-18 246 → 2026-10-24 246（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `244e1bf6e90b` · [字段定义](../../DATASET.md)*
