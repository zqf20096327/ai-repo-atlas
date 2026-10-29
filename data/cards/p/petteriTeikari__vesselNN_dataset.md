# petteriTeikari/vesselNN_dataset

⭐ 18 · MIT · 推送 2026-02-16 · [GitHub](https://github.com/petteriTeikari/vesselNN_dataset) · 个人维护

**小鼠脑血管双光子显微镜体数据集（12 堆栈+体素级标注）**

开源体积式脑血管分割数据集：收录 12 组小鼠脑双光子显微镜堆栈，均附带稠密体素级人工分割标签，来源于三次采集（正常血管、血脑屏障破坏、肿瘤血管）。每堆栈提供 BM4D 去噪后的多层 8-bit TIFF 与对应标签体，附 XML 采集元数据，可直接用于训练与评测体积分割方法。数据为 Teikari et al. (2016) 论文的配套数据，供 vesselNN 分割框架使用。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 组体积堆栈，输入/标签成对提供
- 稠密体素级人工分割标注
- 覆盖正常、血脑屏障破坏、肿瘤三类血管形态
- 含 BM4D 去噪 TIFF、预计算 VD2D/VD2D3D 输出与 XML 采集元数据

## 适用场景

- 训练或基准测试体积血管分割模型
- 研究不同血管形态（正常/BBB 破坏/肿瘤）下的分割性能
- 作为 Teikari et al. (2016) 论文的配套数据复现实验

## 场景标签

 · 领域:医学影像/神经科学

## 证据(README 行号)

> L3: > Open-source volumetric brain vasculature dataset -- 12 two-photon microscopy stacks with dense voxel-level segment
> L14: This repository provides 12 volumetric two-photon microscopy stacks of mouse brain vasculature with dense voxel-lev

## 星数曲线

```mermaid
xychart-beta
    title "petteriTeikari/vesselNN_dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `edc11ef58d8f` · [字段定义](../../DATASET.md)*
