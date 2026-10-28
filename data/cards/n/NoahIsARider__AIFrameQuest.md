# NoahIsARider/AIFrameQuest

⭐ 24 · Vue · 推送 2026-08-10 · [GitHub](https://github.com/NoahIsARider/AIFrameQuest) · 组织维护 · 中文 README

**带多模态图像检索与 AI 审核的社区讨论平台**

基于 Flask + Vue 3 的全栈社区讨论平台，包含用户前端/后端与管理员前端/后端四部分。功能覆盖注册登录、多类别内容管理（动漫/影视/游戏等）、评论与五星评分、浏览计数。AI 相关能力包括 FAISS 图像相似度搜索、图像问答、文生图的多模态检索与图像上传请求，以及管理员侧对图片和评论的 AI 自动审核。部署需 MySQL 与 Node.js 环境，前后端分别启动，生产环境提供 Nginx 与 Waitress 配置说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- FAISS 图像相似度搜索与多模态（文搜图/图问答）检索
- 管理员侧对图片和评论的 AI 自动审核
- 用户端与管理端分离的完整全栈架构（Flask + Vue 3）

## 适用场景

- 搭建支持图片检索与评分的社区讨论站点
- 通过以图搜图或文字描述检索图像内容
- 用 AI 自动审核用户上传的图片与评论

## 场景标签

`多模态` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L52: - 💡 User module: image-based Q&A, text-to-image search (multimodal retrieval), and image upload requests
> L53: - 🛡️ Admin module: AI-powered automatic moderation of images and comments

## 星数曲线

```mermaid
xychart-beta
    title "NoahIsARider/AIFrameQuest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `be63d5030bdf` · [字段定义](../../DATASET.md)*
