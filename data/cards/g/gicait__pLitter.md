# gicait/pLitter

⭐ 44 · Jupyter Notebook · 推送 2026-04-07 · [GitHub](https://github.com/gicait/pLitter) · 组织维护

**面向街面与河流塑料垃圾检测的数据集与预训练模型项目**

GIC-AIT 发起的塑料垃圾识别与监测项目：提供街面级（pLitterStreet）与河面漂浮（pLitterFloat）两个 RGB 图像数据集，标注为 COCO 格式 JSON，图像来自泰国、越南、斯里兰卡等地；并发布基于 YOLOv5 的预训练权重（Street YOLOv5l AP50 0.77，CCTV YOLOv5s AP50 0.43）。使用方式为车辆 mounted 相机、无人机与河边固定 CCTV 采集图像/视频，用深度学习目标检测识别塑料垃圾并关联 GPS 生成分布热力图。采用主动学习框架应对垃圾形态多变问题。README 未给出安装命令，仅引导参考 Street 与 CCTV demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pLitterStreet / pLitterFloat 两个 COCO 格式标注数据集
- YOLOv5 预训练权重（Street AP50 0.77 / CCTV AP50 0.43）
- 街面车载相机、无人机与固定 CCTV 三种数据采集方式
- 检测关联 GPS 位置生成塑料垃圾分布热力图

## 适用场景

- 城市街面与路边塑料垃圾热点识别与制图
- 河流漂浮塑料的连续监测与通量估算
- 用公开数据集与权重训练自己的垃圾检测模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: An initiative of GIC-AIT to address the plastic pollution through leveraging the Deep Learning and geospatial techno
> L73: ## # Pre-trained models

## 星数曲线

```mermaid
xychart-beta
    title "gicait/pLitter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ca1256f52a6d` · [字段定义](../../DATASET.md)*
