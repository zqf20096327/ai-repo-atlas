# nalamap/nalamap

⭐ 20 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/nalamap/nalamap) · [官网](http://www.nalamap.org/) · 组织维护

**用自然语言创建网络地图并分析地理空间数据的开源平台**

NaLaMap 是开源 Web GIS 平台：前端 Next.js/Leaflet，后端 Python FastAPI，基于 LangChain/LangGraph 构建 AI agent，支持上传矢量数据、OSM/GeoNames 地理编码、自然语言驱动的自动地理处理（缓冲区、质心、相交等）、AI 辅助地图样式，并可为无地理数据专业知识的用户创建可分享的 GIS-AI 应用。支持 8 家 LLM 提供商（单次仅可激活一家），嵌入支持离线 hashing（默认）、OpenAI 或 Azure。需 PostgreSQL/PostGIS 数据库，可用 Docker 部署。项目处于活跃开发阶段，首个稳定版尚未发布（v1.0.0 未 tag）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言驱动的自动地理处理（buffer/centroids/intersections）
- 多提供商 LLM 支持：OpenAI/Azure/Google/Mistral/DeepSeek/Anthropic/Moonshot/xAI（单次一家）
- 可选嵌入增强的 OSM 语义地理编码（默认离线 hashing）
- 实验性 MCP 集成扩展 AI agent 外部工具
- 为无地理数据专业知识的用户创建并分享 GIS-AI 应用

## 适用场景

- 通过对话式 AI 查询和分析地理空间数据
- 从开放数据门户或自有数据库查找并整合数据
- 为不懂 GIS 的业务用户搭建定制的地图分析应用
- 用自然语言执行缓冲区、质心等地理处理操作

## 场景标签

`数据分析` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L3: NaLaMap is an open-source platform that helps users find and analyze geospatial data in a natural way. It combines m
> L15: * Automated Geoprocessing using natural language (e.g buffer, centroids, intersections).

## 星数曲线

```mermaid
xychart-beta
    title "nalamap/nalamap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `008fd9ac6ad9` · [字段定义](../../DATASET.md)*
