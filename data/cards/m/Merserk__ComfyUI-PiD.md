# Merserk/ComfyUI-PiD

⭐ 132 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/Merserk/ComfyUI-PiD) · 个人维护

**ComfyUI 节点集：接入 NVIDIA PiD/PixelDiT 解码与放大**

面向 ComfyUI 用户的自定义节点集，使用 Comfy-Org/PixelDiT 原生模型加载方式运行 NVIDIA PiD（latent 条件化的像素扩散解码/放大器）。提供 10 个节点：单节点 PiD 解码、提示词/描述文本生成、基于本地 Qwen 的描述创建、兼容 KSampler 的采样捕获、原生 PiD 采样与图像转换、分块 2x-8x 放大，以及无需 VAE 的 PixelDiT 文生图。支持 Flux1/Flux2/SD3/SDXL/Qwen-Image 等骨干。安装需 git clone 到 custom_nodes 并安装依赖，要求 ComfyUI 0.28.0+、Python≥3.10、NVIDIA CUDA GPU（推荐）。模型权重采用 NVIDIA NSCLv1 许可，限于非商业研究/评估用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个 ComfyUI 节点覆盖 PiD 解码、采样、放大与 VAE-free 文生图
- 支持 Flux1/Flux2/SD3/SDXL/Qwen-Image 等多骨干，兼容性感知的选项过滤
- 分块 PiD 放大支持 2x/4x/6x/8x 输出
- 多数节点支持模型文件自动下载

## 适用场景

- 在 ComfyUI 工作流中对 Flux/SD3 等模型输出做 PiD 解码与 4K 放大
- 用 PixelDiT 节点做无 VAE 的像素空间文生图
- 用本地 Qwen 模型为图像生成 PiD 描述文本

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: Compact ComfyUI nodes for **NVIDIA PiD / PixelDiT** using ComfyUI-native `Comfy-Org/PixelDiT` model loading.
> L9: PiD is a latent-conditioned pixel diffusion decoder/upscaler:
> L49: |**PiD Decode**|`IMAGE`|One-node PiD decode from latent + caption + sigma.|

## 星数曲线

```mermaid
xychart-beta
    title "Merserk/ComfyUI-PiD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-18 132 → 2026-10-22 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `28c224ce34a7` · [字段定义](../../DATASET.md)*
