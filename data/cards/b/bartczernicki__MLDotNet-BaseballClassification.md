# bartczernicki/MLDotNet-BaseballClassification

⭐ 15 · C# · 推送 2026-05-05 · [GitHub](https://github.com/bartczernicki/MLDotNet-BaseballClassification) · 个人维护

**用 ML.NET 与 MLB 历史数据训练棒球名人堂分类器的 .NET 工程**

基于 .NET 与 ML.NET 的机器学习训练作业：读取 1876-2025 年 MLB 打者生涯数据，训练多个二分类模型，预测打者是否进入名人堂候选名单及是否入选。机制上支持从配置数组动态选择特征、在单一数据集的两个标签间切换、复用基础数据转换管道、用预定义保留集报告性能指标，并以规则引擎选出最佳模型；模型以 ML.NET 原生格式与 ONNX 持久化，可加载做模型可解释性与新球员推理。面向 .NET 开发者，需 Visual Studio 或 VSCode 及 .NET 10.x、ML.NET v5.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一训练作业构建多个 ML.NET 二分类模型
- 动态特征选择与标签切换
- 模型同时持久化为 ML.NET 原生格式与 ONNX
- 规则引擎选最佳模型并做推理与模型可解释性

## 适用场景

- 用生涯统计数据预测打者入选名人堂的概率
- 参考 ML.NET 多模型训练作业与特征选择写法
- 导出 ONNX 格式模型用于跨框架部署

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: A .Net model building job that builds several models using MLB Baseball data from 1876 - 2025.
> L11: * Builds multiple ML.NET binary classification models in a single C# "script" (training job)

## 星数曲线

```mermaid
xychart-beta
    title "bartczernicki/MLDotNet-BaseballClassification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ae577ba4ece0` · [字段定义](../../DATASET.md)*
