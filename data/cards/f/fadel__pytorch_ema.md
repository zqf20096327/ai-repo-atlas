# fadel/pytorch_ema

⭐ 446 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/fadel/pytorch_ema) · 个人维护

**PyTorch 小库：维护模型参数的指数移动平均**

用于在训练过程中维护模型参数（或任意参数集合）指数移动平均（EMA）的轻量 PyTorch 库。提供 store/copy_to/restore 手动切换与 average_parameters 上下文管理器两种用法，支持传入自定义参数迭代器，通过 state_dict/load_state_dict 序列化以支持训练中断与续训，并带 .to() 方法在不同设备与浮点精度间迁移内部状态。README 顶部提示可优先使用 PyTorch 内置的 torch.optim.swa_utils.AveragedModel，其维护更完善且处理批归一化等带权重依赖状态的模块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ExponentialMovingAverage 维护参数的指数移动平均（可设 decay）
- state_dict/load_state_dict 支持暂停、序列化与续训
- .to() 支持跨设备与浮点 dtype 迁移内部状态
- 方法可作用于任意兼容的参数迭代器，不限于构造时的模型参数

## 适用场景

- 训练深度学习模型时用 EMA 提升评估与推理参数
- 长周期训练中断后恢复 EMA 影子参数与更新计数
- 在 GPU 与 CPU 之间迁移 EMA 状态

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9: A small library for computing exponential moving averages of model
> L10: parameters.
> L50: By default the methods of `ExponentialMovingAverage` act on the model parameters the object was constructed with, b

## 星数曲线

```mermaid
xychart-beta
    title "fadel/pytorch_ema 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 445 --> 447
    line [446, 446]
```

2026-10-18 446 → 2026-10-22 446（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7a80a58b5c09` · [字段定义](../../DATASET.md)*
