# stmluyuer/CNN-BILISTM

⭐ 18 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/stmluyuer/CNN-BILISTM) · 个人维护 · 中文 README

**CNN+BiLSTM/LSTM 时间序列预测的早期实验代码**

个人早期练习仓库：用 Keras 构建 CNN+BiLSTM 模型从历史数据预测后续数值，另含一个 LSTM 加多项式特征工程的模型。代码覆盖数据预处理、训练、评估与 Matplotlib 可视化，训练时使用 EarlyStopping 与 ReduceLROnPlateau。脚本从工作目录读取 data.csv，输入列与训练行数（前 1190 行）为硬编码；作者自述模型较基础、代码保留拼音命名，更换数据需核对硬编码设置，且未固定 Keras 计算后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CNN+BiLSTM 与 LSTM 两种模型的时间序列预测实现
- 多项式特征生成 + 随机森林特征重要性筛选
- EarlyStopping 与 ReduceLROnPlateau 训练策略，MSE 损失
- 动态/静态两种预测脚本的评估图

## 适用场景

- 学习 CNN+BiLSTM 时间序列建模的代码结构
- 参考特征工程与训练回调的用法
- 在自己数据上复跑实验（需核对硬编码列与行数）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: 这是我早期做的时间序列预测实验，用卷积神经网络（CNN）和双向长短期记忆网络（BiLSTM）从历史数据中提取特征、预测后续数值。仓库包含数据预处理、模型训练、评估和结果可视化的代码。
> L9: CNN + BiLSTM 是初期测试用的基础模型。模型用 Python 的 Keras 构建，Pandas、NumPy 处理数据，Scikit-learn 做标准化，Matplotlib 绘图，SciPy 做统计分析。只用 Scik

## 星数曲线

```mermaid
xychart-beta
    title "stmluyuer/CNN-BILISTM 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-24 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d71e30c3babf` · [字段定义](../../DATASET.md)*
