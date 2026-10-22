# nipreps/mriqc

⭐ 381 · Python · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/nipreps/mriqc) · [官网](http://mriqc.readthedocs.io) · 组织维护

**脑部 MRI 影像质量指标提取与可视化质控工具**

MRIQC 从结构（T1w/T2w）、功能与弥散 MRI 数据中提取无参考图像质量指标（IQM），生成质量评估报告。基于 nipype 工作流集成 ANTs、AFNI 等第三方工具箱，遵循 BIDS 数据结构与 BIDS-App 标准，采用最小预处理原则。由 NiPreps 社区维护，以 Apache-2.0 许可发布（21.0.x 起），提供 PyPI 包与 Docker 镜像，配套论文发表于 PLOS ONE。

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

- 对结构/功能/弥散 MRI 提取无参考质量指标（IQM）
- 基于 nipype 工作流，集成 ANTs、AFNI 工具箱
- 遵循 BIDS 与 BIDS-App 标准
- 以 Docker 镜像与 PyPI 包形式分发

## 适用场景

- 对脑部 MRI 数据做自动化质量控制
- 在 BIDS 格式数据集上批量生成影像质量报告
- 神经影像流水线前筛除低质量扫描

## 场景标签

 · 领域:神经影像/医学影像质量控制

## 证据(README 行号)

> L5: MRIQC extracts no-reference IQMs (image quality metrics) from
> L6: structural (T1w and T2w), functional and diffusion MRI (magnetic resonance imaging)

## 星数曲线

```mermaid
xychart-beta
    title "nipreps/mriqc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 380 --> 382
    line [381, 381]
```

2026-10-18 381 → 2026-10-22 381（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8c2cca9d7b7e` · [字段定义](../../DATASET.md)*
