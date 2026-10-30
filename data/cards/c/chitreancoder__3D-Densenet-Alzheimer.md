# chitreancoder/3D-Densenet-Alzheimer

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-10-16 · [GitHub](https://github.com/chitreancoder/3D-Densenet-Alzheimer) · 个人维护

**3D DenseNet 集成模型：对 T1 MRI 做 4 类阿尔茨海默病分类**

发表于 Brain Informatics (BI 2020) 的论文配套代码与权重：三个 3D DenseNet-121 模型对 ADNI T1 MRI 扫描做 CN/AD/EMCI/LMCI 四分类，集成平均三者输出，验证集准确率 83.3%。提供训练、评估脚本及论文权重。数据来自 ADNI 且不可再分发，用户需自备 ADNI 账号，将 NIfTI 文件放入指定目录后生成 80/20 划分。README 说明限制：按扫描而非按被试划分、无独立测试集、已发布权重基于早期不可复原的划分。

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

- 三个 3D DenseNet-121 模型集成，4 类分类验证准确率 83.3%
- 提供论文训练权重与 train/evaluate 脚本
- make_splits.py 生成含 ADNI 被试 ID 的 80/20 划分

## 适用场景

- 复现 BI 2020 论文的 AD 四分类实验
- 用自己的 ADNI 数据重训或评估 3D DenseNet 集成
- 基于提供的模型结构做医学影像分类研究

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Code and weights for 3D DenseNet Ensemble in 4-Way Classification of Alzheimer's Disease (Brain Informatics, BI 2020
> L5: Three 3D DenseNet-121 models classify T1 MRI scans as CN, AD, EMCI or LMCI, and the ensemble averages their outputs.

## 星数曲线

```mermaid
xychart-beta
    title "chitreancoder/3D-Densenet-Alzheimer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8d5bd36bd625` · [字段定义](../../DATASET.md)*
