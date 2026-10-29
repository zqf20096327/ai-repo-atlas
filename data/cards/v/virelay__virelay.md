# virelay/virelay

⭐ 31 · Python · AGPL-3.0 · 推送 2026-04-30 · [GitHub](https://github.com/virelay/virelay) · 组织维护

**可视化 CoRelAy 生成的谱相关性分析结果的 Web 工具**

XAI 可视化工具，以小型 Web 应用的形式查看、浏览和交互分析 CoRelAy 生成的 SpRAy 流水线结果，包括源数据、归因、聚类与嵌入。项目文件为 YAML 格式，数据集、归因数据库与分析数据库采用 HDF5 或目录结构。支持同时打开多个项目，分析发现可导入、导出和共享。当前仅支持图像数据，归因需与对应输入数据同形状。内置 HTTP 服务器适合小项目，大规模部署建议配合 Gunicorn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化检查 CoRelAy 生成的分析结果
- 归因数据以热力图展示，支持多种聚类方法发现异常分类策略
- 支持多项目并排打开，发现可导入/导出/共享
- 提供 pipx/pip 安装与本地或服务器运行方式

## 适用场景

- 分析模型在数据集上的归因与聚类结果，理解分类策略
- 与协作者共享和复用 XAI 分析发现
- 定位数据集中被异常分类的样本

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **ViRelAy** is an XAI visualization tool for the analysis of the results of spectral relevance analysis (SpRAy) pip
> L33: - Understand the classification strategies of your model by viewing attribution data as heatmaps

## 星数曲线

```mermaid
xychart-beta
    title "virelay/virelay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `28d16a98530c` · [字段定义](../../DATASET.md)*
