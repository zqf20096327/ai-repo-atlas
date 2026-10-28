# federhub/ST_DeepLearning

⭐ 33 · Jupyter Notebook · 推送 2026-06-24 · [GitHub](https://github.com/federhub/ST_DeepLearning) · 组织维护

**环境数据时空预测框架：EOF 分解+深度网络重建时间序列**

论文配套代码（Scientific Reports 2020）：将时空场经 SVD/EOF 分解为时间基函数与空间系数，训练前馈神经网络映射空间坐标到系数，在新位置重建完整时间序列。提供两个实验：内置模拟数据（高斯随机场+AR(1)）与瑞士小时温度数据（不随仓库分发，需联系作者获取）。通过 uv 安装，支持 CLI 与 Python API，输出预测 npy、统计 CSV 与 Keras 模型文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SVD/EOF 时空分解+深度前馈网络的预测框架
- 内置模拟数据端到端复现实验
- CLI 与 Python API 双入口
- 提供论文图表复现 notebook

## 适用场景

- 环境/气候时空数据的站点预测
- 复现论文实验结果
- 作为时空插值方法的研究基线代码

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: `stdl` decomposes a spatio-temporal field into temporal basis functions (via SVD/EOF analysis) and spatial coeffici
> L5: > **A Novel Framework for Spatio-Temporal Prediction of Environmental Data Using Deep Learning**

## 星数曲线

```mermaid
xychart-beta
    title "federhub/ST_DeepLearning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b0160b7d3b03` · [字段定义](../../DATASET.md)*
