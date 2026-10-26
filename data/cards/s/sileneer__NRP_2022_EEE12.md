# sileneer/NRP_2022_EEE12

⭐ 79 · Jupyter Notebook · MIT · 推送 2026-07-17 · [GitHub](https://github.com/sileneer/NRP_2022_EEE12) · 个人维护

**用 LSTM/GRU 预测锂离子电池健康状态（SOH）的深度学习项目**

基于 PyTorch 的锂离子电池 SOH（健康状态）预测框架，实现 LSTM 与 GRU 两种循环神经网络并训练对比。使用牛津电池退化数据集 1（约 262MB .mat 文件，需自行下载并放入 datasets 目录），通过 Jupyter Notebook（main_torch.ipynb）加载数据、归一化预处理、训练模型并生成预测与可视化。README 报告 GRU 模型平均 RMSE 为 0.724%。面向电池健康管理方向的科研与工程开发者，运行需 Python 3.10+、建议 4GB 内存与 500MB 磁盘空间。

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

- LSTM 与 GRU 双模型实现与训练对比
- 使用开源 Oxford Battery Degradation Dataset 1 真实退化数据
- README 报告 GRU 模型平均 RMSE 0.724%
- 以 Jupyter Notebook 形式提供端到端流程

## 适用场景

- 我想训练模型预测锂离子电池的 SOH
- 我想比较 LSTM 与 GRU 在电池退化数据上的表现
- 我想复现基于公开数据集的电池健康监测实验

## 场景标签

 · 领域:能源/电池健康管理

## 证据(README 行号)

> L13: **We propose a simple yet effective machine learning framework utilizing Long Short-Term Memory (LSTM) and Gated Re
> L18: - 🧠 **Deep Learning Models**: Implementation of LSTM and GRU architectures

## 星数曲线

```mermaid
xychart-beta
    title "sileneer/NRP_2022_EEE12 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-26 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b2a36f5f72cc` · [字段定义](../../DATASET.md)*
