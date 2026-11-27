# williamgilpin/convoca

⭐ 89 · Python · 推送 2026-11-26 · [GitHub](https://github.com/williamgilpin/convoca) · 个人维护

**用卷积神经网络预测与分析元胞自动机规则**

基于 PyTorch 的科研代码库：用 CNN 实现已知元胞自动机（CA）规则集，并能以图像序列为训练数据学习未知 CA 规则。网络首层为可训练卷积滤波器提取细胞邻域信息，后续层用重复 1x1 卷积实现 CA 规则，末层 softmax 输出细胞状态；提供可选的径向对称卷积层与周期边界条件层。附 Jupyter 演示 notebook 与 benchmark 模块，配套 2019 年 Physical Review E 论文。使用 uv 安装运行，要求 Python>=3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以图像序列为训练数据学习未知元胞自动机规则
- 可训练卷积滤波器提取细胞邻域，1x1 卷积实现 CA 规则
- 可选 SymmetricConvolution 层与 Wraparound2D 周期边界层
- 提供 simulation/training/inference benchmark 与演示 notebook

## 适用场景

- 训练网络复现 Conway's Game of Life 等已知规则
- 从图像序列中推断未知元胞自动机的规则
- 对 CA 的模拟、训练与推理做性能基准测试

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Demonstrate and learn cellular automata using convolutional neural networks in PyTorch
> L8: This code both implements and analyzes known CA rulesets using PyTorch, and it also learns the rules of unknown CA g
> L16: Models are instantiated using the `initialize_model(...)` function, which builds a network with a trainable convolu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `c643feebf140` · [字段定义](../../DATASET.md)*
