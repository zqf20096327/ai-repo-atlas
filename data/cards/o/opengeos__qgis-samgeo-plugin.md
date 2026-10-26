# opengeos/qgis-samgeo-plugin

⭐ 129 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/opengeos/qgis-samgeo-plugin) · [官网](https://samgeo.gishub.org) · 个人维护

**QGIS 插件：在 GIS 中用 SAM 做遥感图像分割**

QGIS 插件，封装 SamGeo Python 包，基于 Meta Segment Anything Model 对遥感影像做分割。支持 SamGeo（SAM1）/SamGeo2/SAM3 三个版本，提供文本提示、点提示、框提示与批量点分割四种交互方式，处理后可输出为矢量（GeoPackage/Shapefile）或栅格（GeoTIFF），并保留地理参考。运行需 QGIS 3.22+、Python 3.10+，SAM 3 模型需在 Hugging Face 申请访问权限，或从 ModelScope 下载。也可在 QGIS Python 控制台中编程调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 SAM1/SAM2/SAM3 三代模型，可选 meta 或 transformers 后端与 cuda/cpu 设备
- 文本、点、框、批量点四种分割提示方式
- 保留空间参考的 GeoTIFF 输入，矢量/栅格两种输出格式
- 可在 QGIS Python 控制台编程调用

## 适用场景

- 在 QGIS 中对遥感影像按文本描述提取建筑物、树木、道路等地物
- 通过点击/框选交互式分割地图上的目标区域
- 用建筑质心点批量分割大量单个对象

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: A QGIS plugin for remote sensing image segmentation using SamGeo, powered by Meta's Segment Anything Model (SAM).
> L12: - **Text-based segmentation**: Describe what you want to segment (e.g., "building", "tree", "road")
> L148: 1. Enter a text prompt describing what to segment (e.g., "tree", "building")

## 星数曲线

```mermaid
xychart-beta
    title "opengeos/qgis-samgeo-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 128 --> 130
    line [129, 129]
```

2026-10-18 129 → 2026-10-26 129（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `94338a1f5afb` · [字段定义](../../DATASET.md)*
