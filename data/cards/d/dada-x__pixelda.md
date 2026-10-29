# dada-x/pixelda

⭐ 17 · SCSS · 推送 2025-11-12 · [GitHub](https://github.com/dada-x/pixelda) · 个人维护 · 中文 README

**AI 生成像素风游戏素材（图片/动画/音乐）的 Web 平台**

由 FastAPI 后端与 Angular 前端组成的 Web 平台，面向 2D 像素风游戏开发者：通过自定义提示词调用通义（Tongyi/DashScope）与豆包（Doubao/Volcano）的模型生成图像、由首帧图生成视频动画、拆分动画帧供精灵图使用，并用 rembg 去除帧背景、生成背景音乐，附带缓存与生成历史。各模型按量计费（如 0.2 元/图）。需自行搭建前后端运行，前置 Python 3.13、Node.js 22、Angular 20。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用通义/豆包模型生成像素风图像与提示词驱动动画
- 动画帧拆分与预览，供 2D 精灵图使用
- rembg 去除帧背景（beta）
- 背景音乐与音轨生成

## 适用场景

- 为我的像素风游戏生成角色/素材图片
- 把首帧图扩展成精灵动画并拆帧导出
- 给游戏生成配套背景音乐

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L4: PiXelDa is an AI-powered platform designed for generating pixel-art game assets, including images and animations, us
> L151: |Image Generation|Doubao|doubao-seedream-4-0-250828|0.2 RMB/image|

## 星数曲线

```mermaid
xychart-beta
    title "dada-x/pixelda 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `992b050b9b7a` · [字段定义](../../DATASET.md)*
