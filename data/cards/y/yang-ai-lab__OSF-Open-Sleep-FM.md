# yang-ai-lab/OSF-Open-Sleep-FM

⭐ 34 · Jupyter Notebook · MIT · 推送 2026-03-12 · [GitHub](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM) · [官网](https://yang-ai-lab.github.io/osf) · 组织维护

**睡眠基础模型 OSF：多导睡眠图信号的预训练与下游任务模型**

面向睡眠生理学研究的代码库：基于 166,500 小时、九个公开来源的睡眠记录构建 SleepBench 基准，系统评估四类自监督预训练目标，并提出 OSF 系列 ViT 骨干睡眠基础模型，在睡眠分期、觉醒/呼吸暂停/血氧饱和事件检测等任务上使用。提供预训练与微调脚本、12 通道 64Hz PSG 输入的嵌入提取 demo notebook 及可下载权重；SleepBench 数据需通过 NSRR 注册申请获取，预处理代码尚未开源。

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

- 166,500 小时、九个公开来源构成的 SleepBench 基准
- 支持对比/自蒸馏/重建/自回归多类自监督预训练方法
- 提供 ViT-Base 12 通道预训练权重与嵌入提取 demo
- 睡眠分期、觉醒、呼吸不足、血氧饱和四类下游任务评测

## 适用场景

- 我需要用预训练模型从 PSG 信号提取嵌入做睡眠分析
- 我想复现或对比睡眠基础模型的预训练与缩放实验
- 我在睡眠分期或事件检测下游任务上做微调评测

## 场景标签

`模型训练` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: To fill this gap, we curate a massive corpus of 166,500 hours of sleep recordings from nine public sources and esta
> L23: With an enhanced pre-training and scaling recipe, we introduce OSF, a family of sleep FMs that achieves state-of-th

## 星数曲线

```mermaid
xychart-beta
    title "yang-ai-lab/OSF-Open-Sleep-FM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7c0ed7cc9742` · [字段定义](../../DATASET.md)*
