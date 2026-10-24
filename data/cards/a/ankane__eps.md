# ankane/eps

⭐ 693 · Ruby · MIT · 推送 2026-10-17 · [GitHub](https://github.com/ankane/eps) · 个人维护

**Ruby 机器学习库：快速构建并部署预测模型**

面向 Ruby/Rails 开发者的机器学习库：以数组、Rover 数据框、Numo 数组等格式传入数据，训练 LightGBM（默认）、线性回归或朴素贝叶斯模型，输出回归或分类预测。模型以 PMML 标准格式存储，可加载 Python（sklearn2pmml）、R（pmml 包）等语言构建的模型并在 Ruby 中服务。内置训练/验证集划分与性能报告（RMSE/准确率），支持文本特征、权重、概率输出与预测监控，Rails 场景下推荐 app/ml_models 组织方式及数据库存储模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 LightGBM（默认）、线性回归、朴素贝叶斯三种算法
- 模型以 PMML 标准格式存储，可服务 Python/R 等语言构建的模型
- 数据点≥30 时自动划分训练/验证集并报告 RMSE 或准确率
- 支持数值/类别/文本特征与数据点权重

## 适用场景

- 在 Rails 应用中构建并部署预测模型（如房价预测）
- 将 Python 或 R 训练的模型以 PMML 部署到 Ruby 服务中
- 对模型预测结果做持续监控与指标告警

## 场景标签

 · 领域:机器学习/数据科学

## 证据(README 行号)

> L3: Machine learning for Ruby
> L40: model.predict(bedrooms: 2, bathrooms: 1)
> L197: Eps makes it easy to serve models from other languages. You can build models in Python, R, and others and serve th

## 星数曲线

```mermaid
xychart-beta
    title "ankane/eps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 692 --> 694
    line [693, 693]
```

2026-10-18 693 → 2026-10-24 693（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `0fa5608f0848` · [字段定义](../../DATASET.md)*
