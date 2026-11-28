# ml-rust/treeboost

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-13 · [GitHub](https://github.com/ml-rust/treeboost) · 个人维护

**面向表格数据的 Rust 梯度提升树训练与推理库**

TreeBoost 是用 Rust 实现的表格数据梯度提升库，训练 GBDT、线性+树混合模型与随机森林，支持时间序列、缺失值、混合特征类型与多标签目标。提供三层 API（AutoModel 自动选模式、UniversalModel 中层配置、GBDTModel 底层控制），后端按 CUDA/WGPU/AVX-512/SVE2/Scalar 自动选择。输入 CSV/Parquet/polars DataFrame，输出 rkyv/TRB 模型文件，附带 CLI 与 Python 绑定（后者需从源码构建）。不支持导出 ONNX 或 XGBoost 格式，Python 侧不覆盖 AutoModel 与 UniversalModel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AutoModel 一次调用训练基线并报告所选模式
- 五种后端自动选择：CUDA、WGPU、AVX-512、SVE2、Scalar
- TRB 模型文件支持增量学习与更新前漂移检查
- conformal prediction 输出预测区间

## 适用场景

- 对表格数据训练基线模型并自动选择提升模式
- 用 CLI 对 CSV/Parquet 数据做训练与预测
- 时间序列趋势场景使用线性+树混合模式
- 需要模型随数据增量更新并带漂移检查

## 场景标签

 · 领域:机器学习/表格数据建模

## 证据(README 行号)

> L38: TreeBoost is a gradient boosting library for tabular data, in Rust. It trains gradient-boosted decision trees, line
> L7: Trains a baseline model in one call and exposes full control over boosting modes, configs, and backends. Backends: S


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c6a958658f7c` · [字段定义](../../DATASET.md)*
