# Eighonet/parking-research

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-06-18 · [GitHub](https://github.com/Eighonet/parking-research) · 组织维护

**论文代码库：深度学习停车位占用检测方法对比**

论文《Revising deep learning methods in parking lot occupancy detection》的官方代码仓库，研究停车位占用检测问题。实现两类方法：基于 patch 的分类（8 种 CNN 与 5 种 Vision Transformer 模型）与基于交叉区域的分类（Faster R-CNN、RetinaNet 多骨干组合）。提供 ACPDS、ACMPS、CNRPark、PKLot、SPKL 等数据集的预处理版本与标注结构，含自定义数据集的预处理与标注脚本。实验在 NVIDIA Tesla V100 GPU 上进行，代码基于 PyTorch 实现，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- patch 分类基线含 8 种 CNN 与 5 种 Vision Transformer 模型
- 交叉区域分类基线含 Faster R-CNN / RetinaNet 多骨干组合
- 提供 5 个停车位数据集的预处理版本与图像级视觉条件标注（11 类）
- 自定义数据集的预处理与标注工具（annotators widgets）

## 适用场景

- 复现论文中的停车位占用检测实验
- 在自有停车场图像数据上训练占用检测模型
- 比较 CNN 与 Vision Transformer 在该任务上的表现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Welcome to the research repo of the *''Revising deep learning methods in parking lot occupancy detection''* paper. H
> L70: In this study, we explored two approaches to the parking lot occupancy detection problem: patch-based classificatio
> L123: All baseline models are located in the `baselines` folder. All models are implemented using PyTorch and can be tra

## 星数曲线

```mermaid
xychart-beta
    title "Eighonet/parking-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `01d801925114` · [字段定义](../../DATASET.md)*
