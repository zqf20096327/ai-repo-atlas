# drabekj/Stock-Marke-Prediction

⭐ 19 · Jupyter Notebook · MIT · 推送 2026-06-02 · [GitHub](https://github.com/drabekj/Stock-Marke-Prediction) · 个人维护

**用早收盘全球指数预测标普500当日涨跌的前馈网络**

基于 TensorFlow 2 / Keras 的前馈神经网络，读取澳大利亚 All Ordinaries、日经 225、恒生、DAX 等早于标普 500 收盘的指数当日收益率，在短回看窗口上分类标普 500 同日收益方向。项目始于 2017 年，后迁移至 Python 3.11 + TensorFlow 2，数据经 yfinance 从 Yahoo Finance 下载。提供独立训练脚本 train.py 与原始分析 notebook，示例输出测试准确率 0.5512（多数类基线 0.5293）。属实验性研究代码，非投资工具。

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

- 利用时区错位的早收盘指数当日数据预测标普 500 涨跌方向
- TF2/Keras 独立训练脚本 train.py，去除已废弃 API
- yfinance 数据下载脚本从 Yahoo Finance 刷新数据
- 附带原始分析 notebook Globe+Markets.ipynb

## 适用场景

- 学习时区错位市场信息的时序分类实验
- 复现并修改指数收益率预测模型
- 作为 TensorFlow 2 金融分类示例学习

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: > Feed-forward neural network that predicts the daily direction of the S&P 500
> L36: The model uses the daily returns of the non-target indices over a short

## 星数曲线

```mermaid
xychart-beta
    title "drabekj/Stock-Marke-Prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a4dd1431936b` · [字段定义](../../DATASET.md)*
