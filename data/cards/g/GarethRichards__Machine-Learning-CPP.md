# GarethRichards/Machine-Learning-CPP

⭐ 130 · C++ · Unlicense · 推送 2026-08-09 · [GitHub](https://github.com/GarethRichards/Machine-Learning-CPP) · 个人维护

**用现代 C++17 复现 Nielsen 深度学习书的神经网络代码**

将 Michael Nielsen《Neural Networks and Deep Learning》一书的 Python 代码移植为 C++17，分章节对应：第 1 章为单文件 network.py 的 Python 风格移植，第 3 章改写为头文件形式的库并使用策略类，实现随机梯度下降训练，可识别 MNIST 手写数字。线性代数依赖 Boost uBLAS，展示 STL 算法、lambda、结构化绑定等现代 C++ 特性。代码单线程运行，作者自述为学习与实验用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 Nielsen 书中 network.py / network2.py 的 C++17 移植
- 实现随机梯度下降与反向传播，可识别 MNIST 手写数字
- 第 3 章代码组织为头文件库并使用策略类
- 线性代数使用 uBLAS，其余仅依赖 C++ 标准库

## 适用场景

- 对照原书用 C++ 学习神经网络原理
- 参考现代 C++（STL 算法/lambda/结构化绑定）实现机器学习代码
- 实验手写数字识别的小型代码库

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L16: tried to showcase some of the new features of Modern C++ here, STL algorithms and lambda functions. With just a cou
> L3: The C++ code in this repository is a hopefully accurate port of the python code in Michael Nielsen's book

## 星数曲线

```mermaid
xychart-beta
    title "GarethRichards/Machine-Learning-CPP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-28 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ba96f8a1f780` · [字段定义](../../DATASET.md)*
