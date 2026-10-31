# 77axel/PyCNN

⭐ 22 · Python · MIT · 推送 2026-06-14 · [GitHub](https://github.com/77axel/PyCNN) · [官网](https://77axel.github.io/PyCNN/) · 个人维护

**纯 NumPy/Cython 从零实现的 Python CNN 构建训练库**

不依赖 TensorFlow/PyTorch 等深度学习框架、仅用 NumPy/PIL/SciPy/Cython 从零实现的卷积神经网络 Python 库，支持多分类训练、模型保存加载、CUDA 加速与 Adam 优化器、CPU/GPU 后端切换、Hugging Face 数据集读取与数据增强，并可将模型导出为 PyTorch 格式。面向需要构建、训练、测试 CNN 模型的开发者；常规使用自动下载预编译二进制，无需本地编译器，源码构建需 C++ 编译器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无深度学习框架，仅基于 NumPy/PIL/SciPy/Cython 实现 CNN
- CUDA 加速（CuPy）与 Adam 优化器，CPU/GPU 后端切换
- 支持 Hugging Face 数据集与本地数据集训练、数据增强
- PyTorch 模型导出与实时训练可视化

## 适用场景

- 在本地数据集文件夹上训练图像分类模型
- 不引入大框架的前提下实验 CNN 训练流程
- 把训练好的模型导出到 PyTorch 继续使用

## 场景标签

`模型训练` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L15: This is a Convolutional Neural Network (CNN) library project implemented entirely from scratch using only low-level
> L1: PyCNN Logo A Python library to easily build, train, and test your CNN AI models.

## 星数曲线

```mermaid
xychart-beta
    title "77axel/PyCNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `96b0a99c4c9c` · [字段定义](../../DATASET.md)*
