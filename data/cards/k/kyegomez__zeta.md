# kyegomez/zeta

⭐ 604 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/zeta) · [官网](https://zeta.apac.ai) · 个人维护

**PyTorch 模块化组件库，供开发者快速组装 AI 模型**

基于 PyTorch 的模块化 AI 模型构建库，提供注意力机制（Multi-Query、Sigmoid、Flash 等）、MoE 专家路由、前馈网络、BitLinear 与动态量化、融合算子（FusedDenseGELUDense、FusedDropoutLayerNorm）、Mamba 状态空间模块等可复用组件，并含 PalmE 多模态架构、U-Net 等完整模型实现，以及 DPO 强化学习训练、模型执行日志装饰器和 hyper_optimize 优化接口。通过 pip 安装 zetascale 包使用，文档见 zeta.apac.ai 与 readthedocs。

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

- 注意力/MoE/量化/融合算子等模块化 PyTorch 组件库
- 含 PalmE 多模态架构、U-Net、Mamba 等完整实现
- 提供 DPO（RLHF）训练与模型日志/优化工具
- pip install zetascale 安装，附测试套件与示例目录

## 适用场景

- 用现成积木式组件搭建 Transformer 或多模态模型
- 为现有 PyTorch 模型替换量化层与融合算子
- 在 RLHF 流程中使用 DPO 实现

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: **Zeta** is a modular PyTorch framework designed to simplify the development of AI models by providing reusable, hi
> L30: Zeta provides a comprehensive library of modular components commonly used in modern AI architectures, including:

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/zeta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 603 --> 605
    line [604, 604]
```

2026-10-18 604 → 2026-10-30 604（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `142a950d0bbf` · [字段定义](../../DATASET.md)*
