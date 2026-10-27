# Hejarshahabi/TerraTiff

⭐ 27 · Python · NOASSERTION · 推送 2026-06-02 · [GitHub](https://github.com/Hejarshahabi/TerraTiff) · 个人维护

**给遥感/GIS 开发者：无需 GDAL 的 GeoTIFF 读写处理 Python 库**

基于 tifffile、numpy 与 pyproj 构建的轻量级 GeoTIFF 栅格处理库，明确声明无需安装 GDAL。功能包括读取/写出单波段与多波段 GeoTIFF、把 numpy 数组导出为带地理参考的 TIFF、4 种重采样方法（nearest/bilinear/cubic/average）、包围盒裁剪、多边形与栅格掩膜、WGS 84/全部 120 个 UTM 分区/任意 EPSG 的 CRS 解析与元数据级转换，以及 NoData 与波段操作。限制：to_crs 仅重投影元数据，不重采样像元数据。以 pip 包形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 GDAL 依赖，基于 tifffile + numpy + pyproj
- numpy 数组转带地理参考 GeoTIFF，支持任意波段数与 10 余种数据类型
- 4 种重采样方法与包围盒裁剪、多边形/栅格掩膜
- 支持 WGS 84、全部 120 个 UTM 分区与任意 EPSG 代码

## 适用场景

- 把模型输出或计算结果的 numpy 数组保存为带坐标的 GeoTIFF
- 在没有 GDAL 的环境下读写与处理遥感栅格数据
- 对卫星影像做重采样、裁剪与云/地物掩膜处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: A lightweight, **GDAL-free** Python package for reading, writing, and exporting GeoTIFF raster files.
> L47: The most common use case: you have a numpy array (e.g. from a computation, a model output, or a CSV) and you want t

## 星数曲线

```mermaid
xychart-beta
    title "Hejarshahabi/TerraTiff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `db942654f4a9` · [字段定义](../../DATASET.md)*
