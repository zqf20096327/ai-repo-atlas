# NEGU93/cvnn

⭐ 198 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/NEGU93/cvnn) · [官网](https://complex-valued-neural-networks.readthedocs.io/) · 个人维护

**TensorFlow 后端的复数值神经网络 Python 库**

以 TensorFlow 为后端实现复数值神经网络的 Python 库：提供 cvnn.layers 模块替代 tf.keras.layers，使用真正的复数数据类型而非以实数向量模拟实部虚部，支持 Sequential 与 Functional 两种 API。供从事复数域深度学习（如作者本人的复数神经网络博士课题）的开发者与研究者使用。作者声明库已停止维护、与 TF 2.16+ 不兼容，欢迎他人接手维护。安装提供 conda 与 pip 两种方式。

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

- 使用真正的复数数据类型而非实数向量模拟
- cvnn.layers 替代 tf.keras.layers，代码写法与 TensorFlow 基本一致
- 支持 Sequential API 与 Functional API 两种建模方式

## 适用场景

- 处理复数数据（如雷达、通信信号）的深度学习建模
- 在 TensorFlow 中搭建复数值层的网络
- 复数神经网络方向的科研实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: This is a library that uses Tensorflow as a back-end to do complex-valued neural networks as CVNNs are barely suppo
> L9: Using this library, the only difference with a Tensorflow code is that you should use `cvnn.layers` module instead o

## 星数曲线

```mermaid
xychart-beta
    title "NEGU93/cvnn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 197 --> 199
    line [198, 198]
```

2026-10-18 198 → 2026-10-30 198（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `51c564b82d92` · [字段定义](../../DATASET.md)*
