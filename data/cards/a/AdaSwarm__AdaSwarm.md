# AdaSwarm/AdaSwarm

⭐ 18 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/AdaSwarm/AdaSwarm) · 组织维护

**面向深度学习研究者的 PyTorch 损失函数库：以粒子群近似梯度**

AdaSwarm 是基于同名 IEEE 论文的 PyTorch 损失函数库：在损失层运行内部粒子群仅评估损失、不做微分，近似损失对输出的梯度，再经链式法则传回标准优化器（如 Adam），训练循环其余不变。提供 BCELoss、CrossEntropyLoss 与通用 SwarmLoss 包装任意逐元素损失。适用场景为非凸多峰与不可微/黑盒损失（相位恢复、离散指标 F1/IoU/WER、PINN 等）。限制：每步成本随输出维度×群规模×迭代增长，不适于大 softmax 输出；光滑凸损失上无优势。要求 Python 3.10+、torch≥2.2。

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

- 内部粒子群仅评估损失、不做微分，近似梯度后交回标准优化器
- adaswarm.nn.SwarmLoss 可包装任意自定义/不可微逐元素损失
- 保留原有优化器与训练循环，仅替换 criterion 即可使用
- 提供与 Adam 的对照示例与 Colab 笔记本

## 适用场景

- 训练在欺骗性局部极小值处卡住的模型
- 直接优化不可微或黑盒指标（F1、AUC、IoU、WER）
- 周期性/多峰损失（相位恢复、DOA、姿态旋转）与 PINN 拟合

## 场景标签

 · 领域:深度学习/优化

## 证据(README 行号)

> L10: *AdaSwarm* is based on "AdaSwarm: Augmenting Gradient-Based optimizers in Deep Learning with Swarm Intelligence, _R
> L14: **AdaSwarm is a drop-in _loss function_.** You keep your normal optimiser (e.g. `Adam`) and your
> L59: AdaSwarm runs an internal particle swarm over the loss to approximate its gradient, then hands control

## 星数曲线

```mermaid
xychart-beta
    title "AdaSwarm/AdaSwarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f24e69eb0ca8` · [字段定义](../../DATASET.md)*
