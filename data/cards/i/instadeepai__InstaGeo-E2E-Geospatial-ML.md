# instadeepai/InstaGeo-E2E-Geospatial-ML

⭐ 89 · Python · NOASSERTION · 推送 2026-08-22 · [GitHub](https://github.com/instadeepai/InstaGeo-E2E-Geospatial-ML) · 组织维护

**端到端地理空间机器学习框架：卫星影像的预处理、训练与部署**

Python 框架，面向基于多光谱卫星影像（NASA HLS、Sentinel-2/1）的机器学习全流程：Data 组件负责数据检索、切片、云掩膜与 Dask 分布式处理；Model 组件基于 Prithvi 地理空间基础模型进行训练、评估、chip 推理与 Ray 模型服务，附模型注册表；Apps 组件为带交互地图、任务处理与实时监控的 Web 平台，通过 Docker Compose 部署。README 给出洪水制图、作物分割、蝗虫滋生地预测等任务的指标表。需 Python 3.11+，可选 CPU/CUDA 安装变体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Data/Model/Apps 三组件：数据检索→训练推理→Web 服务的全流程覆盖
- 基于 Prithvi 地理空间基础模型，支持洪水制图、作物分割等任务
- uv 锁定依赖与分组件安装（data/model/apps 依赖组）
- Docker Compose 一键部署全栈应用（前端/API/Redis/RQ 队列）

## 适用场景

- 用 HLS 或 Sentinel 影像做洪水制图、作物分类等分割/分类任务
- 训练与微调基于 Prithvi 的地理空间模型
- 在地图界面圈定区域、提交任务并可视化预测结果

## 场景标签

`微调` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: InstaGeo is an end-to-end geospatial machine learning framework that automates data preprocessing, model training, i
> L7: It leverages the Prithvi geospatial foundational model and consists of three core components: Data, Model, and Apps,

## 星数曲线

```mermaid
xychart-beta
    title "instadeepai/InstaGeo-E2E-Geospatial-ML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-29 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `bf9a579e3f08` · [字段定义](../../DATASET.md)*
