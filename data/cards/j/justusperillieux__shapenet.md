# justusperillieux/shapenet

⭐ 348 · Python · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/justusperillieux/shapenet) · [官网](https://shapenet.rtfd.io) · 组织维护

**PyTorch 实现论文模型的面部关键点检测与形状拟合库**

论文 Super-Realtime Facial Landmark Detection and Shape Fitting by Deep Regression of Shape Model Parameters 的 PyTorch 实现，通过深度回归形状模型参数预测面部关键点并进行形状拟合，描述中给出最高 400 FPS 的速度。提供数据预处理、训练、预测、JIT 导出脚本，内置 Python 与 C++ 的 ShapeLayer 实现，附带灰度人脸与猫的预训练权重（224x224 输入），训练与验证基于 delira 框架。面向使用该代码开展研究的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度回归形状模型参数的 PyTorch 模型实现，预测面部关键点
- 提供数据预处理、训练、预测、torch.jit 导出的完整脚本链
- ShapeLayer 提供 Python 与 C++ 双实现，JIT 模块可从 Python 与 C++ 访问
- 附灰度人脸与猫的预训练权重

## 适用场景

- 在面部图像上预测关键点并拟合形状模型
- 复现论文实验或在新数据集上训练形状回归网络
- 将训练好的模型导出为 jit-ScriptModule 用于 Python 或 C++ 部署

## 场景标签

`科研工具` `人脸识别` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains the PyTorch implementation of our Paper "SUPER-REALTIME FACIAL LANDMARK DETECTION AND SHAPE
> L34: #### Prediction
> L46: The `networks` subpackage contains the actual implementation of the shapenet with bindings to integrate the `ShapeL


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c360c35c5dd0` · [字段定义](../../DATASET.md)*
