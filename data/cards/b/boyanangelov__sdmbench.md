# boyanangelov/sdmbench

⭐ 19 · R · MIT · 推送 2026-03-16 · [GitHub](https://github.com/boyanangelov/sdmbench) · 个人维护

**物种分布模型（SDM）基准评测的 R 工作流与 GUI**

面向生态学研究者的 R 包，为物种分布建模提供一致的基准评测流程：物种 occurrence 数据（默认从 GBIF 下载，也可 CSV 上传）与环境数据（含未来气候情景）的获取与预处理、空间数据划分、多种机器学习模型集成对比，最终确定预测力最高的模型–数据处理组合，并绘制栖息地适宜性地图。提供 Shiny GUI 供非/半技术用户使用。深度学习（Keras/TensorFlow）与 MaxEnt（需 Java）为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一致的物种与环境数据获取、预处理与空间划分流程
- 集成多种机器学习模型并输出基准评测结果
- Shiny GUI 支持非/半技术用户上传自定义 CSV 数据
- 绘制最优模型的栖息地适宜性地图（静态/动态）

## 适用场景

- 快速对比多个 SDM 模型与数据处理组合的预测力
- 避免模型选择与评估中的不一致问题，快速测试 SDM 原型
- 通过 GUI 用自定义物种分布数据做分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: monitoring 4 . The `sdmbench` package solves
> L19: - integration of a wide variety of machine learning models

## 星数曲线

```mermaid
xychart-beta
    title "boyanangelov/sdmbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8976193c5efd` · [字段定义](../../DATASET.md)*
