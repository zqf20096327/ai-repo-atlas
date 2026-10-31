# MICS-Lab/thunder

⭐ 51 · Python · CC-BY-4.0 · 推送 2026-10-28 · [GitHub](https://github.com/MICS-Lab/thunder) · [官网](https://mics-lab.github.io/thunder/) · 组织维护

**病理图像基础模型评测基准：23 个模型 16 个数据集横向评测**

THUNDER 是发表于 NeurIPS 2025 D&B Track（Spotlight）的 tile 级数字病理学图像理解基准，用于对比计算病理学基础模型：覆盖下游任务性能、特征空间比较、不确定性与鲁棒性三个维度，集成 23 个基础模型（UNI、Virchow、Phikon、CONCH、DINOv2 等）与 16 个数据集，支持用户自定义模型与自定义数据集。提供 Python API 与 CLI 下载模型/数据并运行基准，另含 get_model_from_name 接口可在自有数据上提取 embeddings；提供 SLURM 脚本复现排行榜。以 PyPI 包（thunder-bench）分发，需设置 THUNDER_BASE_DATA_FOLDER 环境变量，分割任务需至少 32GB 显存的 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 23 个基础模型 × 16 个数据集的三维度评测（性能/特征空间/不确定性）
- 支持自定义模型与自定义数据集运行任一任务
- API 与 CLI 下载模型数据并运行基准，含零样本 VLM 分类任务
- 提供 SLURM 脚本复现排行榜结果

## 适用场景

- 横向比较病理学基础模型在下游任务上的表现
- 在自有病理数据集上评测已支持或自定义的模型
- 用任一支持的基础模型提取自身数据的 embeddings

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: We introduce **THUNDER**, a comprehensive benchmark designed to rigorously compare foundation models across various
> L34: We propose a benchmark to compare and study foundation models across three axes: (i) downstream task performance, (

## 星数曲线

```mermaid
xychart-beta
    title "MICS-Lab/thunder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-31 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b2b27f7a3c41` · [字段定义](../../DATASET.md)*
