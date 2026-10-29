# dagengine/dagengine

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/dagengine/dagengine) · [官网](https://dagengine.ai) · 组织维护

**面向 TypeScript 开发者的 AI 工作流 DAG 编排引擎**

TypeScript 编写的 DAG 执行引擎库，面向构建 AI 工作流的开发者：将数据项（sections）与分析维度（dimensions）声明为有向无环图依赖后，引擎自动并行执行无依赖任务，内置按维度/提供商的成本与 token 实时统计、条件跳过逻辑、指数退避重试与提供商回退链。支持 Anthropic/OpenAI/Gemini 统一接口混用，提供 18 个 async 生命周期钩子，可搭配 Portkey 网关获得限流、缓存与负载均衡。以 npm 包分发，要求 Node.js≥18。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于依赖声明自动并行执行任务（sections×dimensions DAG）
- 内置按维度与提供商的成本/token 实时跟踪
- 提供商回退链与自动重试（指数退避）
- 支持 Anthropic/OpenAI/Gemini 统一接口与 Portkey 网关

## 适用场景

- 对批量数据并行跑多个 AI 分析维度并控制成本
- 在同一工作流中混用不同模型提供商
- 通过生命周期钩子集成数据库、缓存等外部服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: **dagengine** is a TypeScript DAG engine that turns sequential AI workflows into parallel ones automatically.
> L100: Use Anthropic Claude, OpenAI GPT, Google Gemini with a unified interface. Switch providers per dimension. Mix mode
> L271: const engine = new DagEngine({

## 星数曲线

```mermaid
xychart-beta
    title "dagengine/dagengine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3ba4ae2173a7` · [字段定义](../../DATASET.md)*
