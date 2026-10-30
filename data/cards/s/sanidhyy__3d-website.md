# sanidhyy/3d-website

⭐ 18 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/sanidhyy/3d-website) · [官网](https://web-3d.netlify.app) · 个人维护

**Three.js 3D T 恤定制器，可生成 AI 纹理**

基于 React、Three.js 与 Vite 的网页应用：在 3D 场景中定制 T 恤，支持改颜色、上传自定义 Logo，并通过 OpenAI DALL·E API（Netlify Function /api/v1/dalle）生成 AI 纹理贴图。OpenAI API key 经 AI Settings 存入 httpOnly 加密 cookie。本地运行需 Git 与 NodeJS，推荐用 npx netlify-cli dev 同时启动前端与 API；纯前端模式不含 AI 生图。面向开发者自行部署与二次开发。

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

- Three.js 3D 场景中定制 T 恤颜色与 Logo
- 经 Netlify Function 调用 DALL·E 生成 AI 纹理
- OpenAI API key 以加密 httpOnly cookie 存储

## 适用场景

- 在浏览器里 3D 预览并定制 T 恤样式
- 用 AI 生成的图案作为 T 恤纹理
- 作为 Three.js + OpenAI API 的学习/模板项目部署

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # A 3D AI Powered T-Shirt Customizer using Three.js
> L43: Customize T-Shirt
> L49: Ability to generate AI textures

## 星数曲线

```mermaid
xychart-beta
    title "sanidhyy/3d-website 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `208250e4a12a` · [字段定义](../../DATASET.md)*
