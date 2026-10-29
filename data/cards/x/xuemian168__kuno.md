# xuemian168/kuno

⭐ 79 · TypeScript · Apache-2.0 · 推送 2026-05-16 · [GitHub](https://github.com/xuemian168/kuno) · [官网](https://qut.edu.kg/) · 个人维护 · 中文 README

**面向多语言场景的轻量博客 CMS，Go + Next.js，Docker 部署**

全栈博客系统：Go 后端加 Next.js 前端，SQLite 存储，内置 Markdown 编辑器（支持 Mermaid 图表）、70+ 语言界面、分类标签管理、管理后台与 SEO 设置。提供 LLMs.txt 输出以适配 AI 搜索引擎。部署以 Docker 为主：一键脚本、Docker Compose、蓝绿部署（< 2s 停机）与健康检查自动回滚，也支持本地无 Docker 开发。默认管理员账号为 admin，需首次登录后修改密码。Apache 2.0 许可，由个人维护并标注 TikHub 赞助。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ 语言界面（next-intl 驱动的 i18n-first 设计）
- Markdown 编辑器带实时预览与 Mermaid 图表支持
- Docker 一键部署，蓝绿策略 < 2s 停机，失败自动回滚
- LLMs.txt 支持，面向 AI 搜索引擎的 SEO 输出

## 适用场景

- 搭建多语言个人或团队博客站点
- 通过 Docker 在服务器上一键部署并低停机升级 CMS
- 让博客内容被 AI 搜索引擎更好地抓取（LLMs.txt）

## 场景标签

 · 领域:内容管理/博客

## 证据(README 行号)

> L7: **KUNO** /ˈkuːnoʊ/ — a lightweight, i18n-first CMS built with Go and Next.js. The name comes from "坤" (kūn, earth in
> L24: - SEO optimization with LLMs.txt support for AI search engines

## 星数曲线

```mermaid
xychart-beta
    title "xuemian168/kuno 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-29 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `189cba5e8b8f` · [字段定义](../../DATASET.md)*
