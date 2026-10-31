# cocoalex00/Mamba2D

⭐ 19 · Python · 推送 2026-08-27 · [GitHub](https://github.com/cocoalex00/Mamba2D) · [官网](https://arxiv.org/abs/2412.16146) · 组织维护

**面向视觉任务的原生多维状态空间模型 PyTorch 实现**

论文 Mamba2D 的官方 PyTorch 实现：提出 M2D-SSM，用单一原生 2D 扫描替代对图像做 1D SSM 栅格化扫描的做法，token mixer 含 2D SSM 分支与局部分支并行。提供三种尺寸（N/T/S，7M–50M）的 ImageNet-1K 分类、MS-COCO 检测（Mask R-CNN）与 ADE20K 分割（UperNet）的预训练权重与配置，检测分割部分可拷贝 backbone 包接入 MMDetection/MMSegmentation。通过 uv 建立虚拟环境并安装 requirements.txt 运行，需自行下载 ImageNet 数据集。

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

- M2D-SSM 采用单一原生 2D 扫描处理多维数据
- 提供分类/检测/分割三种任务全尺寸预训练权重
- downstream/ 目录支持接入 MMDetection 与 MMSegmentation
- 更新后的 CUDA wavefront 核算降低峰值显存约 81%

## 适用场景

- 用 Mamba2D backbone 训练或微调视觉模型
- 在 MMDetection/MMSegmentation 中替换 backbone 做检测与分割
- 复现论文的 ImageNet/MS-COCO/ADE20K 实验结果

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: Mamba2D
> L21: State-Space Models (SSMs) have emerged as an efficient alternative to transformers, yet existing visual SSMs retain
> L23: We achieve state-of-the-art speed and accuracy across a range of tasks and model sizes. On ImageNet-1K classificati

## 星数曲线

```mermaid
xychart-beta
    title "cocoalex00/Mamba2D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5a2dec5bb975` · [字段定义](../../DATASET.md)*
