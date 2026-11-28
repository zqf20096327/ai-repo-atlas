# Wither033/ComfyUI-MiniMaxH3-PixelHead

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Wither033/ComfyUI-MiniMaxH3-PixelHead) · [官网](https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead) · 个人维护

**ComfyUI 中 MiniMax-H3 视频的低显存像素解码头（预览版）**

以 ComfyUI 自定义节点形式提供的 MiniMax-H3 视频像素读取头：用 45.7 MiB BF16 的 ConvNeXt 单步解码器替代官方 2.68 GB 的 36 层 ViT3D Video VAE，在 NVIDIA L4 基准（384×256×22f）中位延迟 29.59 ms。README 明确标注为实验预览版：全局色彩、运动与平面图形可正常解码，但自然高频纹理与快速遮挡显著过平滑，不建议用于最终视频渲染，安装方式为克隆到 custom_nodes 并下载权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 45.7 MiB BF16 解码头替代 2.68 GB 官方 ViT3D Video VAE，基准显示 8.5× 速度提升
- 提供 ComfyUI 节点（Pixel Head Tap / Zero Video VAE 解码）与示例工作流
- README 按运动类型给出 PSNR/LPIPS 分项基准与已知问题清单

## 适用场景

- 在 ComfyUI 中对 MiniMax-H3 视频潜变量做低显存快速解码预览
- 生成草稿/调版阶段的快速视频回看（非最终渲染）
- 基于 FastFrames 训练工具自行训练或复现像素头

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: 3D video direct pixel readout head for **MiniMax-H3** in ComfyUI (`45.7 MiB` BF16 vs `2.68 GB` stock ViT3D Video VAE
> L44: 1. **`16×` larger pixel volume per DiT token**: 2D heads (`Qwen-Image 2.1`, `Krea-2`) reconstruct `16×16 = 256` pix
> L60: 1. Clone into `ComfyUI/custom_nodes` (or `comfy node install comfyui-minimaxh3-pixelhead`):


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `7b0d636c41e0` · [字段定义](../../DATASET.md)*
