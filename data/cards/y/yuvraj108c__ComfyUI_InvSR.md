# yuvraj108c/ComfyUI_InvSR

⭐ 263 · Python · NOASSERTION · 推送 2026-06-05 · [GitHub](https://github.com/yuvraj108c/ComfyUI_InvSR) · 个人维护

**ComfyUI 图像超分节点：封装 InvSR 扩散反演超分模型**

将 InvSR（基于扩散反演的任意步数图像超分）封装为 ComfyUI 自定义节点的项目。安装方式为在 custom_nodes 目录 git clone 后 pip 安装依赖；Diffusers 模型（sd-turbo）与 InvSR 权重首次使用时自动下载。提供 num_steps、cfg、chopping_size 等参数控制推理步数、引导强度与大幅图像分块处理，针对显存有限场景给出 chopping_batch_size=1 的设置说明。面向使用 ComfyUI 的图像生成/处理用户，License 为 NTU S-Lab License 1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 InvSR 任意步数扩散反演超分为 ComfyUI 节点
- Diffusers 模型与 InvSR 权重自动下载
- chopping 参数支持 1k→4k 大图分块与低显存处理
- 支持 noise_predictor_sd_turbo_v5 与 diftune 两个权重版本

## 适用场景

- 在 ComfyUI 工作流中对图像做超分辨率放大
- 显存有限时通过分块参数处理大尺寸图像
- 可调步数在超分质量与速度间设置

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L4: This project is a ComfyUI wrapper for InvSR (Arbitrary-steps Image Super-resolution via Diffusion Inversion)
> L36: - Diffusers model (stabilityai/sd-turbo) will download automatically to `ComfyUI/models/diffusers`

## 星数曲线

```mermaid
xychart-beta
    title "yuvraj108c/ComfyUI_InvSR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 261 --> 264
    line [262, 263, 263]
```

2026-10-18 262 → 2026-10-25 263（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `effba6991959` · [字段定义](../../DATASET.md)*
