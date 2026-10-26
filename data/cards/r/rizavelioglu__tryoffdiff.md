# rizavelioglu/tryoffdiff

⭐ 152 · Python · NOASSERTION · 推送 2026-06-03 · [GitHub](https://github.com/rizavelioglu/tryoffdiff) · [官网](https://rizavelioglu.github.io/tryoffdiff/) · 个人维护

**从人物照片重建平铺服装图像的扩散模型（Virtual Try-Off）**

论文 TryOffDiff 与后续工作 MGT 的官方代码库：基于 Stable Diffusion-v1.4 微调的扩散模型，输入穿着服装的人物图像，生成该服装的平铺（packaged garment）图像，支持多件服装场景；使用 SigLIP 作图像编码器，评测依赖 IQA_PyTorch、clean-FID 与 DISTS-pytorch。提供训练、推理与评测脚本，模型与演示托管在 Hugging Face。面向计算机视觉研究与电商/时尚方向的开发者，许可证限制商用（除非完整开源）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Stable Diffusion-v1.4 的虚拟试脱（Try-Off）服装重建
- SigLIP 图像编码器
- 后续工作 MGT 扩展到多件服装场景
- 提供训练、推理与评测脚本

## 适用场景

- 从模特上身照生成服装平铺图用于商品展示
- 复现论文实验或在此模型上做研究
- 构建电商服装图像生成流水线的研究原型

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L6: 1. _"TryOffDiff: Virtual-Try-Off via High-Fidelity Garment Reconstruction using Diffusion Models"_,
> L41: Our code relies on PyTorch, with 🤗 Diffusers for diffusion model components

## 星数曲线

```mermaid
xychart-beta
    title "rizavelioglu/tryoffdiff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 151 --> 153
    line [152, 152]
```

2026-10-18 152 → 2026-10-26 152（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b89487e0e7c3` · [字段定义](../../DATASET.md)*
