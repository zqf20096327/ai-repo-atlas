# Ladbaby/PyOmniTS

⭐ 105 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Ladbaby/PyOmniTS) · [官网](https://ladbaby.github.io/PyOmniTS-docs/) · 组织维护

**时间序列分析训练框架：任意模型×数据集×损失组合训练**

面向研究者的时间序列分析训练框架，收录 54 个模型（覆盖规则采样 MTS、不规则采样 IMTS、预训练与交通模型）、11 个数据集与 5 类损失函数，支持预测、分类、插补三种任务。核心机制：模型 forward 参数与数据集 __getitem__ 返回值解耦，适配一次即可组合训练；核心组件最少化依赖（不依赖 PyTorch Lightning 等），支持多 GPU 并行训练。另在 Hugging Face 提供时间序列排行榜，并为 agent 提供官方 PyOmniTS skill。限制：分类与插补数据集尚未发布。

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

- 收录 54 个模型与 11 个数据集，支持任意模型×数据集×损失组合训练
- 模型 forward 与数据集 __getitem__ 参数/返回值解耦，新增组件不破坏既有训练代码
- 核心组件最少化第三方依赖，支持多 GPU 并行训练
- Hugging Face 时间序列排行榜与 agent 专用 skill（clawhub）

## 适用场景

- 复现时间序列论文模型并跨数据集统一评测
- 在不规则多变量时间序列（医疗/生物力学）上做预测或插补
- 把其他论文代码改造进统一框架由 agent 自动化复现

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L31: - **Extensibility**: Adapt your model/dataset **once**, train almost **any combination** of "model" $\times$ "datas
> L46: 54 models, covering regular, irregular, pretrained, and traffic models, have been included in PyOmniTS, and more ar

## 星数曲线

```mermaid
xychart-beta
    title "Ladbaby/PyOmniTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-24 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b2929d4f87c8` · [字段定义](../../DATASET.md)*
