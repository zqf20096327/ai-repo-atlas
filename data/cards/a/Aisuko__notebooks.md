# Aisuko/notebooks

⭐ 24 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/Aisuko/notebooks) · [官网](https://www.kaggle.com/aisuko/code) · 个人维护

**在 Kaggle 免费 GPU 上实践 LLM 工具与量化技术的 notebook 集合**

一组在 Kaggle 平台上运行的 ML/LLM 实验 notebook 合集，覆盖微调、量化、多模态、NLP、强化学习、计算机视觉等任务，使用 P100 单卡、T4x2 双卡或 CPU 完成。作者目标是在受限算力与消费级硬件上研究生成式 AI，熟悉 LLM 工具生态与量化技术。微调指标记录于 wandb.ai，并说明因 num_train_epochs 不足指标并非最优。部分大型 notebook（如 BERTopic 主题建模）需到 Kaggle 平台查看完整版本。

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

- 全部 notebook 在 Kaggle 免费 GPU（P100/T4x2）或 CPU 上运行
- 覆盖微调、量化、PEFT、多模态等 LLM 任务与工具生态实践
- 微调指标（训练/评估/系统功耗）记录于 wandb.ai

## 适用场景

- 在免费 GPU 环境下学习 LLM 微调与量化流程
- 参考受限算力下的模型实验做法与指标记录
- 跟随 notebook 了解 LLM 工具生态与相关论文概念

## 场景标签

`教程课程` `微调` `模型量化` · 领域:学习与行业

## 证据(README 行号)

> L3: > We might agree that the operation of LLMs will embed in daily programming in the future. So, we use these notebook
> L5: All these notebooks have been completed running on the Kaggle platform. With the free GPUs. Some of the notebooks us
> L29: > Note: All the fine-tuning here is under the limited computing resource, so the metrics are not the best. Most of 

## 星数曲线

```mermaid
xychart-beta
    title "Aisuko/notebooks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2b93db4e6759` · [字段定义](../../DATASET.md)*
