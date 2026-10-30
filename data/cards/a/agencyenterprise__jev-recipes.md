# agencyenterprise/jev-recipes

⭐ 24 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/agencyenterprise/jev-recipes) · [官网](https://jev-recipes.com) · 组织维护

**JS/TS 的类型化 LLM 决策函数库：路由、重排、门控等 248 个配方**

面向 JavaScript/TypeScript 开发者的 248 个决策配方库：以单个函数调用完成 route、rerank、tool-call-gate、verify、answerability 等文本决策，每个返回带类型的结果并显式给出不确定性（ready/review 状态）。每个配方通过 TypeSafe 的 System One API 或注入的兼容客户端调用模型。提供 npm 包、npx CLI（可离线试用 fixture，无需 API key）与批量接口（route-many 批量 20 条/次），支持接入 Vercel AI SDK 或 LangChain。要求 Node.js 22.9+ 与 TypeSafe API key。

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

- 248 个决策配方，返回带类型与显式不确定性的结果
- CLI 支持离线 fixture 试用与 JSON/stdin 输入运行
- route-many 批量处理（默认每批 20 条、上限 500 请求）
- 可插入 Vercel AI SDK / LangChain agent 框架

## 适用场景

- 在客服流中把消息路由到对应团队并在不确定时请求人工
- agent 循环中对工具调用、完成声明做门控审查
- RAG 流程中重排证据、判断可回答性与声明核验

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Typed AI decisions for agents, RAG, and support flows: route, rerank, gate, grade, compare, and label text with on
> L28: Each recipe accepts your data, calls Jev through TypeSafe's System One API or an injected compatible client, and re
> L129: The TypeSafe SDK handles API calls and typed answers. Recipes add the instructions, input and response validation,

## 星数曲线

```mermaid
xychart-beta
    title "agencyenterprise/jev-recipes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a44af176ab99` · [字段定义](../../DATASET.md)*
