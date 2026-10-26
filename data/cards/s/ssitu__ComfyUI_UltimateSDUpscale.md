# ssitu/ComfyUI_UltimateSDUpscale

⭐ 1,581 · Python · GPL-3.0 · 推送 2026-06-22 · [GitHub](https://github.com/ssitu/ComfyUI_UltimateSDUpscale) · 个人维护

**ComfyUI 节点：以分块 img2img 方式放大图像**

将 Coyote-A 的 Ultimate Stable Diffusion Upscale 脚本实现为 ComfyUI 自定义节点，对大图执行分块（tiled）的 image-to-image 扩散过程，在保持扩散模型训练尺寸的同时改善放大图像的细节并降低硬件需求。面向 ComfyUI 用户，提供 git clone、ComfyUI Manager、comfy-cli 与手动下载四种安装方式，节点位于 image/upscaling 菜单，附带参数文档与示例工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分块 img2diffusion 放大，降低硬件需求
- 支持 git clone / ComfyUI Manager / comfy-cli / 手动下载四种安装方式
- 内置节点参数文档与示例工作流

## 适用场景

- 在 ComfyUI 中对大图做细节增强放大
- 显存有限时对高分辨率图像执行 img2img 处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # ComfyUI_UltimateSDUpscale
> L3: ComfyUI nodes for performing the image-to-image diffusion process on large images in tiles. This approach improves t

## 星数曲线

```mermaid
xychart-beta
    title "ssitu/ComfyUI_UltimateSDUpscale 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24", "2026-10-26"]
    y-axis "stars" 1573 --> 1582
    line [1574, 1577, 1578, 1579, 1581]
```

2026-10-18 1,574 → 2026-10-26 1,581（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `31f8bf2a4dcc` · [字段定义](../../DATASET.md)*
