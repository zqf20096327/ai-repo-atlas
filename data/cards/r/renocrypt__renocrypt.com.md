# renocrypt/renocrypt.com

⭐ 14 · Astro · 推送 2026-08-24 · [GitHub](https://github.com/renocrypt/renocrypt.com) · [官网](https://www.renocrypt.com/) · 个人维护

**个人博客网站源码：关于机器学习与工程的静态写作站**

renocrypt.com 的源码仓库：基于 Astro 5 的静态站点（无运行时服务器），内容为机器学习/AI 写作与工程笔记两类 MDX 集合，配 KaTeX 数学公式、Shiki 语法高亮、RSS 与 sitemap，主题 token 支持昼夜切换。通过 GitHub Actions 构建并发布到 GitHub Pages，绑定自定义域名。本地开发需 Node 24，用 npm 安装依赖后运行 dev 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Astro 5 静态生成，无运行时服务器、无主题子模块
- MDX 内容集合（posts 写作 / dev 工程笔记）配 KaTeX 与 Shiki
- GitHub Actions 自动构建发布到 GitHub Pages，自定义域名强制 HTTPS
- Tailwind CSS 4 主题 token，昼夜双主题

## 适用场景

- 查看或复用 renocrypt.com 站点的构建配置与结构
- 本地跑起站点预览或写文章
- 参考 Astro + Tailwind + MDX 的静态博客工程组织方式

## 场景标签

 · 领域:博客/静态站点

## 证据(README 行号)

> L3: > The source for **renocrypt.com**, a writing site on machine learning, AI, and engineering, published under the *Ma
> L17: - **Content collections** (`src/content.config.ts`): `posts` (ML/AI writing) and `dev` (engineering notes)

## 星数曲线

```mermaid
xychart-beta
    title "renocrypt/renocrypt.com 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2650ea5326b1` · [字段定义](../../DATASET.md)*
