# voxel51/voxelgpt

⭐ 255 · Python · Apache-2.0 · 推送 2026-08-11 · [GitHub](https://github.com/voxel51/voxelgpt) · [官网](https://gpt.fiftyone.ai) · 组织维护

**用自然语言查询视觉数据集与 FiftyOne 文档的 AI 助手插件**

Voxel51 团队开发的 FiftyOne 插件，结合 LLM/LMM 与 FiftyOne 计算机视觉查询语言，让用户以自然语言过滤、排序、语义切分数据集并提问：支持数据 schema、目标检测、地理位置、时间与聚合查询，可执行亮度/唯一性/聚类等计算（可用环境变量禁用或设置审批阈值），并可基于 FiftyOne 文档、博客与 YouTube 转录回答文档问题及一般机器学习问题。默认使用 OpenAI API，支持私有 Azure OpenAI 部署；可在 FiftyOne App 中作为插件或 operator 使用，也可在 Python 中交互调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转为 FiftyOne 视图阶段，支持 schema/检测/地理/时间/聚合查询
- 可执行亮度、熵、唯一性、相似度索引、降维、聚类等计算，带审批与环境变量控制
- 基于 FiftyOne 文档、Voxel51 博客与 YouTube 转录回答文档问题（YouTube 链接定位到时间戳）
- 支持 OpenAI 与私有 Azure OpenAI 部署，可在 App 或 Python 中使用

## 适用场景

- 不写代码，用英文提问搜索和筛选我的图像/视频数据集
- 让 AI 代为执行数据集计算（去重、聚类、唯一性打分）
- 查询 FiftyOne 文档与计算机视觉概念并获得带出处的解答

## 场景标签

 · 领域:计算机视觉/数据集工具

## 证据(README 行号)

> L15: VoxelGPT is a FiftyOne Plugin
> L18: vision query language, enabling you to filter, sort, semantically slice and ask
> L213: Finally, VoxelGPT can answer general questions about computer vision, machine

## 星数曲线

```mermaid
xychart-beta
    title "voxel51/voxelgpt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 253 --> 256
    line [254, 255, 255]
```

2026-10-18 254 → 2026-10-22 255（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `166bd7d05075` · [字段定义](../../DATASET.md)*
