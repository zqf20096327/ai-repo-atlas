# tommasocarraro/LTNtorch

⭐ 164 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/tommasocarraro/LTNtorch) · [官网](https://tommasocarraro.github.io/LTNtorch/) · 个人维护

**Logic Tensor Networks 的 PyTorch 实现：用逻辑公理指导神经网络训练**

LTNtorch 是逻辑张量网络（LTN）的 PyTorch 实现。LTN 是神经-符号框架：将一阶逻辑知识库中的公理作为可满足性目标，构造损失函数指导（深层）神经网络训练；通过可微分的一阶逻辑语言 Real Logic 将逻辑符号映射为张量或张量运算，逻辑连接词用模糊逻辑语义接地、量词用模糊聚合器接地，最终转换为 PyTorch 计算图。面向从事神经-符号计算、半监督学习与知识约束学习的研究者与开发者，提供 pip 安装、Jupyter 教程与七类示例（分类、回归、聚类、嵌入学习等），核心模块单测覆盖 100%。

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

- 一阶逻辑公式的可满足性作为损失函数训练神经网络
- 可微分逻辑语言 Real Logic：符号接地为张量/张量运算
- 逻辑连接词用模糊语义、量词用模糊聚合器接地
- 含教程与分类/回归/聚类/嵌入学习等七类 Jupyter 示例

## 适用场景

- 在分类、回归等任务中引入先验逻辑约束做训练
- 半监督学习：用逻辑公理补充标注数据不足
- 学习可解释的逻辑常量嵌入，训练后对新数据查询谓词与公式真值

## 场景标签

 · 领域:机器学习/神经符号计算

## 证据(README 行号)

> L15: Logic Tensor Network (LTN) is a Neural-Symbolic (NeSy) framework which supports learning of neural networks using t
> L24: The idea is to use the logical axioms as a loss function for our Logic Tensor Network. The objective is to find sol

## 星数曲线

```mermaid
xychart-beta
    title "tommasocarraro/LTNtorch 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-27"]
    y-axis "stars" 162 --> 165
    line [163, 164, 164]
```

2026-10-23 163 → 2026-10-27 164（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c80a767272a9` · [字段定义](../../DATASET.md)*
