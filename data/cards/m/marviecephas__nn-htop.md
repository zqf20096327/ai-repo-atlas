# marviecephas/nn-htop

⭐ 7 · Python · 推送 2026-10-13 · [GitHub](https://github.com/marviecephas/nn-htop) · 个人维护

**PyTorch 训练的终端监控器：查看层激活与梯度范数**

基于 PyTorch hook 的终端 TUI 监控工具：通过 register_forward_hook 跟踪各层激活均值、register_full_backward_hook 计算梯度 L2 范数，监控时自动覆盖 inplace=True 以避免 autograd 图冲突；张量在 hook 回调内立即 detach 并降为标量以防止计算图保留；训练线程只写原子状态字典，UI 以 5 FPS 轮询以不影响训练吞吐。提供内置演示（3 层 MLP 训练），并支持以上下文管理器方式挂载到任意 torch.nn.Module，也可集成到自定义训练循环。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PyTorch 前向/反向 hook 采集层激活均值与梯度 L2 范数
- Textual 非阻塞 TUI，5 FPS 轮询原子状态字典
- hook 内即时 detach 张量并降为标量，防止计算图保留
- 支持挂载任意 torch.nn.Module 与手动集成训练循环

## 适用场景

- 训练 PyTorch 模型时在终端实时观察各层激活与梯度
- 排查梯度消失/爆炸等训练问题
- 在不干扰训练吞吐的前提下监控自定义训练循环

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: A terminal-based monitor for PyTorch neural network layer activations and gradient norms (htop for PyTorch neural ne
> L23: Attach `Monitor` to any `torch.nn.Module` using context-managed hook lifecycle and launch the non-blocking Textual 
> L45: - **Hook Instrumentation**: Attaches `register_forward_hook` (mean activation tracking) and `register_full_backward

## 星数曲线

```mermaid
xychart-beta
    title "marviecephas/nn-htop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-11-20"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-10-18 6 → 2026-11-20 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `c3f43b5e70d8` · [字段定义](../../DATASET.md)*
