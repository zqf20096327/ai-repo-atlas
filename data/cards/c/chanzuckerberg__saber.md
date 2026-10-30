# chanzuckerberg/saber

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-10-19 · [GitHub](https://github.com/chanzuckerberg/saber) · 组织维护

**用 Segment Anything 2 从电镜数据分割细胞器的研究平台**

SABER 面向科研用户，对冷冻电子断层扫描（cryo-ET）或电镜（EM）数据做细胞器自主分割。基于基础视觉模型（Segment Anything 2 类）把视频级训练迁移到 3D 断层图像分析：支持零样本推理（配合形态学启发式）或用专家标注训练自定义分类器以提升精度。提供交互式 GUI 用于标注与分割细化，可生成跨断层切片的体积分割掩码，以 Python 包与 CLI 形式分发。注意需 pip 25.2 及以上安装，GUI 为可选额外安装。

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

- 零样本分割 EM/cryo-ET 数据，无需显式重训练
- 交互式 GUI 用于人工标注与分割细化
- 基于专家标注训练自定义分类器精调结果
- 生成跨断层切片的 3D 体积分割掩码

## 适用场景

- 对 cryo-ET 断层图像做细胞器三维分割
- 用少量专家标注训练分割分类器
- 人工标注并精调电镜数据分割结果

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L8: **S**egment **A**nything **B**ased **E**xpert **R**ecognition is a robust platform designed for autonomous segmentat
> L14: * 🔍 Zero-shot segmentation: Segment EM/cryo-ET data without explicit retraining, using foundational vision models.

## 星数曲线

```mermaid
xychart-beta
    title "chanzuckerberg/saber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `245ccf91ab9d` · [字段定义](../../DATASET.md)*
