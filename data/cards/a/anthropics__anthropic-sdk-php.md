# anthropics/anthropic-sdk-php

⭐ 201 · PHP · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/anthropics/anthropic-sdk-php) · 组织维护

**在 PHP 应用中调用 Claude API 的官方 SDK**

Anthropic 官方维护的 PHP SDK，为 PHP 应用提供访问 Claude API 的客户端。通过 Composer 分发，依赖 PSR-18 HTTP 客户端（未安装时可加装 Guzzle）。要求 PHP 8.1.0+。文档位于 platform.claude.com，README 提供最小调用示例。许可证为 Apache 2.0，早期版本及此前合并的第三方贡献仍保留 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Composer 安装（anthropic-ai/sdk）
- 依赖 PSR-18 HTTP 客户端，可选配 Guzzle
- 要求 PHP 8.1.0+
- Apache 2.0 许可，旧版本保留 MIT

## 适用场景

- 在 PHP 项目中接入 Claude API
- 为现有 PHP 服务添加模型调用能力

## 场景标签

 · 领域:LLM 基础设施/客户端 SDK

## 证据(README 行号)

> L5: The Anthropic SDK for PHP provides access to the Claude API from PHP applications.
> L14: composer require "anthropic-ai/sdk:^1.14.0"

## 星数曲线

```mermaid
xychart-beta
    title "anthropics/anthropic-sdk-php 星数(近 12 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-30", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-25", "2026-11-27"]
    y-axis "stars" 193 --> 203
    line [194, 195, 196, 197, 194, 198, 201, 202, 201, 202, 201, 201]
```

2026-10-25 194 → 2026-11-27 201（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cf1596fe6d29` · [字段定义](../../DATASET.md)*
