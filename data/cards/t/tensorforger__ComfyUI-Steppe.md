# tensorforger/ComfyUI-Steppe

⭐ 9 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/tensorforger/ComfyUI-Steppe) · 组织维护

**ComfyUI 潜空间生成式放大节点：图像视频 2×/4× 上采样与 2× 帧率**

面向 ComfyUI 用户提供的一组自定义节点，在 Wan 2.1 / Qwen-Image VAE 潜空间直接运行生成式上采样模型：单步生成放大后的 latent，由 VAE 直接解码，无需对基础模型做第二次去噪采样。支持图像与视频的 2× 分辨率、链式 4×、以及 latent 帧插值 2× 帧率；通过 hff 参数控制锐度，提供 200M 1-step、200M base、20M lite 三个模型，首次使用时自动从 Hugging Face 下载。附纯 PyTorch 的 steppe Python 包可脱离 ComfyUI 使用。不支持 Wan 2.2 5B VAE 及 FLUX/SD3/SDXL latent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单步生成式 latent 上采样，VAE 直接解码，无需二次采样
- 支持 2× 分辨率、链式 4×，以及 2× 帧率的 latent 帧插值
- hff 高频特征参数控制细节与锐度
- 提供独立于 ComfyUI 的纯 PyTorch steppe 包

## 适用场景

- 放大 Wan 2.1 / Qwen-Image 生成的图像到更高分辨率
- 将 Wan 2.1 视频同时放大分辨率并提升帧率
- 在 ComfyUI 工作流中替代 hires fix 的二次采样流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L11: **Steppe** is a family of *generative latent upscalers*: small generative models trained only for upscaling, which
> L17: - **One step**: about 45 ms for a 1024 px image with the default model. Most of the time goes to the VAE decode.
> L121: resolution. Steppe is a generative model itself: a window transformer on the full resolution latent grid generates


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `e96ae70cd1ae` · [字段定义](../../DATASET.md)*
