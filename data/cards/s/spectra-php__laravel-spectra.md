# spectra-php/laravel-spectra

⭐ 21 · PHP · MIT · 推送 2026-10-29 · [GitHub](https://github.com/spectra-php/laravel-spectra) · [官网](https://spectraphp.com) · 个人维护

**Laravel 应用的 AI/LLM 调用可观测性包：追踪、计费与预算**

Laravel 包，为 AI 与 LLM 调用提供可观测能力：自动追踪 AI 请求、计算不同定价单位下的用量与成本、按用户执行预算限制，并通过统一仪表盘与 API 查看 AI 操作。2.0 版本自动追踪流式响应、对每家提供商的 prompt-cache 读写与推理 token 计费，并更新定价目录；多数应用只需运行一个新迁移。面向在 Laravel 中构建 AI 功能的开发者，由个人作者 Ahmad Mayahi 维护，MIT 许可。

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

- 自动追踪 AI 请求并计算用量与成本
- 按用户执行预算限制
- 统一仪表盘与 API 查看操作
- 2.0 自动追踪流式响应并对缓存读写/推理 token 计费

## 适用场景

- 我在 Laravel 应用里追踪各 AI 提供商的请求与成本
- 按用户设置调用预算并强制执行
- 通过仪表盘检查 AI 功能的运行情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: Spectra is a comprehensive Laravel package for AI observability. It helps you track AI requests, measure usage, calc
> L17: Spectra 2.0 tracks streamed responses automatically, bills prompt-cache reads and writes and reasoning tokens for e

## 星数曲线

```mermaid
xychart-beta
    title "spectra-php/laravel-spectra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b1c7d4e11aec` · [字段定义](../../DATASET.md)*
