# ggsharma/microgradpp

⭐ 16 · C++ · GPL-3.0 · 推送 2026-01-14 · [GitHub](https://github.com/ggsharma/microgradpp) · 个人维护

**C++17 自动微分引擎与神经网络库，学习反向传播**

受 Karpathy micrograd 启发的纯 C++ 机器学习库：实现基于动态构建计算图的反向模式自动微分引擎，其上提供 Value、MLP、Tensor 等类以及 ReLU/Tanh/Sigmoid 等激活函数，用于构建和训练神经网络。可经 CMake 编译，也可作为 header-only 库直接包含头文件使用；提供 MLP 训练与 OpenCV 图像训练示例，OpenCV 为可选依赖。面向学习机器学习与 C++ 的开发者，GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向模式自动微分引擎，动态构建计算图
- 支持 header-only 方式集成与 CMake 构建
- Tensor 类与多种激活函数（ReLU/Tanh/Sigmoid）
- OpenCV 集成的图像神经网络示例

## 适用场景

- 用现代 C++ 学习反向传播与神经网络原理
- 在 C++ 项目中以 header-only 方式嵌入小型神经网络
- 运行 MLP 训练与图像学习示例

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L26: **microgradpp** (micrograd++) is a C++ implementation of an automatic differentiation (autograd) engine with a neur
> L39: * ✅ **Pure C++**: Entirely implemented in C++ for high performance

## 星数曲线

```mermaid
xychart-beta
    title "ggsharma/microgradpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `86545e8a25a7` · [字段定义](../../DATASET.md)*
