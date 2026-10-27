# rohit901/cooperative-foundational-models

⭐ 84 · Python · MIT · 推送 2026-01-02 · [GitHub](https://github.com/rohit901/cooperative-foundational-models) · [官网](https://rohit901.github.io/coop-foundation-models/) · 个人维护

**科研论文官方代码：用 CLIP/SAM 将闭集检测器变为开集检测**

WACV 2025 论文 "Enhancing Novel Object Detection via Cooperative Foundational Models" 的官方 PyTorch 代码。提出免训练的协作机制，利用预训练基础模型 CLIP（SigLIP）与 SAM 的互补能力，把闭集检测器（Mask-RCNN）转换为开集检测器，可定位并分类已知与新颖类别物体；还可与 GDINO 等开集检测器组合。在 LVIS 与 COCO OVD 基准上报告结果，并提供自定义图像的 LVIS 1203 类推理脚本。复现需自行下载 COCO2017/LVIS 数据集与预训练权重，经 conda 环境安装运行。

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

- 免训练、模块化机制，可组合替换各组件
- 将任意闭集检测器转换为开集检测器
- 提供 LVIS 1203 类词汇的自定义图像推理脚本
- 在 LVIS 与 COCO OVD 基准报告 mAP 结果

## 适用场景

- 复现论文中的新颖物体检测与开放词汇检测结果
- 对自定义图像运行 LVIS 词汇的零样本目标检测
- 把已有的 Mask-RCNN 闭集检测器改造成开集检测器

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L24: > **Abstract:** *In this work, we address the challenging and emergent problem of novel object detection (NOD), foc
> L30: - We propose a simple, modular, and training-free approach which can detect (i.e. localize and classify) known as w

## 星数曲线

```mermaid
xychart-beta
    title "rohit901/cooperative-foundational-models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-27 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a84e80dc9d47` · [字段定义](../../DATASET.md)*
