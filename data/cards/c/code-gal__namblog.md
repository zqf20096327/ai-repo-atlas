# code-gal/namblog

⭐ 14 · JavaScript · GPL-3.0 · 推送 2026-01-23 · [GitHub](https://github.com/code-gal/namblog) · [官网](https://namblog.nigzu.com) · 个人维护 · 中文 README

**博客系统：Markdown 写作，由 AI 生成交互式网页**

基于 .NET + Vue 3 的自部署博客系统，写作时以 Markdown 为蓝图，提交后由 AI 生成带样式与交互的 HTML 页面（演示页、图表、代码演示等），每次提交生成新版本并可切换历史版本。提供 Web 编辑器、MCP 协议（接入 Cherry Studio、Claude Desktop 等 AI 客户端批量管理）、Obsidian 式文件夹监控同步三种管理方式。支持中英双语、PWA、SEO 预渲染，推荐 Docker 部署，本地开发需 .NET 10 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 按 prompt 将 Markdown 转为带样式交互的 HTML，保留版本历史
- MCP 协议接入 AI 客户端，支持创建/查询/批量管理文章等工具集
- Web 编辑器 / MCP / 文件夹监控三种内容管理途径
- 中英双语界面、PWA、SEO 预渲染、Docker 镜像多标签部署

## 适用场景

- 写博客时让 AI 把 Markdown 变成交互式演示网页
- 在 AI 客户端里通过对话批量管理博客文章
- 配合 Obsidian 本地写作并自动同步到博客

## 场景标签

 · 领域:博客/内容发布系统

## 证据(README 行号)

> L17: Focus only on content when writing your blog. Treat Markdown as a blueprint, and let AI agents transform it into HT
> L42: - Let AI generate HTML when submitting articles, customize style with prompts

## 星数曲线

```mermaid
xychart-beta
    title "code-gal/namblog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `f1cc6fe34c24` · [字段定义](../../DATASET.md)*
