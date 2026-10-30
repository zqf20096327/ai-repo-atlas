# yacine-benbaccar/Pool-Detection

⭐ 18 · Jupyter Notebook · 推送 2026-02-18 · [GitHub](https://github.com/yacine-benbaccar/Pool-Detection) · 个人维护

**从卫星图像中检测游泳池的 Convnet 图像分类 POC**

证明卫星图像中检测泳池可行性的概念验证项目：训练一个 3 层 Convnet 分类模型区分含泳池与不含泳池的 50x50 图像（训练集约 1400 张/类，验证集约 100 张/类）；检测时将卫星图像切分为 512 个 50x50 patch 逐一预测，30 张卫星图像在双核 CPU 上约 35 秒处理完成。包含相邻框合并后处理、概率阈值过滤与热力图可视化，输出各候选框坐标与概率的字典。作者自述为基线工作，可后续改进。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 3 层 Convnet 二分类模型，基于 50x50 图像训练
- 滑窗网格检测，每张卫星图像 512 个候选 patch
- 相邻检测框合并后处理与概率阈值过滤（默认 ≥0.5）
- 输出 bounding box 坐标与概率字典，支持热力图叠加可视化

## 适用场景

- 在卫星图像上定位潜在泳池位置
- 作为低分辨率遥感图像检测的基线实现
- 复现并改进滑窗式目标检测流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: The aim of this project is to provide a POC (Proof Of Concept) to prove the feasibility of **detecting pools from sa
> L48: The baseline model is a simple 3-layered Convnet. This model is a simple implementation of a *Convolutional Neural 
> L54: For the detection part, we divide the image into a grid of 50x50 patches which give us 512 candidate positions to t

## 星数曲线

```mermaid
xychart-beta
    title "yacine-benbaccar/Pool-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `a6b2158f1fc7` · [字段定义](../../DATASET.md)*
