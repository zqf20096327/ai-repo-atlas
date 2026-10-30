# BennyDaBall930/ComfyUI-Latent-Tiled-PiD

⭐ 18 · Python · MIT · 推送 2026-08-28 · [GitHub](https://github.com/BennyDaBall930/ComfyUI-Latent-Tiled-PiD) · 个人维护

**ComfyUI 原生节点包：对生成潜空间切片做 NVIDIA PiD 平铺解码至最高 244MP**

两个原生 ComfyUI 节点加一个 QA 节点：Size Picker 以下拉菜单提供 56 个（FLUX.2 通道 55 个）端到端渲染测试过的尺寸预设；Decode 节点夹在 KSampler 与 SaveImage 之间，将生成潜空间切成重叠瓦片，逐块以 PiD 蒸馏 4 步调度解码，经升余弦羽化混合像素，输出分辨率恒为潜空间的 4 倍，实测至 244MP。支持 Krea 2 Turbo（qwen 系）与 FLUX.2 Klein 4B/9B、FLUX.1/Z-Image-Turbo 通道；sd3/sdxl 路径存在但未测试。QA 节点输出中间调色度增量与阴影偏绿判定。限制：max_tile 固定 1024，PiD 权重与部分上游模型为非商业许可。

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

- 对生成潜空间（而非解码后像素）切片的平铺 PiD 解码，输出恒为潜空间 4 倍
- 56 个渲染测试过的尺寸预设，覆盖 9 种长宽比，实测至 244MP（15616x15616）
- 支持 Krea 2 Turbo / FLUX.2 Klein 4B、9B / FLUX.1 Z-Image-Turbo 通道
- 内置 QA 节点：输出色度增量与阴影偏绿指标，按阈值判定

## 适用场景

- 在 ComfyUI 中将扩散模型输出放大到 33MP–244MP 的大幅面图像
- 避开 PiD 单次解码超出 1024→4096 训练包络时的色调崩塌
- 新分辨率或新模型组合下用 QA 节点验证解码质量

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L8: Latent-native tiled decoding for NVIDIA PiD
> L9: (Pixel Diffusion Decoder, arXiv:2605.23902) as native ComfyUI
> L55: ### Latent-Tiled PiD Size Picker

## 星数曲线

```mermaid
xychart-beta
    title "BennyDaBall930/ComfyUI-Latent-Tiled-PiD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `095fbb5935f3` · [字段定义](../../DATASET.md)*
