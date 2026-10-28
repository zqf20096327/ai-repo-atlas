# antoinehabis/Deep-ContourFlow

⭐ 20 · Python · MIT · 推送 2026-08-15 · [GitHub](https://github.com/antoinehabis/Deep-ContourFlow) · [官网](https://arxiv.org/abs/2407.10696) · 个人维护

**免训练主动轮廓图像分割库：冻结 CNN 特征驱动轮廓演化**

Python/PyTorch 图像分割库，面向需要无监督或单样本分割的开发者与科研用户。核心机制：以冻结的 ImageNet 预训练 CNN（VGG16/ResNet）多尺度特征作为轮廓能量，从圆形初始化演化出闭合轮廓，无需训练与标注数据；支持无监督前景提取与基于单张标注样例的 one-shot 模式，适用于自然图像与医学影像（皮肤镜、组织病理）。提供 pip 可编辑安装、Colab 笔记本及一条 make reproduce 命令复现基准（17,788 张图，约 3-4 小时单 GPU）。限制：GPU 结果因 cuDNN 自调优与混合精度存在约 ±0.01 IoU 波动。

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

- 无训练：冻结 VGG16/ResNet 骨干驱动轮廓演化，无需标注数据
- 两种模式：无监督分割与单张样例 one-shot 分割
- 适用于自然图像与医学影像（组织病理、皮肤镜）
- make reproduce 一条命令复现基准，配置固定、子集有随机种子

## 适用场景

- 在没有标注数据的情况下做前景/背景分割
- 医学影像（皮肤病灶、肿瘤区域）的单样本分割
- 复现论文基准或对比训练-free 分割方法

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L16: > **Deep ContourFlow (DCF)** segments objects by *evolving a contour* — like a classical active contour / snake — b
> L24: - **Training-free** — uses a frozen ImageNet backbone (VGG16 / ResNet). No fine-tuning, no labels, no dataset to co
> L26: - **Domain-agnostic** — works on natural images and medical imaging (histopathology, dermoscopy).

## 星数曲线

```mermaid
xychart-beta
    title "antoinehabis/Deep-ContourFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `eb239459a400` · [字段定义](../../DATASET.md)*
