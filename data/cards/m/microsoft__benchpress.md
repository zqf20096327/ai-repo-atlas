# microsoft/benchpress

⭐ 34 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/microsoft/benchpress) · 组织维护

**为 LLM 补全未跑评测分数的基准成绩预测工具与数据集**

Microsoft Research 发布的基准分数补全工具：整理 84 个前沿模型在 133 个基准上的公开分数矩阵（23.3% 填充率），发现其几何近似秩 2，用 Logit+Bias ALS 分解补全缺失分数，中位绝对误差 4.6 分，并给出校准 90% 区间与信任概率。支持使用内置矩阵、导入 EEE/HELM 外部数据或自带 CSV，仅需少数已知分数即可预测模型其余基准表现。面向 LLM 评测与选型场景的开发者与研究者，代码 MIT，数据集 CDLA-Permissive-2.0，Windows 安装步骤标注 TBA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- logit 空间偏差分解秩 2 矩阵补全，缺失分数预测中位误差 4.6 分
- 内置 84 模型 × 133 基准引用可溯分数矩阵，数据发布于 Hugging Face
- 支持 EEE / HELM 外部分数导入与自带 CSV 矩阵
- 五个探针基准即可预测其余评测画像，保留 92.1% 成对模型排序

## 适用场景

- 模型发布前预估其在未跑基准上的分数，决定最值得运行的评测
- 只提供少数已知分数即可补全自家模型完整的基准画像
- 复现论文的分数矩阵与预测方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L22: **Abstract**: A modern model release reports scores on 40+ benchmarks; behind the release, evaluations were run ord
> L24: We compile a public score matrix of 84 frontier models on 133 benchmarks (2,604 observed cells, 23.3% filled) and f
> L270: BenchPress uses **Logit + Bias ALS**:

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/benchpress 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a8ab51cd34a` · [字段定义](../../DATASET.md)*
