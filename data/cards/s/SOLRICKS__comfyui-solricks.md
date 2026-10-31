# SOLRICKS/comfyui-solricks

⭐ 14 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/SOLRICKS/comfyui-solricks) · [官网](https://solricks.com/en) · 组织维护

**ComfyUI 的视频/图像抗锯齿与细节增强节点包**

面向 ComfyUI 图像与视频工作流的自定义节点包，含三个节点：VideoTAADLAA（时间抗锯齿+抖动采样+DLAA 风格细化）、VideoDetailRefiner（轻量细节与纹理细化）、VideoAdaptiveAA（针对易锯齿区域的边缘清理）。实现基于 PyTorch 张量架构自行重写，不使用 NVIDIA 闭源 SDK 或原生 DLAA/DLSS 二进制。附带两个 1x 细化模型（保持原分辨率、非 ESRGAN、不做放大），提供游戏风格预设系统，经 ComfyUI Manager 验证，无需额外 Python 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VideoTAADLAA 结合时间抗锯齿、抖动采样与 DLAA 风格细化
- 附带 DLAANet 与 DLAATexture 两个 1x safetensors 细化模型
- 自适应边缘清理与运动感知清理（减少鬼影/拖尾）
- 轻量推理设计，ComfyUI 后处理场景低显存占用

## 适用场景

- 给 AI 生成的视频做抗锯齿与闪烁抑制后处理
- 细化发丝、布料、细线等微纹理细节
- 在 LTX/Wan 工作流末尾作为独立后处理节点使用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L12: Anti-aliasing and detail refinement nodes for ComfyUI image and video workflows. VideoTAADLAA combines temporal ant
> L96: 1. Install via **ComfyUI Manager** by searching for **SOLRICKS** or **Anti-Aliasing Pack**, or clone this repo into

## 星数曲线

```mermaid
xychart-beta
    title "SOLRICKS/comfyui-solricks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4f88552cf9d3` · [字段定义](../../DATASET.md)*
