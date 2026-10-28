# subhashladumor1/laravel-ai-guard

⭐ 29 · PHP · MIT · 推送 2026-02-14 · [GitHub](https://github.com/subhashladumor1/laravel-ai-guard) · 个人维护

**Laravel 应用的 AI 成本追踪与预算管控包**

面向 Laravel 10.x-12.x 的 PHP 包（PHP 8.1+），围绕 AI 调用做成本治理：调用前按 token 单价估算费用，调用后从响应记录用量与花费，支持全局/用户/租户三级预算与周期重置，超预算中间件返回 402，Kill Switch 可经 .env 关停全部 AI 调用（503）。计费维度覆盖缓存读写、长上下文及音频/视频/图像/嵌入等多模态，适配 OpenAI、Anthropic、Gemini、xAI、Mistral、DeepSeek 的价目；与 Laravel AI SDK 配合使用，也可用于任意 AI API。

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

- 调用前估算与调用后按响应记录 token 用量与成本
- 全局/用户/租户三级预算，超支返回 402，Kill Switch 全局关停
- 支持 Context Caching、长上下文与音频/视频/图像/嵌入等多模态计费维度
- 提供 AIGuard Facade、中间件与 artisan 报表/预算重置命令

## 适用场景

- 给我的 SaaS 按用户或租户设 AI 花费上限
- 在调用 AI 前预估成本，避免账单超支
- 按天/月生成 AI 用量与成本报表
- 追踪多模态（视频、音频、图像）调用的真实花费

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L6:  It helps Laravel developers track OpenAI & LLM token usage 📊, estimate AI costs before execution ⚠️, enforce per-us
> L49: > **TL;DR:** Laravel AI SDK does the AI. Laravel AI Guard decides _whether_ you're allowed to call and _how much_ y
> L330: |Condition|Response|

## 星数曲线

```mermaid
xychart-beta
    title "subhashladumor1/laravel-ai-guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dd5a26e5258c` · [字段定义](../../DATASET.md)*
