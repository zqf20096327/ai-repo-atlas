# Javihaus/ndt

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Javihaus/ndt) · 个人维护

**训练期神经网络表征维度监测与检测器效度验证库**

面向 PyTorch 用户的 Python 库：通过挂钩采样各层激活，训练中高频记录 participation_ratio、stable_rank 等四个维度指标，用于观察表征是否坍缩；同时提供效度验证框架，将任意跃迁检测器跑在受控真值轨迹与纯噪声空对照上，输出召回率、误报率与 PASS/FAIL 报告。效度框架纯 NumPy 实现无需 GPU。基准涵盖 55 次训练、30,147 次测量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三行代码为任意 PyTorch 模型附加四指标逐层维度追踪
- 检测器效度验证：真值对照+空对照+渲染报告与 PASS/FAIL 判定
- 效度框架纯 NumPy，无 GPU 也可运行
- 基准：55 次训练 30,147 次测量的检测器对比结果

## 适用场景

- 自监督/对比学习训练中监控表征坍缩
- 在采信训练曲线跃迁结论前验证检测器误报率
- 逐层观察模型训练中的表征几何变化

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L19: :mag: *ndt* monitor how a neural network's representational dimensionality evolves during training and lets you wat
> L29: |You want to see representation geometry, not just loss.|Four dimensionality metrics per layer, logged on any PyTor
> L74: Add representational-dimensionality tracking to any PyTorch model in three lines. The tracker attaches hooks, sampl

## 星数曲线

```mermaid
xychart-beta
    title "Javihaus/ndt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3bc6d603e52a` · [字段定义](../../DATASET.md)*
