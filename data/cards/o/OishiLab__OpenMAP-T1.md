# OishiLab/OpenMAP-T1

⭐ 49 · Python · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/OishiLab/OpenMAP-T1) · 组织维护

**全脑 T1 MRI 深度学习分割工具：分块 280 个解剖区域**

面向神经影像研究者与临床影像分析人员的深度学习全脑分区工具：对 3D T1 加权脑 MRI 执行六阶段流程（预处理、裁剪、去颅骨、分区、半球分割、合并），基于 JHU-atlas 输出 280 个解剖结构标签，单个处理时间低于 90 秒。同一仓库包含 OpenMAP-T1（侧重白质）与 OpenMAP-T1c（侧重脑沟脑脊液）两个模型，需申请下载预训练模型；提供 uv/pip 源码安装、Docker 与 CPU/GPU 推理，论文发表于 Human Brain Mapping。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六阶段 CNN 流程将 T1 MRI 分区为 280 个解剖结构
- 同仓库含 OpenMAP-T1 与 OpenMAP-T1c 两种变体
- 支持 CPU 与 GPU 推理，提供 uv/pip/Docker 三种安装路径
- 输出 NIfTI 分区图与 CSV 区域体积（1mm 网格）

## 适用场景

- 科研中批量做全脑分区并计算区域体积
- 临床 T1 影像的快速脑组织分区
- 替代耗时的多图谱标签融合流程做脑分区

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L19: **OpenMAP-T1: A Rapid Deep-Learning Approach to Parcellate 280 Anatomical Regions to Cover the Whole Brain**
> L26: **Abstract**: *This study introduces OpenMAP-T1, a deep learning-based method for rapid and accurate whole brain pa
> L33: OpenMAP is a family of deep-learning models that parcellate the whole brain into 280 anatomical regions.

## 星数曲线

```mermaid
xychart-beta
    title "OishiLab/OpenMAP-T1 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-27 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3f61610d82bb` · [字段定义](../../DATASET.md)*
