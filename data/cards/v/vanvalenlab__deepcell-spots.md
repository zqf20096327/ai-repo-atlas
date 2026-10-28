# vanvalenlab/deepcell-spots

⭐ 24 · Python · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/vanvalenlab/deepcell-spots) · [官网](https://deepcell-spots.readthedocs.io/) · 组织维护

**空间转录组荧光点检测的深度学习 Python 库**

面向空间转录组数据分析的深度学习包，提供 Polaris 应用：可用预训练模型或训练新模型进行荧光点检测（SpotDetection，返回斑点坐标），并用 SVI 概率模型做组合条形码解码（SpotDecoding，返回基因身份），两者配合 DeepCell 的细胞核/细胞质分割模型使用。基于 TensorFlow、Keras、PyTorch 与 DeepCell 构建，以 pip 包和 Docker 镜像形式提供，附示例 notebook。由 Caltech Van Valen Lab 维护，采用修改版 Apache 2 许可。

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

- SpotDetection 预训练模型输出荧光斑点坐标（RNA FISH / 原位测序）
- SpotDecoding 用 SVI 概率模型为每个斑点返回基因身份
- Polaris 组合点检测与解码及 DeepCell 细胞分割
- 支持训练新的深度学习检测模型

## 适用场景

- 对 RNA FISH / 多重 FISH 图像做荧光点检测
- 为多重 FISH 数据集做条形码解码得到基因身份
- 结合细胞分割进行空间转录组分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: `deepcell-spots` is a deep learning package for analyzing spatial transcriptomics data sets. Its application, Polar
> L29: `deepcell-spots` contains an applications that greatly simplify the implementation of machine learning models for s

## 星数曲线

```mermaid
xychart-beta
    title "vanvalenlab/deepcell-spots 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bc30d2303fca` · [字段定义](../../DATASET.md)*
