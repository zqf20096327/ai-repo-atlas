# edshkim98/LocalDiffusion-Hallucination

⭐ 28 · Python · 推送 2026-07-03 · [GitHub](https://github.com/edshkim98/LocalDiffusion-Hallucination) · 个人维护

**科研代码：免训练的局部扩散框架，降低图像翻译中的结构幻觉**

ECCV 2024 Oral 论文 'Tackling Structural Hallucination in Image Translation with Local Diffusion' 的官方实现。面向计算机视觉与医学影像研究者，提供一种 training-free 推理框架：先用 PatchCore（或 MRI 分割网络）检测条件图像中的 OOD 区域，再将反向扩散拆为仅以 OOD 区域为条件的分支与仅以 IND 区域为条件的分支，最后按 OOD 掩码融合。方法插入已冻结的预训练扩散模型，无需重训练。论文报告在医学与自然图像数据集上分别降低误诊 40% 与 25%。以 PyTorch 源码与 YAML 配置提供，需自行训练基准扩散模型，新数据集需重新校准 OOD 阈值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OOD 检测 + 双分支反向扩散 + 掩码融合的三阶段推理流程
- training-free：直接作用于冻结的预训练扩散模型，无需重训练
- 支持 MNIST/BRATS/MVTec 三类实验，MNIST 演示开箱即用（数据随仓库附带）
- YAML 配置开关可退化为原版条件扩散基准

## 适用场景

- 医学影像（如未见肿瘤）翻译时抑制结构幻觉以降低误诊风险
- 在 OOD 样本上复现论文的局部扩散实验
- 作为免训练方案插入已有的预训练条件扩散模型

## 场景标签

`图像生成` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L12: A **training-free** diffusion framework that reduces *structural hallucination* when translating out-of-distributio
> L37: The pipeline has three stages, applied entirely at inference time on top of a frozen, pre-trained diffusion model:
> L41: |**1. OOD detection**|A PatchCore anomaly detector (or, optionally, a pre-trained segmentation network for MRI) sco

## 星数曲线

```mermaid
xychart-beta
    title "edshkim98/LocalDiffusion-Hallucination 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b7d1f1f2e551` · [字段定义](../../DATASET.md)*
