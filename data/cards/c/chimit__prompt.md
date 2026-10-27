# chimit/prompt

⭐ 43 · PHP · MIT · 推送 2026-07-11 · [GitHub](https://github.com/chimit/prompt) · 个人维护

**Laravel 应用中用 Blade 语法管理 AI 提示词的包**

一个 Laravel Composer 包，把 AI 提示词以 Markdown 文件形式存放于 resources/prompts 目录，支持子目录组织。提示词文件可使用完整 Blade 语法，包括变量、PHP 表达式与 HTML 渲染；通过 Prompt::get() 方法传入数据渲染提示词，用法与 Blade 视图一致。面向在 Laravel 应用中集成 AI 功能的开发者，提供模板化的提示词管理方式。README 仅覆盖安装与基本用法，未展示与具体模型服务商的对接细节。

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

- 提示词以 .md 文件存放于 resources/prompts，支持子目录组织
- 提示词支持完整 Blade 语法（变量、PHP 表达式）
- Prompt::get() 方法按 Blade 视图方式传入数据渲染

## 适用场景

- 在 Laravel 项目中集中管理 AI 提示词模板
- 用 Blade 变量与表达式动态生成提示词
- 按目录结构组织不同场景的提示词（如 SEO）

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Prompt is a simple Laravel package for managing your AI prompts in Markdown files, with the full power of Blade.
> L40: Use the `Prompt::get()` method to render your prompts with data, just like you would with Blade views:

## 星数曲线

```mermaid
xychart-beta
    title "chimit/prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `89f41d91c8ac` · [字段定义](../../DATASET.md)*
