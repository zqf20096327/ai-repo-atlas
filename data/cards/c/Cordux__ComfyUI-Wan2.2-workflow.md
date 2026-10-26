# Cordux/ComfyUI-Wan2.2-workflow

⭐ 66 · Unlicense · 推送 2026-01-26 · [GitHub](https://github.com/Cordux/ComfyUI-Wan2.2-workflow) · 个人维护

**低显存用户的 Wan 2.2 14B 文生视频/图生视频 ComfyUI 工作流**

面向 6GB 显存显卡用户的 ComfyUI 工作流文件：通过 GGUF 量化模型（befox rapid 合并版 Q3_K/Q4_K/Q5_K）、激进 CPU offload 与内存清理节点，在 RTX 3050 6GB 上以约 4.6 分钟生成 1 秒视频。支持文生视频与图生视频双模式一键切换、FPS×秒数自动算帧、末帧提取用于视频链式延长。需在 ComfyUI 中安装 9 个自定义节点包并从 Hugging Face 下载约 15GB 模型文件，最小系统内存 16GB。公共领域发布，无署名要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GGUF 量化 + CPU offload（约 9GB 卸载到内存）适配 6GB 显存
- t2v/i2v 双模式通过开关节点同时切换两条路径，无需手动重连
- FPS×Seconds 自动帧数计算（+1 帧适配 Wan 初始化）与末帧自动保存
- 4 步采样；RTX 3050 6GB 实测 1 秒视频约 4.6 分钟

## 适用场景

- 在 6-8GB 显存的消费级显卡上生成 Wan 2.2 视频
- 通过末帧提取把多段生成串联成更长视频
- 用输入图片驱动图生视频动画

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: Generate high-quality text-to-video and image-to-video content using Wan 2.2 14B on budget hardware!
> L13: - **GGUF Quantization** - Leverages quantized models for memory efficiency

## 星数曲线

```mermaid
xychart-beta
    title "Cordux/ComfyUI-Wan2.2-workflow 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-26"]
    y-axis "stars" 63 --> 67
    line [64, 65, 66, 66]
```

2026-10-18 64 → 2026-10-26 66（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `df9849e9ff20` · [字段定义](../../DATASET.md)*
