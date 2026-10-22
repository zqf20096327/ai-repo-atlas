# astropuzzo/ComfyUI-MiniMax-H3-Image-Studio

⭐ 208 · Python · Unlicense · 推送 2026-09-30 · [GitHub](https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio) · [官网](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) · 个人维护

**ComfyUI 节点包：MiniMax H3 文生图与参考图编辑**

面向 ComfyUI 用户的 MiniMax H3 图像生成节点集：提供文生图与图像编辑两套模板工作流，支持多张参考图（最多九图）与可堆叠的 MiniMax H3 LoRA 适配器，文本/视觉编码器使用 Qwen3-VL 权重。机制上采样单帧 latent 并复用视频 VAE 解码技术（源自 Fizgig H3 Still），无需帧数选择或额外安装。README 自述仍属实验性：提示词遵循、身份保持与细节表现不稳定。需 ComfyUI 0.37.0 及以上，从 Manager 安装或克隆到 custom_nodes。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 文生图与图像编辑两套模板工作流，支持最多九张参考图
- 可堆叠的 MiniMax H3 LoRA 节点，无硬编码数量上限
- 单帧 latent 采样 + 视频 VAE 解码，无需帧数控制
- 只需三个模型文件即可启动（H3 模型、Qwen3-VL 编码器、视频 VAE）

## 适用场景

- 在 ComfyUI 中用 MiniMax H3 生成图像
- 用多张参考图做图像编辑（人物/姿势/背景组合）
- 挂载 LoRA 适配器调整生成风格或加速采样

## 场景标签

 · 领域:图像生成/ComfyUI 生态

## 证据(README 行号)

> L5: MiniMax H3 **text-to-image and image editing** in ComfyUI. Two starter workflows, one shared model setup, optional s
> L13: Use **ComfyUI 0.37.0 or newer**. Install Image Studio through ComfyUI Manager or clone this repository into `ComfyU

## 星数曲线

```mermaid
xychart-beta
    title "astropuzzo/ComfyUI-MiniMax-H3-Image-Studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 206 --> 209
    line [207, 208, 208]
```

2026-10-18 207 → 2026-10-22 208（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8a09f1490d7c` · [字段定义](../../DATASET.md)*
