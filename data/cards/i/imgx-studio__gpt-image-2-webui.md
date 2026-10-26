# imgx-studio/gpt-image-2-webui

⭐ 56 · TypeScript · 推送 2026-04-27 · [GitHub](https://github.com/imgx-studio/gpt-image-2-webui) · [官网](https://imgx.studio/) · 组织维护 · 中文 README

**自托管的 GPT Image / OpenAI 兼容文生图 WebUI**

基于 Next.js 16 + React 19 的图像生成 Web 前端，调用 GPT Image / OpenAI 兼容图像 API（含 gpt-image-2、gpt-image-1 模型选项），面向设计师、营销与产品团队。功能覆盖文生图、以图生图（最多 4 张参考图、单张 10MB）、尺寸/格式/背景控制、生成后选图迭代与 remix 操作。支持浏览器直连或服务器代理两种模式，密钥可存于浏览器 localStorage 或服务端环境变量。提供 9 种语言 UI，可部署到 Vercel 或 Node.js standalone；仓库当前未包含 License 文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生图与以图生图，最多 4 张 PNG/JPG/WEBP 参考图（单张 10MB）
- 1-4 张图像分次独立请求，降低批量上限导致的缺图
- 浏览器直连或 /api/images 服务器代理两种连接模式
- 9 种语言 UI 与各语言 README

## 适用场景

- 团队自托管一个文生图工作台，用自有 API 密钥生成产品图和广告视觉
- 上传产品照片做改图、变体与扩展，再从结果继续迭代
- 内部设计/营销团队在 Vercel 或自有服务器上部署使用

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: ImgX Studio is a premium WebUI for **GPT Image / OpenAI-compatible image APIs**. It helps designers, marketers, pro
> L47: - **Designed for gpt-image-2**: includes `gpt-image-2`, `gpt-image-2-2026-04-21`, and `gpt-image-1` model options.

## 星数曲线

```mermaid
xychart-beta
    title "imgx-studio/gpt-image-2-webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-26 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c414d6a933c6` · [字段定义](../../DATASET.md)*
