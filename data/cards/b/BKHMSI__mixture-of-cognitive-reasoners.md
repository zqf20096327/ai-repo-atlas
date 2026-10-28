# BKHMSI/mixture-of-cognitive-reasoners

⭐ 47 · Python · 推送 2026-02-07 · [GitHub](https://github.com/BKHMSI/mixture-of-cognitive-reasoners) · [官网](https://cognitive-reasoners.epfl.ch) · 组织维护

**脑功能特化专家模块的模块化推理模型（论文代码）**

EPFL 团队论文 MiCRo 的官方代码库：将预训练语言模型的层划分为对应人脑认知网络（language/logic/social/world）的四个专家模块，经课程式后训练诱导功能特化。支持三阶段训练脚本与文本生成脚本，生成时可按 CSV 指定消融特定专家，从而在推理时调控模型行为。提供配置文件目录与数据处理工具，属研究复现型项目。

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

- 将预训练模型层划分为 4 个对应脑认知网络的专家模块
- 三阶段课程式后训练流程（main.py + 配置文件）
- 生成时可消融指定专家（language/logic/social/world）
- 在 GSM8K、BBH、CogBench 等基准上评估（论文声明）

## 适用场景

- 复现论文中的模块化认知推理训练与消融实验
- 研究专家模块的可解释性与因果作用
- 推理时通过专家路由控制输出风格

## 场景标签

 · 领域:机器学习研究/神经科学启发 AI

## 证据(README 行号)

> L12: > Human cognitive behavior arises from the interaction of specialized brain networks dedicated to distinct function
> L20: python main.py -c config_micro_llama.yml

## 星数曲线

```mermaid
xychart-beta
    title "BKHMSI/mixture-of-cognitive-reasoners 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-28 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7bdd0b536a66` · [字段定义](../../DATASET.md)*
