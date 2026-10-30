# baojudezeze/RMP-Adapter

⭐ 20 · Python · 推送 2026-03-13 · [GitHub](https://github.com/baojudezeze/RMP-Adapter) · 组织维护

**文本生成图像扩散模型的多概念定制适配器（推理代码+权重）**

RMP-Adapter 是面向文生图扩散模型（SD1.5 系列）的多概念定制方法实现：通过多提示适配器（MP-Adapter）从参考图提取像素级概念信息，再经区域去噪框架（RDF）控制各概念在生成图像中的位置与呈现。README 提供推理代码与预训练权重（训练脚本未发布），依赖自动下载 Realistic Vision V5.1、SD-VAE、Grounding-DINO、SAM 等基础模型，需手动下载适配器与 CLIP 权重，Python>=3.10、CUDA 12.1 环境。支持与 ControlNet 等插件组合使用，仅限学术研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提示适配器提取参考图像素级概念信息
- 区域去噪框架控制多概念在生成图中的位置
- 提供推理代码与预训练权重，训练脚本未发布
- 可与 ControlNet 等插件模块组合，兼容其他模型

## 适用场景

- 把多个人物/物品参考图合成进同一张生成图像
- 虚拟试穿：将服装概念叠加到人物图像
- 保持角色一致性的故事图像生成

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: 🎨 We propose an end-to-end multi-concept customization method, based on our RMP-Adapter pipeline: A Region-based Mul
> L5: ✨ What makes it cool? Our method leverages multiple prompt adapters (MP-Adapter) to extract pixel-level information 

## 星数曲线

```mermaid
xychart-beta
    title "baojudezeze/RMP-Adapter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8cb729c163c0` · [字段定义](../../DATASET.md)*
