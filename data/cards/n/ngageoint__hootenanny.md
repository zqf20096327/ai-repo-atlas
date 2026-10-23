# ngageoint/hootenanny

⭐ 395 · JavaScript · GPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/ngageoint/hootenanny) · 组织维护

**将多源地图合并为单一无缝地图的地理数据融合工具**

开源地图数据融合（conflation）工具，使用机器学习技术实现地形领域 Foundation GEOINT 要素的自动化与半自动化合并：针对建筑物、道路、铁路、河流、POI 等类型提供专门融合算法，其余类型走通用几何融合；支持 TDS/MGCP/Geonames/OSM 等多种模式的属性翻译、要素过滤、数据清洗与 JOSM 校验集成。提供 Web UI（基于 Mapbox iD Editor）、Web 服务 API、命令行与 Node.js 绑定，可经 RPM、源码或 Docker 安装，未自动匹配的要素可人工审核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 7 类要素的专门融合算法，其余走通用几何融合
- 支持 TDS/MGCP/Geonames/OSM 等模式间的属性翻译
- 提供 Web UI、Web 服务 API、CLI 与 Node.js 绑定多种使用方式
- 保留合并要素的几何与属性来源，支持人工审核未匹配要素

## 适用场景

- 将 OSM 数据与官方地形数据合并为单一底图
- 从多源数据生成可路由的路网
- 批量处理前按要素类型或属性过滤数据
- 通过 API 构建自定义的地图融合客户端

## 场景标签

 · 领域:地理信息系统/地图数据处理

## 证据(README 行号)

> L13: Hootenanny is an open source map data conflation tool developed with machine learning techniques to facilitate auto
> L38: Hootenanny has specifically tailored conflation algorithms available for the following data types:

## 星数曲线

```mermaid
xychart-beta
    title "ngageoint/hootenanny 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 394 --> 396
    line [395, 395]
```

2026-10-18 395 → 2026-10-23 395（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5a1cd57169c4` · [字段定义](../../DATASET.md)*
