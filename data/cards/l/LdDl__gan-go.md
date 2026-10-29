# LdDl/gan-go

⭐ 87 · Go · 推送 2026-08-19 · [GitHub](https://github.com/LdDl/gan-go) · 个人维护

**Go 语言 GAN 示例库：用 Gorgonia 构建生成对抗网络**

基于 Gorgonia 机器学习库的 Go 语言 GAN 示例仓库：提供生成器与判别器对抗训练的实现，用于学习生成 f(x)=x^2、sin(x) 等函数的数据分布。附带线性、卷积、池化、LSTM、RNN、GRU 等多种层类型封装（部分层与示例不属 GAN 主题，仅演示用相同抽象构建其他网络）。作者声明不定位为高层机器学习框架。通过 git clone 后进入 cmd/examples 目录以 go run 运行各示例，输出训练过程与最终生成数据的 PNG 图像。

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

- 用 Gorgonia 实现 Generator/Discriminator 对抗训练
- 示例生成 x^2、sin(x) 等函数分布并输出 PNG 图像
- 提供线性/卷积/池化/LSTM/RNN/GRU 等层类型封装
- 包含 train_cnn/train_lstm/train_gru 等非 GAN 示例程序

## 适用场景

- 在 Go 生态中学习 GAN 的构建方式
- 参考如何用相同抽象搭建 CNN、RNN 等其他网络
- 观察 GAN 训练过程中生成数据逐轮变化

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: **Recipe for simple GAN in Golang ecosystem via Gorgonia library**
> L11: This just a repository with simple example how to build GAN in Gorgonia

## 星数曲线

```mermaid
xychart-beta
    title "LdDl/gan-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-29 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `cb86d8213bad` · [字段定义](../../DATASET.md)*
