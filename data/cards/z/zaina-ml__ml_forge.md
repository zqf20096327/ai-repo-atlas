# zaina-ml/ml_forge

⭐ 427 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/zaina-ml/ml_forge) · 个人维护

**可视化节点编辑器：拖拽搭建并训练 PyTorch 图像分类模型**

面向不写代码用户的桌面端可视化 PyTorch 流水线编辑器：在画布上拖拽节点、连线，按 Data Prep→Model→Training 三个标签页组装数据预处理、网络层（Linear/Conv2D/BatchNorm 等）与训练流程，由工具生成并运行训练代码。支持实时 loss 曲线、checkpoint、早停、推理（top-k 预测）与训练指标摘要，可导出独立可运行的 train.py。限制：需预装 PyTorch 2.0+（不作为依赖安装），支持 CUDA/MPS/CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽节点连线生成并运行 PyTorch 训练代码
- 三标签页工作流：数据准备→模型→训练
- 训练后推理与指标面板（最终 loss、最佳验证精度、曲线）
- 导出无需 ML Forge 即可运行的独立 train.py

## 适用场景

- 不会写代码的用户想训练 MNIST/CIFAR 等图像分类模型
- 教学场景中可视化理解神经网络结构与训练流程
- 搭建原型后导出 PyTorch 代码继续开发

## 场景标签

 · 领域:机器学习/计算机视觉

## 证据(README 行号)

> L5: A visual PyTorch pipeline editor. Build, train and run image classification models without writing code.
> L17: - **Visual pipeline** - drag nodes onto a canvas, connect them with wires, and ML Forge generates and runs the trai

## 星数曲线

```mermaid
xychart-beta
    title "zaina-ml/ml_forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 425 --> 428
    line [426, 427, 427]
```

2026-10-18 426 → 2026-10-24 427（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f2b1c85397e1` · [字段定义](../../DATASET.md)*
