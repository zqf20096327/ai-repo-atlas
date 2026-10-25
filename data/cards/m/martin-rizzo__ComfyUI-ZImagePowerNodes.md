# martin-rizzo/ComfyUI-ZImagePowerNodes

⭐ 368 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/martin-rizzo/ComfyUI-ZImagePowerNodes) · 个人维护

**面向 Z-Image/Z-Image Turbo 模型的 ComfyUI 自定义节点集**

一套专为 Z-Image / Z-Image Turbo 文生图模型开发的 ComfyUI 自定义节点：包含 Z-Sampler Turbo 采样器（Intensity、Turbo Creativity 潜空间扰动等参数）、带 100+ 预设风格的 Style Prompt Encoder、软重绘用 VAE 编码器、CivitAI 兼容元数据图片保存等节点。给使用 ComfyUI 运行 Z-Image 模型的用户安装使用，最低要求 ComfyUI v0.14、PyTorch 2.5、Python 3.10。README 同时列出 INT8-ConvRot、GGUF、FP8、BF16 等量化格式的推荐模型文件及放置目录，并附带参考工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Z-Sampler Turbo 节点：低步数（3 步起）保持构图一致，支持 Intensity/Intensity Bias 参数
- Turbo Creativity 通过潜空间扰动增加不同 seed 间的构图多样性
- Style Prompt Encoder 内置 100+ 预设视觉风格，可搜索缩略图画廊浏览
- 保存图片时可嵌入 CivitAI 兼容元数据，便于分享生成参数与工作流

## 适用场景

- 在 ComfyUI 中运行 Z-Image Turbo 生成图像并控制风格与一致性
- 低步数快速试错提示词后再提高步数出高质量图
- 做 Z-Image 的软重绘（soft inpainting）并保存带元数据的作品到 CivitAI

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: **Z-Image Power Nodes** is a collection of nodes designed specifically for the Z-Image / Z-Image Turbo model, they a
> L67: * __⚡Z-Sampler Turbo v2 (Simple)__

## 星数曲线

```mermaid
xychart-beta
    title "martin-rizzo/ComfyUI-ZImagePowerNodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 367 --> 370
    line [368, 369]
```

2026-10-18 368 → 2026-10-25 369（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `bea46394b970` · [字段定义](../../DATASET.md)*
