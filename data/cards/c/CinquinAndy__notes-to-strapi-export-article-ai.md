# CinquinAndy/notes-to-strapi-export-article-ai

⭐ 20 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/CinquinAndy/notes-to-strapi-export-article-ai) · 个人维护

**将 Obsidian 笔记导出到 Strapi 的插件，带 AI frontmatter 与 SEO 处理**

Obsidian 社区插件，用于把 Markdown 笔记通过 Strapi API 导出为 CMS 内容：支持配置多条导出路由、按路由自定义字段映射（基于 OpenAPI schema）、多语言设置与图片（含图库）自动上传。AI 部分：调用 OpenAI API 生成 frontmatter、做 SEO 优化与内容分析，配置 OpenAI Token 为必填项，另有可选的 ForVoyez API 用于图片处理增强。安装需手动下载 release 文件放入插件目录，或克隆仓库 npm 构建开发版。3.0.0 版本经过完全重构，需重置配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多条导出路由与按路由自定义字段映射（OpenAPI schema）
- AI 生成 frontmatter、SEO 优化与内容分析
- 图片与图库自动上传到 Strapi
- 3.0.0 版本完全重构，需重启配置

## 适用场景

- 把 Obsidian 写作的笔记直接发布到 Strapi 站点
- 为不同内容类型（文章/页面/分类）配置不同导出路由
- 让 AI 自动生成 SEO 相关的 frontmatter 字段

## 场景标签

 · 领域:内容管理/写作工具

## 证据(README 行号)

> L7: Strapi Exporter is a game-changing Obsidian plugin that streamlines your content creation process by seamlessly expo
> L17: - 🤖 AI-Powered Content Processing
> L85: - (required) Add your OpenAI API Token

## 星数曲线

```mermaid
xychart-beta
    title "CinquinAndy/notes-to-strapi-export-article-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e386ab13c8aa` · [字段定义](../../DATASET.md)*
