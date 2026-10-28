# moonshine-software/forty-five

⭐ 31 · TypeScript · MIT · 推送 2026-02-16 · [GitHub](https://github.com/moonshine-software/forty-five) · [官网](https://getmoonshine.app) · 组织维护

**为 MoonShine 项目安装 AI 编码指南与斜杠命令的 CLI 工具**

面向使用 MoonShine（Laravel 后台面板）框架的开发者的 npm CLI 工具：forty-five init 在项目内下载并安装组件文档、开发指南与 Claude 斜杠命令（如 /forty-five.components、/forty-five.field），使 AI 编码代理在生成 MoonShine 代码时遵循组件结构、必需包装层、OKLCH 调色板等框架约定。当前完整支持 Claude Code，Cursor 与 GitHub Copilot 标注为即将支持；update/status 命令尚未发布，指南从官方仓库拉取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- forty-five init 交互式选择 AI 代理并下载命令与指南
- 提供组件、布局、调色板、自定义字段与组件五类斜杠命令
- 指南覆盖 blade 组件、调色板、字段与组件开发四份文档
- 要求在 Laravel/MoonShine 项目根目录运行（需存在 composer.json）

## 适用场景

- 让 Claude Code 按 MoonShine 约定生成后台组件与自定义字段
- 为 MoonShine 项目统一 AI 生成代码的结构与最佳实践
- 通过斜杠命令快速创建布局与 OKLCH 配色方案

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Forty-Five is a CLI tool that brings AI-powered development assistance to your MoonShine projects. Install guideline
> L9: - 🤖 **AI Agent Integration** - Works with Claude Code (more agents coming soon)
> L22: npm install -g @moonshine-software/forty-five

## 星数曲线

```mermaid
xychart-beta
    title "moonshine-software/forty-five 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 30 --> 33
    line [32, 31, 31]
```

2026-10-18 32 → 2026-10-28 31（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d41380f3cbb9` · [字段定义](../../DATASET.md)*
