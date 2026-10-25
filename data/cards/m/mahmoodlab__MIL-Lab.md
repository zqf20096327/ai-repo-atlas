# mahmoodlab/MIL-Lab

⭐ 158 · Python · NOASSERTION · 推送 2026-02-05 · [GitHub](https://github.com/mahmoodlab/MIL-Lab) · 组织维护

**病理全切片图像多示例学习模型库：9 种 MIL 架构与 FEATHER 预训练权重**

哈佛医学院 Mahmood Lab 开发的多实例学习（MIL）标准化库，面向计算病理学研究者：提供 ABMIL、TransMIL、CLAM、DSMIL 等 9 种 MIL 模型实现，通过 create_model 单行代码初始化；提供在 MGB 泛癌 108 类分类任务（PC-108）上预训练的 FEATHER-24K 权重（0.9M 参数，支持 UNI/CONCHv1.5/UNIv2 编码器，权重需在 HuggingFace 申请权限）。在 15 个基准任务上与 TITAN、GigaPath 等切片基础模型对比。输入为切片 patch 特征张量，可返回注意力分数。采用 CC-BY-NC-ND 4.0 许可，仅限非商业学术研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种 MIL 模型实现，create_model 单行初始化
- FEATHER-24K 预训练权重（PC-108 任务、24K 切片、0.9M 参数）
- 支持 UNI、CONCHv1.5、UNIv2 等 patch 编码器
- 15 个形态与分子分型基准任务的对比评测

## 适用场景

- 在 TCGA 等切片数据上做形态或分子分型训练与推理
- 加载 FEATHER 预训练权重做下游切片分类微调
- 对比或复现多种 MIL 架构的基准表现
- 扩展自定义 MIL 架构并申请 PC-108 预训练

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L8: MIL-Lab provides a standardized library for initializing Multiple Instance Learning (MIL) models, as well as loading
> L13: - **Lightweight supervised slide foundation models**: We provide **FEATHER**, *a lightweight supervised slide found

## 星数曲线

```mermaid
xychart-beta
    title "mahmoodlab/MIL-Lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 157 --> 159
    line [158, 158]
```

2026-10-18 158 → 2026-10-25 158（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `a3e8031ac3bf` · [字段定义](../../DATASET.md)*
