# lucidrains/adam-atan2-pytorch

⭐ 145 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/lucidrains/adam-atan2-pytorch) · 个人维护

**Adam-atan2 优化器的 PyTorch 实现，供深度学习训练使用**

用 PyTorch 实现 Google DeepMind 论文提出的 Adam-atan2 优化器：在 Adam 更新规则中改用 atan2，去掉 epsilon 以获得数值稳定性与尺度不变性；并附带持续学习领域的可塑性改进特性。以 Python 包形式提供，pip 安装后可直接作为 PyTorch 训练循环中的优化器使用，README 附使用示例与多篇相关论文引用。

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

- 以 atan2 替换 Adam 更新规则，移除 epsilon
- 提供数值稳定性与尺度不变性
- 包含持续学习场景的可塑性改进特性
- pip 安装，作为 PyTorch 优化器直接使用

## 适用场景

- 深度学习训练中替换默认 Adam 优化器
- 需要尺度不变更新的训练任务
- 持续学习场景下维持模型可塑性

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: Implementation of the proposed Adam-atan2 optimizer in Pytorch
> L7: A multi-million dollar paper out of google deepmind proposes a small change to Adam update rule (using `atan2`) to r

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/adam-atan2-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-28 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e2f5efdf9d1e` · [字段定义](../../DATASET.md)*
