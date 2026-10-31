# neuromodulation/py_neuromodulation

⭐ 81 · Python · MIT · 推送 2026-02-04 · [GitHub](https://github.com/neuromodulation/py_neuromodulation) · [官网](https://neuromodulation.github.io/py_neuromodulation/) · 组织维护

**颅内神经电生理记录的实时特征提取 Python 工具箱**

面向神经数据分析的 Python 库：输入时间序列数据与采样频率，通过 Stream 接口输出 pandas.DataFrame 格式的时序特征，包括 fft/stft/带通带功率、temporal waveform shape、fooof、mne_connectivity、Hjorth 参数、非线性动力学估计、burst 特征与线长等。内部流式结构模拟在线数据流，理论上可连接硬件采集系统。原始目标是脑植入物患者的运动解码，提供常用机器学习方法的封装。需 Python 3.12 以上，支持 pip 或源码 uv 安装。

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

- 仅需时间序列与采样频率即可进行特征提取
- Stream 接口模拟在线数据流，可对接硬件采集系统
- 涵盖 fft/stft/带功率、fooof、连接性、Hjorth、非线性动力学等多种特征
- 提供常用机器学习方法的封装用于神经解码

## 适用场景

- 我从颅内脑电（ECoG/LFP）记录中提取时序神经特征
- 我做侵入式脑机接口的运动解码研究
- 我需要模拟在线数据流的实时神经信号分析

## 场景标签

 · 领域:神经科学/计算神经工程

## 证据(README 行号)

> L11: and beginner unfriendly process. *py_neuromodulation* allows using a simple
> L35: *py_neuromodulation* offers wrappers around common practice machine learning methods for efficient analysis.

## 星数曲线

```mermaid
xychart-beta
    title "neuromodulation/py_neuromodulation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-31 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a477685378c0` · [字段定义](../../DATASET.md)*
