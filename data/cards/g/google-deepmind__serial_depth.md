# google-deepmind/serial_depth

⭐ 19 · Python · Apache-2.0 · 推送 2026-03-10 · [GitHub](https://github.com/google-deepmind/serial_depth) · 组织维护

**分析 JAX 计算图自动计算神经网络串行深度的工具**

面向 JAX 用户的串行深度（serial depth）计算器：解析神经网络的 jaxpr 计算图，按规则为每类原语赋深度（数据移动 0、逐元素 1、可并行归约 log N、scan 线性累加、cond 取分支最大值），递归处理 jit/pjit 嵌套，取输出变量最大深度作为程序深度。提供 gemma、MLP 等示例脚本，用 uv run 运行。适用于需要量化计算依赖链长度的深度学习研究/分析场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 jaxpr 计算图自动计算串行深度
- 按原语类别赋深度：0/1/log N/线性等规则
- 递归处理 jit/pjit 嵌套与 cond 控制流
- 自带 MLP 与 Gemma3 示例脚本

## 适用场景

- 我需要量化某个 JAX 模型计算的串行依赖深度
- 分析模型结构中不可并行化的计算链长度
- 验证手算的深度值与自动计算结果一致

## 场景标签

 · 领域:深度学习/计算图分析

## 证据(README 行号)

> L3: Automated computation of serial depth for JAX neural networks by analyzing their
> L4: jaxpr (JAX expression) computational graphs.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/serial_depth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2c054812fa9a` · [字段定义](../../DATASET.md)*
