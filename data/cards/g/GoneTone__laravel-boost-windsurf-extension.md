# GoneTone/laravel-boost-windsurf-extension

⭐ 25 · PHP · MIT · 推送 2026-03-29 · [GitHub](https://github.com/GoneTone/laravel-boost-windsurf-extension) · [官网](https://packagist.org/packages/gonetone/laravel-boost-windsurf-extension) · 个人维护 · 中文 README

**为 Windsurf 编辑器提供 Laravel Boost 集成的 Composer 包**

面向 Laravel 开发者的 Composer 开发包，将 Laravel Boost 接入 Windsurf 编辑器或 Windsurf JetBrains 插件（如 PhpStorm）。安装后 Laravel Boost 自动检测 Windsurf，通过 php artisan boost:install 引导安装，可选择 cascade（Windsurf Editor）或 cascade_jetbrains（JetBrains 插件）两种 AI agent 选项。因 Windsurf 仅支持全局级 MCP 配置，切换项目时需运行带 --mcp 参数的命令更新配置指向。要求 PHP 8.2+、Laravel 11.45.3/12.41.1/13.0+ 与 Laravel Boost 2.1.6+。

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

- 通过 Composer 安装，Laravel Boost 自动检测 Windsurf
- 支持 cascade 与 cascade_jetbrains 两种 AI agent 选项
- 提供 --mcp 命令在项目切换时更新 Windsurf MCP 配置

## 适用场景

- 在使用 Windsurf 编辑器时接入 Laravel Boost 的 AI 能力
- 在 PhpStorm 等 JetBrains IDE 中通过 Windsurf 插件使用 Laravel Boost
- 多 Laravel 项目间切换时更新 MCP 配置路径

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: A Laravel Composer package that provides Windsurf integration for Laravel Boost.
> L38: During installation, you will be prompted to select an AI agent. The available options will include the following t

## 星数曲线

```mermaid
xychart-beta
    title "GoneTone/laravel-boost-windsurf-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ddb0094900a3` · [字段定义](../../DATASET.md)*
