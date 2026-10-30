# google-deepmind/strategicwm

⭐ 16 · Python · Apache-2.0 · 推送 2026-05-19 · [GitHub](https://github.com/google-deepmind/strategicwm) · 组织维护

**用 LLM 从自然语言构建博弈树并做博弈论分析的 Python 库**

DeepMind 的 strategicwm（swm）面向研究者和开发者：用 LLM 从自然语言场景描述自动构建扩展式博弈（博弈树）表示。提供两种方式：多智能体逐节点构建（每次节点扩展约需多次 LLM 调用，较准确）与单次 LLM 调用生成完整 JSON 树（更快更省 token 但可编辑性较弱）。附带可视化工具，并支持将博弈树载入 OpenSpiel 做博弈论分析，实现 n 人一般和博弈的加速均衡求解器。默认使用 Gemini 模型，换用其他 LLM 需修改 client_lib.py 源码。以 PyPI 包与 Colab notebook 形式提供，声明非 Google 官方支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体逐节点与单次调用两种博弈树生成方式
- 支持载入 OpenSpiel 做博弈论分析
- n 人一般和博弈的加速均衡求解器
- 提供三个示例 Colab notebook

## 适用场景

- 从自然语言描述快速原型化小型博弈树
- 对构造的博弈做均衡求解与策略评估
- 作为博弈论均衡求解研究的基线

## 场景标签

 · 领域:计算博弈论/LLM 应用

## 证据(README 行号)

> L13: `swm` uses LLMs to aids users in automating the construction of formal
> L65: * **Game Construction:** `swm` is designed to quickly prototype small game
> L70: * **Research:** `swm` implements accelerated equilibrium solvers for

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/strategicwm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7e31e438728b` · [字段定义](../../DATASET.md)*
