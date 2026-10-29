# ThetaCursed/ComfyUI-HiresFix-Ultra-AllInOne

⭐ 29 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/ThetaCursed/ComfyUI-HiresFix-Ultra-AllInOne) · 个人维护

**ComfyUI 高清修复一体化节点：放大+采样+色彩校正合一**

面向 ComfyUI 用户的高清修复（Hires Fix）自定义节点：将潜空间/模型放大、KSampler 采样、VAE 编解码与色彩还原合并为单个节点，替代 6+ 个节点的组合流程。提供深度直方图匹配以处理高去噪放大时的褪色问题，内置 Tiled VAE 编解码以降低显存占用，支持 ESRGAN/Real-ESRGAN 模型放大与 Bicubic/Bislerp 等潜空间方法，自动将分辨率对齐到 8 的倍数。通过 git clone 到 custom_nodes 目录安装，重启 ComfyUI 后使用。

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

- 单节点替代 VAE Encode、Latent Upscale、KSampler、VAE Decode、Color Match 等 6+ 节点
- Deep Histogram Matching 色彩校正，处理高去噪放大时的变灰/褪色
- 内置 Tiled VAE 编解码，支持中端 GPU 上放大至 4K 及以上
- 支持 ESRGAN/Real-ESRGAN 模型放大与 Bicubic/Bislerp 潜空间方法

## 适用场景

- 在 ComfyUI 工作流中一步完成 Stable Diffusion 图像的高清修复放大
- 放大时保持与低分辨率原图一致的色彩
- 显存受限时通过 Tiled VAE 完成高分辨率输出

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L7: This node simplifies your workflow by combining latent/model upscaling, sampling, and advanced color restoration int
> L11: * **📦 Unified Workflow:** Replaces 6+ nodes (VAE Encode, Latent Upscale, KSampler, VAE Decode, Color Match, etc.) w

## 星数曲线

```mermaid
xychart-beta
    title "ThetaCursed/ComfyUI-HiresFix-Ultra-AllInOne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `196da96494b9` · [字段定义](../../DATASET.md)*
