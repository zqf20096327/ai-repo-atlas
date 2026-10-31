# ankane/xgboost-ruby

⭐ 121 · Ruby · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/ankane/xgboost-ruby) · 个人维护

**Ruby 版 XGBoost 绑定库：在 Ruby 中训练与预测梯度提升模型**

通过 FFI 在 Ruby 中调用 XGBoost 的机器学习库，提供 Learning API（DMatrix、Booster、训练/预测/交叉验证/早停）与仿 scikit-learn 风格的 Regressor/Classifier 接口；支持模型保存加载（JSON）、特征重要度、模型元数据，数据可传入数组、Numo 数组或 Rover 数据框。API 设计遵循 Python 版并去掉 get_/set_ 前缀。面向 Ruby 开发者，以 Gem 安装，macOS 需另装 OpenMP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Learning API 与 scikit-learn 风格双接口（Regressor/Classifier）
- 支持模型 JSON 保存/加载、特征重要度、早停与交叉验证
- 数据输入支持数组、Numo::NArray 与 Rover 数据框
- 经 FFI 调用 XGBoost

## 适用场景

- 在 Ruby 应用中训练梯度提升回归/分类模型
- 加载已有 XGBoost 模型做预测
- 做交叉验证与早停调参

## 场景标签

 · 领域:机器学习

## 证据(README 行号)

> L3: XGBoost - high performance gradient boosting - for Ruby
> L35: booster = XGBoost.train(params, dtrain)

## 星数曲线

```mermaid
xychart-beta
    title "ankane/xgboost-ruby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-31 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ad13ed140478` · [字段定义](../../DATASET.md)*
