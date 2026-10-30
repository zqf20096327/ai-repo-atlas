# Gregor-Mendel-Institute/aradeepopsis

⭐ 52 · Nextflow · GPL-3.0 · 推送 2026-10-06 · [GitHub](https://github.com/Gregor-Mendel-Institute/aradeepopsis) · 组织维护

**植物图像表型测量流水线：CNN 分割提取 78 项性状**

面向植物研究者（以拟南芥为例）的图像表型分析流水线：基于 Nextflow 编排，内置 DeepLabv3+ 语义分割模型（三个预训练模型可选），从单株植物俯视图像中提取植物面积、衰老/坏死组织面积、花青素组织面积及 78 项形态与颜色相关性状，并提供可视化与 Shiny 报告。依赖通过 conda 或 Docker/podman/Singularity/Charliecloud 容器解析，可从个人电脑扩展到 HPC。支持自定义模型或外部分割掩码输入，仅做性状提取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DeepLabv3+ 语义分割，三个预训练模型可选
- 输出 78 项形态与颜色相关性状
- Nextflow 流程支持 conda 与多种容器运行时，可扩展到 HPC
- 支持接入自定义模型或外部分割掩码

## 适用场景

- 高通量无损测定拟南芥生长、生物量与衰老指标
- 批量处理数十万张单株植物图像
- 利用自定义分割模型复用自动化性状提取流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L18: It is built upon the published, convolutional neural network (CNN) DeepLabv3+ [[1]](#ref1) that serves the task of 
> L35: These file records are then, in parallel, served to a deep learning model, allowing for pixel-by-pixel classificati

## 星数曲线

```mermaid
xychart-beta
    title "Gregor-Mendel-Institute/aradeepopsis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `af2fd3575968` · [字段定义](../../DATASET.md)*
