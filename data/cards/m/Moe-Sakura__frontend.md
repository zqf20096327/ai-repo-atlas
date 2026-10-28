# Moe-Sakura/frontend

⭐ 27 · Vue · MIT · 推送 2026-09-04 · [GitHub](https://github.com/Moe-Sakura/frontend) · [官网](https://www.searchgal.top) · 个人维护 · 中文 README

**面向 Galgame 玩家的资源聚合搜索前端**

基于 Vue 3 + TypeScript + Tailwind CSS 的 Web 前端，通过 Cloudflare Workers API 聚合多个 Galgame 资源站点的搜索结果，以 SSE 流式实时展示进度与结果，并按资源获取方式自动标注标签（直接下载/需登录/BT 磁力等）。集成 VNDB 数据库展示游戏封面、截图与简介，简介由 AI Translation API 自动翻译为中文；附带 Artalk 评论系统、随机背景与 PWA 离线支持。安装需 Node.js 18+ 与 pnpm，支持 Vercel/Netlify/Cloudflare Pages 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合多个 Galgame 资源站点并以 SSE 流式展示搜索结果
- 按资源特性自动标注 11 类标签（直接下载/需登录/BT 磁力等）
- 集成 VNDB 游戏信息与 AI 自动翻译简介为中文
- PWA 可安装与离线访问，基于 Artalk 的评论系统

## 适用场景

- 一次搜索多个 Galgame 资源站点的游戏与补丁
- 查看游戏详情、截图并阅读中文翻译简介
- 通过标签筛选直接可下载或需登录的资源

## 场景标签

 · 领域:游戏资源搜索/前端应用

## 证据(README 行号)

> L14: - 🎮 **聚合搜索** - 整合多个 Galgame 资源站点的搜索结果
> L18: - 🤖 **AI 翻译** - 自动翻译游戏简介为中文

## 星数曲线

```mermaid
xychart-beta
    title "Moe-Sakura/frontend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `aac140477a88` · [字段定义](../../DATASET.md)*
