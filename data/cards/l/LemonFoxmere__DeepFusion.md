# LemonFoxmere/DeepFusion

⭐ 18 · JavaScript · GPL-3.0 · 推送 2026-03-23 · [GitHub](https://github.com/LemonFoxmere/DeepFusion) · [官网](https://lemonfoxmere.github.io/DeepFusion) · 个人维护

**在浏览器画布上可视化搭建并训练神经网络的 Web 工具**

基于节点图（node graph）的神经网络可视化编辑器：在画布上以节点表示层（Input/Output/Dense），连线搭建网络，上传 CSV 格式的自定义训练/测试数据（或使用默认数据集），在浏览器内直接训练，支持设置 Epoch 与 Batch size，可测试并用未见过数据展示预测与真值，导出 TFJS 格式的模型结构（.json）与权重（.weights.bin）。作者声明项目仍处 Beta 阶段，功能持续增加中；导出后如需接入 Keras 等库需自行转换。面向不想写代码的神经网络学习与实验用户，以 GPL-3.0 许可分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 节点图画布搭建神经网络（Input/Output/Dense 层可配置连线）
- 上传 CSV 自定义数据集训练，或使用内置默认数据集
- 浏览器内直接训练，可调 Epoch 与 Batch size
- 导出 TFJS 模型结构 .json 与权重 .weights.bin 文件

## 适用场景

- 不写代码在画布上搭建和训练神经网络
- 用自己的 CSV 数据训练定制模型
- 学习实验神经网络结构并导出 TFJS 模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L66: DeepFusion uses a node graph system to make neural networks. This just means that layers will be represented as con
> L115: When the network has been trained or compiled without error, you may choose to export the network via the `Export 

## 星数曲线

```mermaid
xychart-beta
    title "LemonFoxmere/DeepFusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d9725280e78b` · [字段定义](../../DATASET.md)*
