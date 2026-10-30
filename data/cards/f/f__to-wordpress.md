# f/to-wordpress

⭐ 16 · TypeScript · MIT · 推送 2026-05-29 · [GitHub](https://github.com/f/to-wordpress) · [官网](https://www.npmjs.com/package/to-wordpress) · 个人维护

**一条命令把静态站点/文档迁移为本地 WordPress 站**

Node.js CLI 工具 to-wordpress：检测 Jekyll/Hugo/Astro/WXR/Medium/DOCX 等 20 余种文本形来源，自动规划并生成本地 WordPress 站点，含经典 PHP 主题、站点插件、内容与媒体导入、URL 保留、验证与端点检查。通过 @wordpress/env 本地运行 WordPress，创意环节由 Claude Code（默认）、GitHub Copilot CLI 或 OpenAI Codex CLI 三种 agent 适配器驱动，各阶段走 attempt→test→fix 自动修复循环，并提供 Tune the Press 收尾流程。需 Node.js 20+、Docker 与一种 agent CLI；宿主机无需 PHP/Ruby/wp-cli。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 20 余种来源（SSG、WXR、Ghost、Medium/Substack、DOCX/PDF/EPUB 等）
- 三种 agent CLI 适配器：claude（默认）/copilot/codex
- attempt→test→fix 循环自动验证与修复，失败阶段由 agent 做修复
- 生成经典 PHP 主题、站点插件并保留原 URL，Jekyll 自定义插件传入插件阶段重建

## 适用场景

- 把 Jekyll/Hugo/Astro 博客整体迁移到 WordPress
- 将 Substack/Medium 导出或 DOCX/PDF/EPUB 文档批量建为 WordPress 站点
- 在本地 Docker 环境自动生成并验证可迁移的 WordPress 主题与插件

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L33: and uses one of three agent CLIs for the creative parts:
> L199: src/agents/     agent adapters: claude, copilot, codex

## 星数曲线

```mermaid
xychart-beta
    title "f/to-wordpress 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e6d9590d1fbc` · [字段定义](../../DATASET.md)*
