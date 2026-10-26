# Faildes/Chattiori-Model-Merger

⭐ 53 · Python · 推送 2026-10-15 · [GitHub](https://github.com/Faildes/Chattiori-Model-Merger) · 个人维护

**Stable Diffusion/Flux 模型合并 CLI 工具：按用户设定比例融合权重**

面向 Stable Diffusion 系（SD1.x/2.x/XL）与 Flux.1 模型的检查点合并命令行工具，自动检测架构，支持 .ckpt 与 .safetensors。提供 20 余种合并模式（加权和、DARE、正交差分、稀疏 top-k、频段混合等），支持 2-3 模型合并、余弦结构模式（保留一模型结构注入另一模型细节）、块权重/元素级比率、VAE 写入、剪枝及 fp16/bf16/fp8/int8 保存。默认 CPU 运行，GPU 可选（需 VRAM 约等于模型大小），附带 Colab 快速开始流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 余种合并模式，含 DARE、正交差分、频段混合等
- 余弦结构模式：保留基准模型结构、注入其他模型细节
- 支持 SD1.x/2.x/XL/Flux.1/Z-Image/Anima 架构自动检测
- VAE 写入、剪枝、fp16/bf16/fp8/int8 精度保存与合并配方元数据

## 适用场景

- 把多个绘图基础模型按比例融合出新模型
- 在保留主体结构的前提下注入另一模型的细节风格
- 合并后剪枝并量化保存以减小模型体积

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: A fast, deterministic **checkpoint merger** for Stable Diffusion–family models (SD1.x/2.x/XL) and **Flux.1** (auto-d
> L4: Supports **`.ckpt`** and **`.safetensors`**. Runs on **CPU by default** (GPU optional).

## 星数曲线

```mermaid
xychart-beta
    title "Faildes/Chattiori-Model-Merger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `cdf9a9ad5469` · [字段定义](../../DATASET.md)*
