# SaptakBhoumik/TinyVision

⭐ 31 · Jupyter Notebook · CC-BY-SA-4.0 · 推送 2026-05-04 · [GitHub](https://github.com/SaptakBhoumik/TinyVision) · 个人维护

**超轻量图像分类模型研究项目：极小参数量CNN实验**

个人维护的实验性研究项目，探索极小参数量的图像分类模型设计：将手工特征预处理（滤波器组）与紧凑 CNN 架构结合。已完成猫狗分类（1.25万参数以下模型达 86.87% 测试准确率，部分 5k 参数以下模型超 83%）与 Cifar10 分类（22.11k 参数模型达 87.38%）。近期分享基于分位数的 3 比特量化实验（量化模型与 F32 精度差约 5%）。不提供预训练权重下载或安装包，以代码与实验结果形式发布，不接受 PR，缺正式论文与对照比较。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 猫狗分类：12.5k 参数以下模型达 86.87% 测试准确率
- Cifar10：22.11k 参数模型达 87.38% 准确率
- 滤波器组手工特征预处理 + 紧凑 CNN 的组合路线
- 自研分位数 3 比特量化实验（含激活与首末层）

## 适用场景

- 研究极小参数量模型的效率-性能边界
- 复现紧凑 CNN 图像分类实验（猫狗/Cifar10）
- 参考低比特量化（3bit QAT）实验结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **TinyVision** is an evolving research project focused on designing **ultra-lightweight image classification models*
> L35: - ✅ **Cat vs Dog Classification**
> L40: - ✅ **Cifar10 Classification**

## 星数曲线

```mermaid
xychart-beta
    title "SaptakBhoumik/TinyVision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `80629094d5bf` · [字段定义](../../DATASET.md)*
