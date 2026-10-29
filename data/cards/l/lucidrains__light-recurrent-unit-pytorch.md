# lucidrains/light-recurrent-unit-pytorch

⭐ 51 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/lucidrains/light-recurrent-unit-pytorch) · 个人维护

**Light Recurrent Unit 的 PyTorch 实现，供研究者使用**

该仓库以 PyTorch 实现论文《Light Recurrent Unit: Towards an Interpretable Recurrent Neural Network for Modeling Long-Range Dependency》提出的循环神经网络单元，供序列建模研究者使用。提供单层（Cell/Layer）、堆叠及多头（heads>1，K 个候选在门控前 softmax 选择）三种用法接口；附带 Enwik8 数据集上的训练测试脚本（python train.py），通过 pip 以 light-recurrent-unit-pytorch 包名安装。README 另引用 Merrill 等关于状态空间模型状态假象的论文。

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

- 提供 LightRecurrentUnitCell / Layer / 堆叠三层接口
- 多头机制：heads>1 时 K 个并行候选在门控前 softmax 选择
- 附带 Enwik8 训练测试脚本

## 适用场景

- 在序列建模任务中试验 Light Recurrent Unit 结构
- 复现或对比论文中的长程依赖建模方法

## 场景标签

 · 领域:深度学习/循环神经网络

## 证据(README 行号)

> L5: Implementation of the Light Recurrent Unit in Pytorch
> L64:     TITLE   = {Light Recurrent Unit: Towards an Interpretable Recurrent Neural Network for Modeling Long-Range Depe

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/light-recurrent-unit-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ab686ce68e88` · [字段定义](../../DATASET.md)*
