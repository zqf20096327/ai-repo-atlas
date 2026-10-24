# moe-mizrak/laravel-openrouter

⭐ 159 · PHP · MIT · 推送 2026-06-11 · [GitHub](https://github.com/moe-mizrak/laravel-openrouter) · [官网](https://moe-mizrak.gitbook.io/laravel-openrouter/) · 个人维护

**Laravel 包：将 OpenRouter 统一 LLM API 接入 Laravel 应用**

为 Laravel 应用提供接入 OpenRouter（统一 LLM 接口）的 PHP 包。通过 LaravelOpenRouter facade 或直接实例化 OpenRouterRequest 发起对话请求，以 ChatData DTO 结构化封装消息、模型、流式、reasoning、prompt caching、工具调用与 LLM 参数；并暴露 ProviderPreferencesData 实现对 provider 路由的偏好控制（fallback、价格、吞吐、延迟排序等）。要求 PHP 8.2+（v2.x 使用 spatie laravel-data），通过 composer 安装并发布配置文件，需设置 OpenRouter API key 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- facade 与直接实例化两种调用方式，支持流式对话请求（chatStreamRequest）
- ChatData DTO 覆盖 messages/prompt、LLM 参数、工具调用、reasoning、prompt caching、session_id 等
- ProviderPreferencesData 支持 provider 路由偏好（fallback/排序/价格/吞吐/延迟/ZDR）
- PHP 8.2+ 使用 spatie laravel-data；v1.0.9 兼容 PHP 8.1

## 适用场景

- 在 Laravel 应用中调用 OpenRouter 上的多家 LLM 模型
- 实现带会话连续性与流式输出的 AI 对话功能
- 按价格、吞吐或延迟偏好控制 OpenRouter 的 provider 路由

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: This Laravel package provides an easy-to-use interface for integrating **OpenRouter** into your Laravel application
> L28: composer require moe-mizrak/laravel-openrouter

## 星数曲线

```mermaid
xychart-beta
    title "moe-mizrak/laravel-openrouter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 158 --> 160
    line [159, 159]
```

2026-10-18 159 → 2026-10-24 159（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f04c17a1f6af` · [字段定义](../../DATASET.md)*
