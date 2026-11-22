# limix-ldm-ai/LimiX

⭐ 4,424 · Python · NOASSERTION · 推送 2026-11-12 · [GitHub](https://github.com/limix-ldm-ai/LimiX) · [官网](https://www.limix.ai) · 组织维护

**面向表格数据的预训练基础模型：一次前向完成分类/回归/缺失填补**

LimiX 系列是结构化数据基础模型，提供三个规模的预训练权重（LimiX-2 400M、LimiX-2M 2M、LimiX-16M 16M），单个模型在不做任务特定参数更新的情况下，一次前向同时执行分类、回归与缺失值填补。模型采用上下文机制网络（CMN）范式，用结构因果模型生成的合成数据做上下文条件掩码预训练，给出 TabArena/TALENT/BCCO 基准上的评测结果。以 Python 包形式提供 LimiX-infer 命令行推理入口，要求 Python >= 3.12，默认在 CUDA 上运行，也支持 CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单模型一次前向完成分类、回归与缺失值填补，无需任务特定参数更新
- 提供 400M/16M/2M 三个参数规模的预训练权重
- LimiX-infer 命令行入口，支持 --device cpu 回退与 autobatch
- 预训练使用结构因果模型生成的合成数据集

## 适用场景

- 表格数据集上直接推理得到分类与回归预测结果
- 对含缺失特征的数据做缺失值填补
- 在 GPU 或 CPU 环境下批量跑基准数据目录

## 场景标签

 · 领域:机器学习/结构化数据建模

## 证据(README 行号)

> L24: - **[16 Sept 2026] 🚀 LimiX-2 open-source release.** The LimiX-2 weights (`LimiX-2.ckpt`) and inference code are rel
> L35: LimiX-2 is the new-generation model of the LimiX family, developed through model and data scaling guided by our pre
> L198: LimiX supports classification, regression, and missing-value imputation. The public entry point is `inference.pred

## 星数曲线

```mermaid
xychart-beta
    title "limix-ldm-ai/LimiX 星数(近 21 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-22"]
    y-axis "stars" 4384 --> 4428
    line [4387, 4389, 4390, 4392, 4393, 4394, 4399, 4400, 4403, 4392, 4407, 4412, 4413, 4415, 4417, 4418, 4422, 4424, 4425, 4424, 4424]
```

2026-10-20 4,387 → 2026-11-22 4,424（+37）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `fda20e2f10be` · [字段定义](../../DATASET.md)*
