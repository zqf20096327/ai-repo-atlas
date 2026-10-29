# dev-luigi/neural-network-digits

⭐ 42 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/dev-luigi/neural-network-digits) · 个人维护

**从零实现的手写数字识别神经网络，带可视化教学 GUI**

用纯 Python + NumPy 从零实现的多层神经网络（约 140 行，含前向、softmax、交叉熵、带动量的 SGD、L2、dropout），学习 MNIST 手写数字识别，不依赖 PyTorch/TensorFlow。提供 Tkinter 五标签页教学界面：实时查看损失曲线与权重分布、训练中调整超参数、逐神经元逐单元格查看网络内部计算，另有画板试画与神经元编辑。内置助手基于 TF-IDF 检索与规则，明确声明不使用语言模型。支持 pip/pipx、zip 双击与终端命令安装，界面提供英语与意大利语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 NumPy 从零实现网络（前向/反向传播/SGD momentum/L2/dropout/4 种激活函数）
- 训练中可实时调整超参数，可视化权重高斯分布与逐层 PCA/t-SNE 点图
- 逐单元格展示网络数学（加权求和、激活、softmax 步骤），可编辑单个神经元的偏置与权重
- 内置助手为 TF-IDF 检索 + 规则引擎，非语言模型

## 适用场景

- 学习神经网络内部机制：反向传播、激活函数、正则化的直观演示
- 在画板上画数字并观察各神经元激活与预测
- 通过终端命令下载数据、训练与评估同一套流程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L25: A small neural network written **from scratch in Python + NumPy** (no PyTorch or TensorFlow) that learns
> L26: to recognize the handwritten digits of the MNIST dataset, with an **educational graphical interface** to
> L115: It is not a language model, on purpose: the answers come from a small search engine (TF-IDF, written in NumPy

## 星数曲线

```mermaid
xychart-beta
    title "dev-luigi/neural-network-digits 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-29 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6aae3bc539e1` · [字段定义](../../DATASET.md)*
