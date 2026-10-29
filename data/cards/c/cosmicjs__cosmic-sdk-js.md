# cosmicjs/cosmic-sdk-js

⭐ 18 · TypeScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/cosmicjs/cosmic-sdk-js) · [官网](https://www.cosmicjs.com/docs) · 组织维护

**Cosmic 无头 CMS 的官方 JavaScript SDK，取内容、管媒体并调用 AI 生成**

面向 Cosmic 无头 CMS 平台的官方 TypeScript 客户端库：以 Bucket slug 与 read/write key 认证，在 Next.js、Node.js 18+ 和浏览器中读取与增删改内容对象、批量操作、管理媒体库（含 imgix 图片 URL）、内容模型与版本修订；附带 AI 接口，凭 writeKey 生成文本（支持流式）、图像、视频和音频，生成文件保存进媒体库。零运行时依赖，返回类型化结果，可选安装 @cosmicjs/rich-text 渲染富文本块。write key 不可暴露在客户端代码中。

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

- 对象 CRUD、批量操作（单次最多 25 个）与游标分页等链式查询
- 媒体库上传/列表/删除，上传图片含 imgix_url 供裁剪优化
- AI 接口生成文本（流式）/图像/视频/音频，生成文件存入媒体库
- TypeScript 类型化结果，零运行时依赖，支持 Next.js/Node 18+/浏览器

## 适用场景

- 在 Next.js 或 Node 应用中读取 Cosmic 管理的内容并渲染页面
- 通过 SDK 上传和管理媒体文件并获取 CDN URL
- 在内容工作流中直接调用文本与图像生成并把结果存入媒体库

## 场景标签

 · 领域:内容管理/无头 CMS

## 证据(README 行号)

> L21: Cosmic is a headless CMS with a dashboard for creating content and an API for delivering it to any website or appli
> L241: Generate text, images, video, and audio. Requires a `writeKey`. [see docs]
> L7:  The official client for Cosmic. Fetch content, manage media, and generate AI in Next.js, Node, and the browser.

## 星数曲线

```mermaid
xychart-beta
    title "cosmicjs/cosmic-sdk-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1d9ca81f7975` · [字段定义](../../DATASET.md)*
