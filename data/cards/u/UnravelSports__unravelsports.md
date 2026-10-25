# UnravelSports/unravelsports

⭐ 249 · Python · MPL-2.0 · 推送 2026-01-16 · [GitHub](https://github.com/UnravelSports/unravelsports) · [官网](https://unravelsports.readthedocs.io) · 个人维护

**体育追踪数据分析 Python 库：数据转换、GNN 训练与足球战术指标计算**

面向研究人员、分析师与爱好者的体育追踪数据处理库，覆盖足球与美式橄榄球。功能包括：将多供应商追踪数据转换为 Polars DataFrame（足球经 Kloppy 支持 Sportec、SkillCorner、Metrica 等十余种格式，橄榄球直接读取 BigDataBowl 数据）；将 DataFrame 转换为图并配合 PyTorch Geometric 或 Spektral 训练图神经网络、做预测；计算 Pressing Intensity 与 EFPI 阵型位置识别。提供 Jupyter Notebook 教程与 readthedocs 文档，MPL 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 追踪数据转 Polars DataFrame，足球支持 Sportec/SkillCorner/Metrica/StatsPerform 等多源
- 图转换与 GNN 训练/验证/预测，兼容 PyTorch Geometric 与 Spektral
- 按比赛/回合切分训练集以避免数据泄漏
- Pressing Intensity 计算与 EFPI 阵型位置识别

## 适用场景

- 把多供应商足球追踪数据统一为 DataFrame 再建模
- 训练图神经网络预测比赛事件（如反击成功）
- 计算球队逼抢强度并生成视频可视化

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L22: - ⚽ 🏈 **Graph Neural Network** Training, Graph Conversion and Prediction [🔗 Bekkers &amp; Sahasrabudhe (2023)]
> L60: ⚽🏈 Convert **Polars Dataframes** into Graphs to train **graph neural networks**. These Graphs can be used with **Py
> L61: `unravelsports` allows you to **randomize** and **split** data into train, test and validation sets along matches, 

## 星数曲线

```mermaid
xychart-beta
    title "UnravelSports/unravelsports 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 248 --> 250
    line [249, 249]
```

2026-10-18 249 → 2026-10-25 249（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d0dbb243a22d` · [字段定义](../../DATASET.md)*
