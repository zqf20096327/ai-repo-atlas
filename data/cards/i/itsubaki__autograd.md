# itsubaki/autograd

⭐ 27 · Go · MIT · 推送 2026-10-17 · [GitHub](https://github.com/itsubaki/autograd) · [官网](https://pkg.go.dev/github.com/itsubaki/autograd) · 个人维护 · 中文 README

**Go 语言实现的自动微分库，支持反向传播与梯度下降**

itsubaki/autograd 是用 Go 编写的自动微分库，提供 variable 与函数式 API（F.Pow/F.Sin 等），支持反向传播（Backward）、复合函数求导、梯度下降、双重反向传播（double backpropagation）、NoGrad 与 Test 模式，并附 Deep Learning 示例（DataLoader、批量训练）。另提供 dot graph 命令，配合 graphviz 生成计算图可视化。面向需要在 Go 中构建与训练神经网络或求导的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反向传播、复合函数求导与梯度下降
- 支持双重反向传播（double backpropagation）
- NoGrad 与 Test 模式控制计算行为
- dot graph 命令生成计算图可视化（需 graphviz）

## 适用场景

- 在 Go 项目中实现神经网络前向/反向计算
- 对复合函数做高阶求导
- 以图形方式检查计算图结构

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: An automatic differentiation library in Go.
> L37: ### Deep Learning

## 星数曲线

```mermaid
xychart-beta
    title "itsubaki/autograd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-30 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1656fbb70db4` · [字段定义](../../DATASET.md)*
