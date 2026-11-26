# Chunling1/OpenBIM-FloorPlan-AI

⭐ 10 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Chunling1/OpenBIM-FloorPlan-AI) · [官网](https://github.com/Chunling1/OpenBIM-FloorPlan-AI) · 个人维护 · 中文 README

**将建筑平面图分割为墙/窗/门的深度学习工具，面向建筑与BIM从业者**

系统将 2D 建筑平面图（图片/扫描 PDF）转换为结构化语义数据，识别墙体、窗户、门三类构件。基于 UNet+ResNet34，在 CubiCasa5K 上 mIoU 为 0.787，并针对黑底 CAD 施工图做域适应训练。提供 FastAPI Web 服务、浏览器端像素标注工具、ONNX CPU 推理（单张 <1.5s）、分割结果转 IFC 文件及基于度日数法的建筑能耗计算。支持三个模型变体与自定义数据集训练，需从 GitHub Releases 手动下载权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UNet+ResNet34 分割墙体/窗户/门三类构件，CubiCasa5K mIoU 0.787
- ONNX Runtime CPU 推理，无需 GPU，单张推理 <1.5s
- 内置浏览器端语义标注工具，标注保存为 .npy
- 分割 Mask 可自动转换为 IFC 2x3 BIM 文件

## 适用场景

- 把扫描的建筑平面图批量转成结构化构件数据用于 BIM 建模
- 对黑底 CAD 施工图做墙体门窗识别
- 标注自己的平面图数据集来微调模型
- 根据分割出的几何信息估算建筑能耗 EUI

## 场景标签

`目标检测` `微调` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L17: **OpenBIM FloorPlan AI** 是一个将 2D 建筑平面图（图片/扫描 PDF）自动转换为结构化语义数据的深度学习系统。系统自动识别 **墙体、窗户、门** 三大建筑构件，支持后续 BIM 建模和建筑能耗仿真。
> L21: - 🎯 **高精度分割** — 基于 UNet + ResNet34，CubiCasa5K 数据集 mIoU 达 **0.787**
> L23: - ⚡ **CPU 部署** — 提供 ONNX Runtime 推理方案，无需 GPU，单张推理 < 1.5s


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1bbbd0d19254` · [字段定义](../../DATASET.md)*
