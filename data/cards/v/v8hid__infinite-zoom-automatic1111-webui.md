# v8hid/infinite-zoom-automatic1111-webui

⭐ 670 · Python · MIT · 推送 2026-02-08 · [GitHub](https://github.com/v8hid/infinite-zoom-automatic1111-webui) · 个人维护

**SD WebUI 扩展：用 outpainting 生成无限缩放效果视频**

面向 AUTOMATIC1111 与 Vladmandic 版 Stable Diffusion WebUI 的扩展，通过稳定扩散外绘（outpainting）方法生成无限缩放效果视频。工作流程分三步：生成或上传初始图像；按设定步数迭代外绘（将已有图缩小置于画布中心并在空白处生成新图）；在各步之间插值生成渐变缩放帧。帧数由 Zoom Speed 与 Frames per second 参数决定。通过 WebUI 扩展 URL 安装，另提供可在免费 Colab 上运行的版本。README 提示使用 Inpainting 模型可获得结果，Mask Blur 建议设为 0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 outpainting 的无限缩放视频生成
- 支持自定义初始图像或按提示词生成初始图像
- 通过 Zoom Speed 与 FPS 参数控制缩放帧数与时长
- 提供可在免费 Colab 计划上运行的独立版本

## 适用场景

- 为 Stable Diffusion WebUI 用户生成无限缩放动画视频
- 用自己的初始图像制作渐变缩放外绘视频
- 无本地环境时用 Google Colab 免费运行

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: This is an extension for the AUTOMATIC1111's (and Vladmandic´s) webui that allows users to create infinite zoom effe
> L67: Once you have your initial image, the program will start generating outpaint steps. The number of outpaint steps is

## 星数曲线

```mermaid
xychart-beta
    title "v8hid/infinite-zoom-automatic1111-webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 669 --> 671
    line [670, 670]
```

2026-10-18 670 → 2026-10-26 670（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `be0468a0c1ac` · [字段定义](../../DATASET.md)*
