# H21lab/Anomaly-Detection

⭐ 84 · Jupyter Notebook · Apache-2.0 · 推送 2026-03-01 · [GitHub](https://github.com/H21lab/Anomaly-Detection) · [官网](https://www.h21lab.com/tools/anomaly-detection) · 个人维护

**检测 pcap 文件异常的脚本集：TensorFlow 神经网络与 tshark**

H21 lab 维护的网络流量异常检测脚本集合，面向分析 pcap 文件的安全/网络监控场景。提供三种方式：基于 TensorFlow 自编码器的无监督检测（notebook 形式）、基于 TensorFlow 神经网络分类器的有监督检测，以及不依赖机器学习、仅用 tshark 的简单检测脚本。输入为 tshark -T ek -x 生成的 JSON。README 提及后续在线应用 logs-analyzer。程序按无担保方式分发。

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

- TensorFlow 自编码器无监督异常检测（notebook）
- TensorFlow 神经网络分类器有监督检测
- 仅用 tshark 的简单检测脚本（无 ML 依赖）
- 输入为 tshark ek json 格式

## 适用场景

- 分析 pcap 抓包文件中的异常网络流量
- 用无监督方法在无标注数据下检测异常
- 对网络流量做基于神经网络的分类监控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: # Unsupervised Anomaly Detection using tensorflow and tshark
> L15: Using tensorflow neural network classifier and tshark -T ek -x input.

## 星数曲线

```mermaid
xychart-beta
    title "H21lab/Anomaly-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-24 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a10452107165` · [字段定义](../../DATASET.md)*
