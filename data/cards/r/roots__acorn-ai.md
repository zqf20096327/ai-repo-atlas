# roots/acorn-ai

⭐ 25 · PHP · MIT · 推送 2026-06-03 · [GitHub](https://github.com/roots/acorn-ai) · [官网](https://roots.io/announcing-acorn-ai/) · 组织维护

**为 WordPress/Acorn 提供 laravel/ai 封装与 Abilities API 集成的 PHP 包**

Roots 维护的 Acorn 扩展包：在 WordPress 环境中引入 laravel/ai 的完整能力（agents、tools、embeddings、图像生成、音频、转录、reranking），并对接 WordPress 6.9+ 的 Abilities API，将 ability 类通过 Laravel 服务容器解析，支持依赖注入、REST 调用与 MCP Adapter 暴露。API key 经环境变量传给 WordPress AI provider 插件，支持 OpenAI、Anthropic、Gemini。要求 PHP 8.4+、WordPress 6.9+、Acorn 5.0+，经 composer 安装。

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

- 在 WordPress 中经 Acorn 容器提供 laravel/ai 全部功能
- 封装 Abilities API 注册，ability 类经 Laravel 容器解析并支持依赖注入
- API key 经环境变量自动传给 WordPress AI 插件，不存于 wp_options
- ability 可通过 REST 与 WordPress MCP Adapter 暴露给 AI agent

## 适用场景

- 在 WordPress 站点上构建 AI agent、工具与 abilities
- 将文章摘要等能力以 REST API 和 MCP 工具形式提供给 AI agent 调用
- Laravel/Acorn 技术栈开发者统一管理 AI provider 配置与密钥

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: AI support for Acorn — wraps laravel/ai and adds first-class integration with the WordPress Abilities API.

## 星数曲线

```mermaid
xychart-beta
    title "roots/acorn-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 26
    line [24, 25]
```

2026-10-18 24 → 2026-10-30 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6165c4a60099` · [字段定义](../../DATASET.md)*
