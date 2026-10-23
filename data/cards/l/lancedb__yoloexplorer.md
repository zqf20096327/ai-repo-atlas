# lancedb/yoloexplorer

⭐ 145 · Python · 推送 2026-10-05 · [GitHub](https://github.com/lancedb/yoloexplorer) · 组织维护

**用 SQL 与向量语义搜索迭代 YOLO/CV 数据集的探索工具**

面向计算机视觉数据集的探索与操作库：将 Ultralytics YOLO 格式数据集构建为 LanceDB 表，支持 SQL 查询、向量相似度搜索、相似度索引分析与 Pandas 接口，并以 GUI Dashboard、Python 与 Notebook 工作流使用。可在多数据集间检索并增删图片、持久化生成新数据集版本并输出训练命令，供训练 YOLO、SAM、FAST-SAM、RT-DETR 等模型使用。特征提取支持 resnet18/50、efficientnet、googlenet、mobilenet 等多种预训练模型。API 处于开发阶段，从 dev 到 minor 版本将有变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SQL 查询与向量相似度搜索组合使用，支持任意图片文件作为相似度查询输入
- 多数据集 Dashboard 探索与跨数据集增删图片
- 持久化生成新数据集并输出对应训练命令
- 多种预训练模型（resnet/efficientnet/googlenet/mobilenet）可选用于特征提取

## 适用场景

- 查找并清除数据集中的重复或域外图片
- 针对模型易混淆类别检索相似图片做针对性分析
- 从其他数据集补充图片并生成可直接训练的新数据集版本

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L72: YOLOExplorer can be used to rapidly generate new versions of CV datasets trainable on Ultralytics YOLO, SAM, FAST-S
> L3: Explore, manipulate and iterate on Computer Vision datasets with precision using simple APIs.

## 星数曲线

```mermaid
xychart-beta
    title "lancedb/yoloexplorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-23 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e7c5a631d81a` · [字段定义](../../DATASET.md)*
