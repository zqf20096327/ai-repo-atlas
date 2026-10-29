# delvendahl/miniML

⭐ 31 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/delvendahl/miniML) · [官网](https://delvendahl.github.io/miniML/) · 组织维护

**神经科学工具：深度学习检测突触事件（mEPSC 等）**

基于 CNN-LSTM 网络的突触事件检测工具：对一维时间序列电生理数据（如小脑苔藓纤维-颗粒细胞突触的 mEPSC 记录）运行模型推理，自动检出突触事件并计算描述性统计。支持直接读取 HEKA .dat、Axon .abf 与 HDF .h5 文件，结果可存为 .h5 或 .csv；提供 PyQt5 图形界面与教程 Notebook，仓库附带预训练模型和示例数据。需要 Python 3.11，建议使用 TensorFlow 2.14/2.15（Keras 3 存在加载兼容问题），GPU 推理需 CUDA 或 tensorflow-metal。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN-LSTM 网络检测一维时间序列中的突触事件
- 支持 HEKA .dat / Axon .abf / HDF .h5 直接加载
- 提供 GUI（数据加载、预处理、事件检视与删除）
- 附预训练模型与训练 Notebook（含 Kaggle 云端训练）

## 适用场景

- 我在电生理记录中自动检测 mEPSC 等突触事件并做统计分析
- 我已有 HEKA/ABF 格式的膜片钳数据，想直接加载分析
- 我想在示例数据或 Kaggle 上训练自己的检测模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: miniML is a deep-learning-based tool to detect synaptic events in 1d time-series data. It uses a CNN-LSTM network a
> L15: In this repository, we provide documentation, pre-trained models, and Python code to run model inference on recorde

## 星数曲线

```mermaid
xychart-beta
    title "delvendahl/miniML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b395e6ab36fa` · [字段定义](../../DATASET.md)*
