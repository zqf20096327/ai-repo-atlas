# golab-ai/Suiren-Foundation-Model

⭐ 18 · Python · NOASSERTION · 推送 2026-06-24 · [GitHub](https://github.com/golab-ai/Suiren-Foundation-Model) · 组织维护

**分子基础模型：预测量子性质与分子表示学习**

Suiren 分子基础模型通过大规模预训练学习分子表示，支持分子系统能量与力预测、等变原子级嵌入、自定义数据集微调以及领域续训（如二聚体分子 CPT 版本）。仓库以 Python 库形式提供模型 API 与三个 HuggingFace 检查点（Suiren-Base 7GB、Suiren-Dimer 7GB、Suiren-ConfAvg 40M）。输入为原子序数与三维坐标张量，经 ModelLoader 完成数据预处理、推理与去归一化。限制：Base 模型仅支持含 H/C/N/O/F/P/S/Cl/Br/I 的非周期有机分子；推荐逐分子推理，批量可能 OOM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 能量与力的量子性质预测与等变原子级嵌入输出
- 三个预训练检查点（Base/Dimer/ConfAvg），支持微调与领域续训
- YAML 配置驱动，ModelLoader 提供加载、预处理、推理与归一化接口
- 提供全部归一化常数与原子参考表

## 适用场景

- 预测小分子的量子化学能量与力
- 提取原子级嵌入用于下游任务
- 在药物或电池等特定分子域做续训与微调

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L9: Suiren Molecular Foundation Model is designed for quantum property prediction and molecular representation learning.
> L13: - **Energy and Force Prediction**: Accurate quantum property prediction for molecular systems

## 星数曲线

```mermaid
xychart-beta
    title "golab-ai/Suiren-Foundation-Model 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-11-08 18 → 2026-11-21 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `788bd52cd245` · [字段定义](../../DATASET.md)*
