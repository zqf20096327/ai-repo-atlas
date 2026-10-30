# jidohyun/NOD

⭐ 18 · JavaScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/jidohyun/NOD) · [官网](https://nod-archive.com) · 个人维护

**个人链接收藏库：浏览器扩展保存网页，Web 端管理链接**

由 Manifest V3 浏览器扩展与 Web 应用组成的个人链接库：扩展保存当前页面，登录用户可在 Web 端浏览、搜索、打开、删除已存链接。当前阶段仅存储 URL、标题、来源与保存时间，不收集正文也不做 AI 分析；项目描述中的知识差异分析是规划方向。实现基于 Cloudflare Worker 与 D1 数据库，前端为原生 HTML/CSS/JS，需 Bun 与 Node.js 22+ 本地运行，远程部署尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Manifest V3 扩展保存当前页面，Web 端浏览/搜索/删除链接
- 阶段一仅存 URL、标题、来源、时间四项元数据
- Cloudflare Worker + D1 后端，原生 HTML/CSS/JS 前端

## 适用场景

- 在浏览器中一键保存网页链接做个人收藏
- 跨设备搜索和管理个人链接库
- 以轻量自托管方式记录阅读过的页面

## 场景标签

 · 领域:个人知识管理/浏览器工具

## 证据(README 行号)

> L3: NOD is a personal link library. Its Manifest V3 browser extension saves the current page, and the web app lets each 
> L5: Phase 1 stores only the URL, title, source, and saved time. It does **not** collect article bodies or run AI analysi

## 星数曲线

```mermaid
xychart-beta
    title "jidohyun/NOD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 low · 依据 README sha `3a5f55e45e5a` · [字段定义](../../DATASET.md)*
