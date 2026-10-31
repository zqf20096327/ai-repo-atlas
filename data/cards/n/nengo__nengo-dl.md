# nengo/nengo-dl

⭐ 95 · Python · NOASSERTION · 推送 2026-08-02 · [GitHub](https://github.com/nengo/nengo-dl) · [官网](https://www.nengo.ai/nengo-dl) · 组织维护

**基于 TensorFlow 的 Nengo 脉冲神经网络模拟器与训练工具**

NengoDL 是 Nengo 神经网络模型的模拟器，底层使用 TensorFlow 执行，用户只需将标准 Nengo 模型中的 Simulator 类替换为 nengo_dl.Simulator 即可运行。在此之上增加深度学习训练（通过 Keras API 优化模型参数）、CPU 与 GPU 加速仿真、Keras 模型到 Nengo 网络的自动转换，以及将 TensorFlow 代码嵌入 Nengo 模型的能力。面向使用 Nengo 构建脉冲神经网络并结合深度学习方法的研究者与开发者，以 Python 包形式分发，安装与教程见官方文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 TensorFlow 后端模拟 Nengo 网络，仅需替换 Simulator 类
- 通过 Keras API 以深度学习方法优化模型参数
- Keras 模型到 Nengo 网络的自动转换与 TensorFlow 代码嵌入
- CPU 与 GPU 上的加速仿真

## 适用场景

- 在 Nengo 脉冲神经网络模型上应用深度学习训练
- 将已有 Keras 模型转换为 Nengo 网络做神经形态计算
- 在 GPU 上加速 Nengo 模型仿真

## 场景标签

 · 领域:神经科学/机器学习工具

## 证据(README 行号)

> L18: NengoDL is a simulator for `Nengo <https://www.nengo.ai/nengo/>`_ models.
> L20: that network using some underlying computational framework (in this case,
> L50: - optimizing the parameters of a model through deep learning

## 星数曲线

```mermaid
xychart-beta
    title "nengo/nengo-dl 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 93 --> 96
    line [94, 95, 95]
```

2026-10-18 94 → 2026-10-31 95（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `636dc7633d1a` · [字段定义](../../DATASET.md)*
