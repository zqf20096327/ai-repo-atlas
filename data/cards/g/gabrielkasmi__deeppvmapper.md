# gabrielkasmi/deeppvmapper

⭐ 37 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/gabrielkasmi/deeppvmapper) · 个人维护

**法国屋顶光伏大规模检测流水线：航拍影像分类分割并提取装机特征**

面向法国本土的屋顶光伏检测流水线：读取 IGN 航拍切片，用 InceptionV3 分类 299×299 图块，FCN/DeepLab 分割正样本，再经 pypvroof 提取面积、倾角、方位角与装机容量，输出 GeoJSON 与 CSV 登记。需系统级安装 GDAL 并配置数据路径，GPU（CUDA 11.8+、8GB 显存）为必需，断点可续跑。另将 114 万+检测结果以公共 MCP 服务器形式暴露，供 MCP 客户端自然语言查询。成果来自 Mines Paris-PSL 博士工作（2020–2024），附博士论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分类→分割→特征提取四步流水线，崩溃后可从断点续跑
- 输出逐装机登记（面积/倾角/方位角/kWp）与市级聚合 CSV、GeoJSON
- 1.14M+ 检测结果通过公共 MCP 服务器供自然语言查询
- 仅保留位于建筑物上的住宅级装机（1.7–36.1 kWp）

## 适用场景

- 按法国省份批量检测屋顶光伏并统计装机容量
- 通过 MCP 客户端查询既有的检测结果与年度部署情况
- 获取带地理坐标与物理特征的光伏装机研究数据集

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: Large-scale rooftop PV detection pipeline for France. Classifies IGN aerial tiles with InceptionV3, segments positiv
> L108: |**Classification**|Tiles loaded fully in memory. InceptionV3 classifies 299×299 patches; positives saved as GeoTI
> L109: |**Segmentation**|FCN/DeepLab segments each positive patch. LAMB93 polygons extracted, sorted by tile, merged into

## 星数曲线

```mermaid
xychart-beta
    title "gabrielkasmi/deeppvmapper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `58bdb5d60dd2` · [字段定义](../../DATASET.md)*
