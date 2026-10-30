# oziriemeka/laravel-llm-suite

⭐ 38 · PHP · MIT · 推送 2026-05-14 · [GitHub](https://github.com/oziriemeka/laravel-llm-suite) · [官网](https://laravel-llm-suite.hashnode.space/) · 个人维护

**给 Laravel 开发者的多 LLM 提供商统一接入工具包**

基于驱动模式的 Laravel LLM 工具包，以统一 API 接入 OpenAI、Anthropic、LM Studio、ModelsLab 等提供商，覆盖聊天、图像生成、模型列表功能。提供会话管理（数据库或 session 存储）、token 用量统计、LlmFake 与 Dummy 提供商测试支持，并支持注册自定义驱动扩展其他提供商。要求 PHP 8.1+ 与 Laravel 10/11/12，通过 Composer 安装后发布配置与迁移文件。

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

- 驱动模式切换提供商，统一聊天/图像生成接口
- 会话多轮对话管理（database/session 双存储驱动）
- token 用量统计与延迟信息（ChatResponse/TokenUsage）
- 内置 fake 与 Dummy 提供商支持无 API 调用测试

## 适用场景

- Laravel 应用中接入多家 LLM 提供商并按需切换
- 本地 LM Studio 运行开源模型用于开发测试
- 构建带持久化历史的聊天机器人并追踪 token 成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: A unified, driver-based Laravel toolkit for working with multiple LLM providers for chat, image generation, and more
> L10: - **Driver Pattern** - Switch providers like Laravel's Storage or Mail systems

## 星数曲线

```mermaid
xychart-beta
    title "oziriemeka/laravel-llm-suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `09bf8c6bd321` · [字段定义](../../DATASET.md)*
