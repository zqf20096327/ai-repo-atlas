# PathologyDataScience/MuTILs_Panoptic

⭐ 30 · Python · MIT · 推送 2026-02-06 · [GitHub](https://github.com/PathologyDataScience/MuTILs_Panoptic) · [官网](https://www.medrxiv.org/content/10.1101/2022.01.08.22268814v3) · 组织维护

**乳腺癌病理图像中肿瘤浸润淋巴细胞（TILs）的 panorptic 分割与评分模型**

基于 PanopTILs 数据集（151 例患者、814,886 个细胞核标注）训练的神经网络 MuTILs，对全切片病理图像执行组织区域与细胞核的联合 panoptic 分割，输出可解释的 TILs 评分。模型为概念瓶颈结构，支持多分辨率预测，内部-外部交叉验证中淋巴细胞检测 AUROC 0.93、肿瘤相关间质分割 DICE 0.81。推理通过 Docker 容器（CUDA 12）运行，读取配置文件处理后按切片输出分割掩码、细胞核元数据与汇总特征；模型权重托管于 Hugging Face。面向数字病理与肿瘤微环境研究使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 组织区域与细胞核联合 panoptic 分割，输出 TILs 评分
- 概念瓶颈模型，多分辨率可解释预测
- 按切片输出分割掩码、细胞核元数据（CSV）与汇总特征（JSON）
- Docker 容器化推理，权重托管于 Hugging Face

## 适用场景

- 对乳腺癌全切片图像做 TILs 计算评分
- 生成肿瘤微环境的组织与细胞分割图
- 研究可解释病理图像分割方法

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: Tumor-Infiltrating Lymphocytes (TILs) have strong prognostic and predictive value in breast cancer, but their visua
> L64: 4. `python MuTILs_Panoptic/mutils_panoptic/MuTILsWSIRunner.py`

## 星数曲线

```mermaid
xychart-beta
    title "PathologyDataScience/MuTILs_Panoptic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0e2a7b250026` · [字段定义](../../DATASET.md)*
