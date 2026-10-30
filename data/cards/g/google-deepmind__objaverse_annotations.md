# google-deepmind/objaverse_annotations

⭐ 16 · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/google-deepmind/objaverse_annotations) · 组织维护

**Objaverse 76 万 3D 物体的 VLM 标注数据集**

DeepMind 发布的 3D 物体标注数据仓库：对 Objaverse 1.0 数据集中 764K 个物体，用 PaLI-X 视觉语言模型经 ScoreAgg 跨多探针聚合，生成三类 CSV 标注——每物体 8 视角聚合的描述（captions）、类型（type）与材质（material）标注，每条含最可能响应及概率，分号为分隔符。属数据发布，无安装运行流程，细节见 ICML 2024 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Objaverse 1.0 的 764K 个 3D 物体
- PaLI-X 生成、ScoreAgg 跨多探针聚合
- captions/type/material 三类标注，含概率，CSV 格式

## 适用场景

- 为 3D 物体检索或生成任务获取文本描述标注
- 研究 VLM 自动标注 3D 资产的质量
- 训练或评测涉及物体类型与材质分类的模型

## 场景标签

 · 领域:计算机视觉/3D 数据

## 证据(README 行号)

> L3: This repo contains captions and property-specific annotations for 764K objects
> L5: by PaLI-X [2] and aggregated across multiple probes using ScoreAgg:

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/objaverse_annotations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0922bbd3287e` · [字段定义](../../DATASET.md)*
