# kuschanow/ComfyUI-Advanced-Latent-Control

⭐ 23 · Python · 推送 2026-08-11 · [GitHub](https://github.com/kuschanow/ComfyUI-Advanced-Latent-Control) · 个人维护

**ComfyUI 潜空间操作自定义节点包，供生图工作流使用**

ComfyUI 的自定义节点扩展，提供对 latent 的多种变换：镜像翻转并合并、沿 x/y 轴位移、乘法缩放，以及 Latent add/interpolate 等节点；TSampler (Latent Control) 将变换与采样结合，Offset 机制可按步数模式（如 0 0 0 1）周期性触发变换，各变换节点均有一次性版本。Latent normalize 通过 VAE 顺序解码/编码修复潜空间被大幅修改后采样劣化的问题。Transform hijack 通过 sampler post-CFG 钩子把变换挂到克隆模型上，兼容任意采样器；3.0.0 起改为接收/返回 MODEL 以避免 monkey-patch 冲突。面向 Stable Diffusion 生图工作流搭建者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Latent 镜像/位移/乘法等变换节点及组合变换
- Offset 按 process_every/skip_every 模式周期性应用变换，可组合叠加
- Latent normalize 经 VAE 重编码修复被修改 latent 的采样劣化
- Transform hijack 经 post-CFG 钩子将变换挂接模型，兼容任意采样器

## 适用场景

- 在生图工作流中对潜空间做翻转、位移等变换实验
- 按步数规律性施加变换以生成图案化效果
- 潜空间被大幅修改后修复采样质量

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **This custom nodes helps to transform latent in different ways.**
> L44: ## TSampler (Latent Control)

## 星数曲线

```mermaid
xychart-beta
    title "kuschanow/ComfyUI-Advanced-Latent-Control 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3435e539edde` · [字段定义](../../DATASET.md)*
