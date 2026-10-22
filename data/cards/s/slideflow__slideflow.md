# slideflow/slideflow

⭐ 376 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/slideflow/slideflow) · [官网](https://slideflow.dev) · 组织维护

**面向数字病理的深度学习库：全幻灯片图像训练与部署**

Python 深度学习库，面向医学研究者和开发者，用于病理全幻灯片图像（WSI）模型的开发：以 Project 组织切片、切块提取（TFRecords）、弱监督/强监督训练（分类、连续、时序结局）、MIL/SSL/GAN、内置基础模型，并提供热图、镶嵌图、显著性图等可解释性工具与交互式部署界面。支持 PyTorch 与 TensorFlow 双后端，切片读取可选 cuCIM 或 Libvips；另提供 GPL/非商业附加包接入更多预训练模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全幻灯片图像切块提取与训练流水线（弱/强监督）
- 内置基础模型、MIL、SSL、GAN 与不确定性量化
- 热图/镶嵌图/显著性图等可解释性工具
- PyTorch 与 TensorFlow 双后端，cuCIM/Libvips 双切片读取后端

## 适用场景

- 在数字病理切片数据上训练分类或生物标志物预测模型
- 生成模型预测热图与镶嵌图做结果分析
- 用预配置项目从 Genomic Data Commons 下载数据快速入门

## 场景标签

 · 领域:数字病理/医学影像

## 证据(README 行号)

> L11: **Slideflow is a deep learning library for digital pathology, offering a user-friendly interface for model developm
> L16: - Easy-to-use, highly customizable training pipelines
> L26: - **Interactive user interface** for model deployment

## 星数曲线

```mermaid
xychart-beta
    title "slideflow/slideflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 375 --> 377
    line [376, 376]
```

2026-10-18 376 → 2026-10-22 376（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3fa29b4a0edd` · [字段定义](../../DATASET.md)*
