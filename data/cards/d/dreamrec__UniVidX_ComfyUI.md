# dreamrec/UniVidX_ComfyUI

⭐ 81 · Python · GPL-3.0 · 推送 2026-05-11 · [GitHub](https://github.com/dreamrec/UniVidX_ComfyUI) · [官网](https://houyuanchen111.github.io/UniVidX.github.io/) · 个人维护

**ComfyUI 自定义节点包：本地运行 UniVidX 视频本征/Alpha 分解**

为 ComfyUI 提供五个节点（Loader/TaskMode/Sampler/Decode/Save）以运行 UniVidX（SIGGRAPH 2026）14B 视频扩散模型，将视频片段分解为 RGB/Albedo/Irradiance/Normal（本征变体）或 Alpha matte/前景/背景（alpha 变体），共 30 种任务模式。底层依赖 Wan2.1-T2V-14B，支持 FP8 预量化与 lightx2v 蒸馏加速，附 21 帧分块的 chunked 采样器处理长视频。硬件门槛高：需 CUDA 8.0+ 显卡，FP8 路径 VRAM ≥24 GB、BF16 ≥32 GB，磁盘约 85 GB；RTX 5090 上单 21 帧分块 FP8 约 9.43 分钟，非实时处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五节点拖放式工作流覆盖 30 种任务模式（本征与 alpha 两变体）
- FP8 预量化路径与 lightx2v 蒸馏加速（RTX 5090 上 4.59 min/chunk 预览）
- chunked_clip_sampler 将长视频切分为 21 帧重叠窗口并跨模态拼接输出
- 逐 GPU 兼容性表格与实测性能/PSNR 质量矩阵

## 适用场景

- 无绿幕环境下从任意视频片段抠除 VFX alpha matte
- 通过交换 irradiance 通道对视频重新打光
- 为 3D 重建或其他视频模型生成 normal/albedo 条件图

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L12: ComfyUI custom nodes for UniVidX (SIGGRAPH 2026): unified video diffusion that decomposes a clip into **RGB / Albed
> L55: **Strategy A wrapper** — UniVidX's official pipeline runs as an opaque black box. The four output IMAGE batches bec
> L59: - You specifically need **intrinsic** (RGB / Albedo / Irradiance / Normal) or **alpha** (matte / fg / bg) decomposi

## 星数曲线

```mermaid
xychart-beta
    title "dreamrec/UniVidX_ComfyUI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 80 --> 83
    line [82, 81, 81]
```

2026-10-18 82 → 2026-10-31 81（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4dc81eb9d8fc` · [字段定义](../../DATASET.md)*
