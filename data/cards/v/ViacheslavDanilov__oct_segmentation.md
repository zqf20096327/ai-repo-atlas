# ViacheslavDanilov/oct_segmentation

⭐ 19 · Python · MIT · 推送 2026-01-01 · [GitHub](https://github.com/ViacheslavDanilov/oct_segmentation) · [官网](https://www.vdanilov.com/portfolio/coronary-insight/) · 个人维护

**面向心血管科研：OCT 图像中动脉粥样硬化斑块的分割与量化**

基于深度学习的 OCT（光学相干断层扫描）图像斑块分割项目：针对 103 名患者、25,698 张标注切片的数据集，识别管腔、纤维帽、脂质核与滋养血管四类特征。采用九种分割架构（U-Net、U-Net++、DeepLabV3+、LinkNet 等）并按特征流行度设计混合分割策略（单类/双类专用模型），经贝叶斯超参优化与 5 折交叉验证训练。提供 predict.py 推理管线与基于 Streamlit 的可视化 Web 应用；通过 git clone 与 uv 安装，需 Python 3.11。

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

- 四类斑块特征分割（管腔 DSC 0.987、脂质核 0.751）
- 九种架构对比与按特征定制的混合分割策略
- Bayesian+HyperBand 超参优化与 5 折交叉验证
- Streamlit Web 应用：分割叠加、面积动态图表、AI 风险评估

## 适用场景

- 对 OCT 图像批量自动分割斑块形态特征
- 在 Web 界面中浏览患者切片的分割结果与指标
- 复现心血管影像分割研究并引用配套数据集与模型

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L11: This repository provides a comprehensive approach for deep learning-based segmentation and quantification of athero
> L28: We employed nine advanced deep learning architectures — U-Net, U-Net++, DeepLabV3, DeepLabV3+, FPN, LinkNet, PSPNet

## 星数曲线

```mermaid
xychart-beta
    title "ViacheslavDanilov/oct_segmentation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `a9e0587b9f07` · [字段定义](../../DATASET.md)*
