# fictiontribe/galley

⭐ 4 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/fictiontribe/galley) · [官网](https://galleycms.com) · 组织维护

**面向静态站点的开源 AI CMS，Astro 优先，提示—校对—发布**

Galley 是一个面向静态站点（Astro 优先）的开源 CMS：内容存于 git 仓库，用户可通过表单、页面内编辑或 AI 助手（使用自己的 Anthropic Claude key）修改内容，所有改动在实时预览旁逐字段校对后以 git commit 或 pull request 发布，无数据库、无账号。还提供 MCP server 供 Claude Desktop/Claude Code/Cursor 等 MCP 客户端调用同等工具、AI 检查、表单提交、重定向管理、WordPress 迁移等功能。以 npm 包发布，另有 Tauri 2 桌面应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种编辑入口（表单/页面/助手）统一汇入 Proof 校对流程
- 发布即 git commit/push，撤销为 git revert，无数据库
- 内置 MCP server（galley mcp）向任意 MCP 客户端暴露工具
- 识别 Astro/Docusaurus/Nuxt/Next.js/SvelteKit/Eleventy/Hugo/Jekyll 等框架约定

## 适用场景

- 给 Astro 等静态站点配一个 git-based 内容编辑后台
- 通过 AI 助手或 MCP 客户端修改站点文案并逐条校对
- 从 WordPress 迁移内容到静态站点
- 为客户管理多个站点并以 pull request 提交改动

## 场景标签

 · 领域:Web 开发/内容管理

## 证据(README 行号)

> L29: Galley opens a site whose content lives in git and lets anyone change it — in
> L64:  on the page, retyped in the live preview; or the assistant (Anthropic's
> L97: - **Your own AI tool.** An MCP server gives Claude Desktop, Claude Code,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c43e04635580` · [字段定义](../../DATASET.md)*
