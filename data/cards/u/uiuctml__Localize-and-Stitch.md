# uiuctml/Localize-and-Stitch

⭐ 33 · Python · MIT · 推送 2026-02-18 · [GitHub](https://github.com/uiuctml/Localize-and-Stitch) · 组织维护

**稀疏任务算术的模型合并算法官方实现（TMLR 论文）**

论文 Localize-and-Stitch: Efficient Model Merging via Sparse Task Arithmetic（TMLR）的官方实现。算法分两步：定位微调模型中约占参数量 1% 的关键局部区域，再将这些区域拼回预训练模型以实现任务协同，用于将多个微调模型合并为统一模型。论文在多个视觉与语言基准上评估，实验代码在对应文件夹中可复现。另有扩展实现 MergeBench 支持多 GPU 大模型（含 LLM 规模）的定位与基线算法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定位约 1% 参数的关键区域后仅拼回该区域完成合并
- 论文实验（视觉与语言基准）可在对应文件夹复现
- 扩展实现 MergeBench 支持多 GPU 与 LLM 规模模型

## 适用场景

- 复现论文中的视觉与语言模型合并实验
- 将多个微调模型合并为保留各任务能力的单一模型
- 研究稀疏区域作为微调任务的紧凑可解释表示

## 场景标签

 · 领域:机器学习研究/模型合并

## 证据(README 行号)

> L3: This is the official implementation for the algorithm Localize-and-Stitch in the paper "Localize-and-Stitch: Efficie
> L13: Model merging offers an effective strategy to combine the strengths of multiple finetuned models into a unified mod

## 星数曲线

```mermaid
xychart-beta
    title "uiuctml/Localize-and-Stitch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3bd0a976439` · [字段定义](../../DATASET.md)*
