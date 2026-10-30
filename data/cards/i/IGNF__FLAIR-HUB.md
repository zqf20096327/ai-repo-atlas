# IGNF/FLAIR-HUB

⭐ 54 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/IGNF/FLAIR-HUB) · [官网](https://ignf.github.io/FLAIR/FLAIR-HUB/flairhub.html) · 组织维护

**FLAIR-HUB 遥感数据集的多模态语义分割训练与推理代码**

法国 IGN 维护的 UperFuse 代码库，基于 FLAIR-HUB 数据集（覆盖法国 2,528 km²、六种对齐模态：航空影像、Sentinel-1/2 时序、SPOT、地形与历史航空影像）进行土地利用与作物制图的多模态、多任务语义分割。提供两个入口：patch 级的训练/推理/指标计算，以及用预训练模型对更大区域推理的 zonal 检测。通过 conda + pip 安装，以 YAML 配置驱动，附基准结果表与 Tkinter 数据子集下载 GUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持六种模态融合的土地覆盖/作物多任务语义分割训练与推理
- patch 级训练入口 + 大区域 zonal 推理入口双工作流
- 提供 19 个基准配置的 O.A./mIoU 结果表与推理类别配色
- 附带按域/年份/模态筛选下载数据子集的桌面 GUI

## 适用场景

- 在 FLAIR-HUB 数据集上训练多模态遥感分割模型
- 用预训练模型对大区域做土地覆盖或作物制图推理
- 复现或对比多模态融合的基准结果

## 场景标签

`多模态` `目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L27: This repository is built on top of the **FLAIR-HUB** dataset, the largest multi-sensor land cover dataset with very
> L63: #### :file_folder: src/flair_hub --> used to train, infer models, calculate metrics, at the patch level.
> L68: #### :file_folder: src/flair_zonal_detection --> used to infer a pretrained model over larger areas.

## 星数曲线

```mermaid
xychart-beta
    title "IGNF/FLAIR-HUB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-30 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `07623b629a54` · [字段定义](../../DATASET.md)*
