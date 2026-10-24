# speediedan/finetuning-scheduler

⭐ 69 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/speediedan/finetuning-scheduler) · [官网](https://finetuning-scheduler.readthedocs.io) · 个人维护

**PyTorch Lightning 扩展：用分阶段微调计划表加速模型实验**

Fine-Tuning Scheduler（FTS）是 PyTorch Lightning 的回调扩展，供研究者在基础模型实验中定义灵活的分阶段微调计划：支持显式（正则或逐名参数选择）与隐式计划、每阶段早停与最优 checkpoint 自动恢复、epoch 驱动的阶段切换；2.15 起提供实验性 FTSController 将同样计划带入无 Lightning 的纯 PyTorch 训练循环。版本对齐 PyTorch 核心次版本，官方支持最近 4 个 PyTorch 次版本。通过 PyPI/uv 安装，也提供源码与独立 pytorch-lightning 包安装路径。Docker 版本镜像发布在 2.0.2 后暂停。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 显式/正则参数选择与隐式计划表的分阶段微调
- 每阶段早停驱动的最优 checkpoint 自动恢复与阶段组合
- 实验性 FTSController 支持无 Lightning 的纯 PyTorch 训练循环
- CLI 可在 unified/standalone Lightning 导入模式间切换

## 适用场景

- 按计划表分阶段解冻参数微调基础模型
- 在 SuperGLUE 等基准上做计划微调与 FSDP 实验
- 纯 PyTorch 训练循环中复用同样的分阶段微调逻辑

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L1: **A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules.**
> L17: FinetuningScheduler is simple to use yet powerful, offering a number of features that facilitate model research and
> L116: trainer = L.Trainer(callbacks=[FinetuningScheduler()])

## 星数曲线

```mermaid
xychart-beta
    title "speediedan/finetuning-scheduler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-24 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f1f7e246e5cb` · [字段定义](../../DATASET.md)*
