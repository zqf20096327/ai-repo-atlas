# geospaitial-lab/adois

⭐ 24 · Python · GPL-3.0 · 推送 2026-05-28 · [GitHub](https://github.com/geospaitial-lab/adois) · 组织维护

**从 RGB/NIR 正射影像自动生成不透水面地图的工具**

德国 Recklinghausen 县委托、与 Westfälische Hochschule Gelsenkirchen 合作的科研产物：用深度学习方法从数字正射影像（RGB 与 NIR，经可配置 WMS 获取）生成高分辨率不透水面地图，并按地块/瓦片聚合，结果以 Shapefile 导出。模型基于 Emschergenossenschaft Lippeverband 的人工调查数据训练，采用 ONNX 格式。提供 Dockerfile 与 Python 虚拟环境两种安装运行方式，硬件要求 8GB RAM。README 为德语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 RGB/NIR 正射影像生成不透水面地图并按地块聚合
- 影像经可配置 WMS（Web Map Service）获取
- 模型为 ONNX 格式，需单独下载
- 结果以 Shapefile 导出

## 适用场景

- 为市政/县级区域自动化生成不透水面地图
- 基于正射影像做土地封盖统计分析
- 将不透水面结果导入 GIS 系统（Shapefile 输出）

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L15: mit dem Ziel der automatisierten Erkennung versiegelter Flächen aus Fernerkundungsdaten mit Methoden des Deep Learn
> L16: *adois* ermittelt aus RGB- und NIR-DOPs (Digital Orthophoto) hochauflösende Versiegelungskarten inklusive einer Agg

## 星数曲线

```mermaid
xychart-beta
    title "geospaitial-lab/adois 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f624d5691c0a` · [字段定义](../../DATASET.md)*
