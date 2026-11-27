# Furkanbeker/learning-assisted-dab-tdoa

⭐ — · [GitHub]() · 个人维护

**DAB 信号机会 TDOA 无人机定位论文的代码与数据集**

IEEE Access 论文的配套仓库，包含 MATLAB 数据集生成脚本、Python 训练/评测流水线与仿真数据集。接收机中心式 TDOA 方案以参考接收机抵消发射机时偏，再以机器学习（XGBoost、ExtraTrees、HistGradientBoosting 集成）在位置域、测量域与紧耦合 CT-EKF 中做校正，测试集平均定位误差从 16.39 m 降至 3.95 m。提供 Git LFS 存储的 IQ 数据与 1.16 GB/820 MB gzip 分片表格，附 SHA-256 校验与固定随机种子以保证可复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MATLAB 数据集生成脚本与 Python 评测流水线完整可复现（种子固定、场景不重叠划分）
- B3-Ensemble：XGBoost/ExtraTrees/HistGradientBoosting 均值预测每链路测量噪声尺度
- 提供 1,500 场景测试集结果表与论文图表生成脚本
- 附 ADALM-PLUTO SDR 空中发射实测验证

## 适用场景

- 复现论文中的 DAB 信号机会 TDOA 定位实验结果
- 用自己的 CSV 数据集运行学习辅助定位校正流水线
- 基于 MATLAB 脚本生成新的 TDOA 仿真场景数据

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3: Code, dataset and results of the paper
> L13: (receiver-centric TDOA). Learning-assisted corrections are then applied in the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `b036880488db` · [字段定义](../../DATASET.md)*
