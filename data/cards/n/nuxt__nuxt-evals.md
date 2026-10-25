# nuxt/nuxt-evals

⭐ 52 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/nuxt/nuxt-evals) · [官网](https://nuxt.com/evals) · 组织维护

**Nuxt 官方维护的 AI 模型编码能力评测集与评测脚手架**

由 Nuxt 组织维护的 agent 评测仓库，基于 @vercel/agent-eval 运行：每个评测是 `evals/` 下一个自包含 Nuxt 项目，向 agent 提供带缺陷或次优的起始代码与症状式提示，完成后运行对 agent 不可见的 vitest 断言判定。支持 30 个模型实验（经 Vercel AI Gateway 接入 Claude/GPT/Gemini/DeepSeek/Kimi 等），带记忆化只跑未完成的 (model, eval) 对，可导出含 avgCostUsd 的结果并发布到 nuxt.com。当前含 Nuxt 21 项、Nuxt Content 2 项、Nuxt UI 8 项评测。

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

- 21+2+8 共 31 个自包含 Nuxt 编码评测（fix/build 两类）
- 30 个模型实验配置，经 Vercel AI Gateway 接入多家模型
- 记忆化运行：仅执行未完成的 (model, eval) 组合
- 从 transcript 提取 token 并按快照价目计算 avgCostUsd

## 适用场景

- 对比各家编码模型在 Nuxt 任务上的完成情况
- 为 Nuxt 生态新增编码评测条目
- 追踪模型成本并发布评测结果到 nuxt.com

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Agent evaluations for Nuxt coding tasks, powered by `@vercel/agent-eval`.
> L78: Each eval is a self-contained Nuxt project in `evals/`. Most evals provide broken or suboptimal starter code that t
> L90: |`EVAL.ts`|Test file run after the agent finishes (withheld from agent)|

## 星数曲线

```mermaid
xychart-beta
    title "nuxt/nuxt-evals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `11af356bd8c5` · [字段定义](../../DATASET.md)*
