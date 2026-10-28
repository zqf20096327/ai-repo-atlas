# sradc/SmallPebble

⭐ 135 · Python · Apache-2.0 · 推送 2026-01-19 · [GitHub](https://github.com/sradc/SmallPebble) · 个人维护

**极简自动微分与深度学习教学库，纯 Python/NumPy 实现**

面向学习者的深度学习库：核心实现集中在单个文件 smallpebble.py，唯一依赖为 NumPy，在 NumPy 数组上运行自动微分。通过 Python 对象引用隐式构建动态计算图（类似 PyTorch 的方式），调用 get_gradients 时反向遍历图求梯度。支持 matmul、conv2d、maxpool2d 与数组广播，支持立即执行与惰性图构建，提供自定义操作 API；核心逻辑不足 1000 行，不含性能优化与 GPU 支持，仅 CPU 运行。README 附 MNIST 与 CIFAR-10 训练示例及使用指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心实现为单文件，唯一依赖 NumPy，核心逻辑 <1000 行
- 基于动态计算图的自动微分（get_gradients 反向遍历求梯度）
- 支持 matmul/conv2d/maxpool2d/数组广播与自定义操作 API
- 支持立即执行与 sp.Lazy 惰性图构建两种方式

## 适用场景

- 阅读源码与测试理解深度学习框架底层概念
- 在 CPU 上用轻量环境搭建和训练小型神经网络
- 教学场景演示自动微分与计算图构建原理

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: SmallPebble is a minimalist autodiff and deep learning library written from scratch in Python.
> L14: SmallPebble demonstrates the key concepts under the hood of deep learning frameworks,

## 星数曲线

```mermaid
xychart-beta
    title "sradc/SmallPebble 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-28 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ef1241d871c3` · [字段定义](../../DATASET.md)*
