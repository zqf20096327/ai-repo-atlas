# AbductiveLearning/ABLkit

⭐ 102 · Python · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/AbductiveLearning/ABLkit) · [官网](https://ablkit.readthedocs.io/) · 组织维护

**反绎学习（ABL）Python 工具包：统一框架下结合机器学习与逻辑推理**

面向数据与逻辑领域知识同时可用的任务，ABLkit 提供反绎学习（Abductive Learning）范式的高效实现：学习侧支持 scikit-learn 风格模型与 PyTorch 网络（经 BasicNN/ABLModel 包装到示例级），推理侧通过 KBBase 子类定义知识库与 Reasoner 做演绎/反绎推理并最小化不一致性，SimpleBridge 将两侧组合为统一训练框架。提供 SymbolAccuracy、ReasoningMetric 评估指标与 MNIST 加法等 5 个示例；可选安装 SWI-Prolog 支持 Prolog 知识库。附相关论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 学习侧兼容 scikit-learn 风格模型与 PyTorch 网络
- KBBase/Reasoner 构建知识库并最小化反绎推理的不一致性
- SimpleBridge 统一组合学习与推理的训练框架
- 附 MNIST Addition、HWF、BDD-OIA 等 5 个示例与配套论文

## 适用场景

- 在数据与逻辑领域知识并存的场景下构建神经-符号学习系统
- 做手写公式识别或可解释推理相关研究实验
- 快速复现反绎学习论文中的基准任务

## 场景标签

`模型训练` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: **ABLkit** is an efficient Python toolkit for **Abductive Learning (ABL)**. ABL is a novel paradigm that integrates 
> L17: ABLkit encapsulates advanced ABL techniques, providing users with an efficient and convenient toolkit to develop du

## 星数曲线

```mermaid
xychart-beta
    title "AbductiveLearning/ABLkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 100 --> 103
    line [101, 102, 102]
```

2026-10-18 101 → 2026-10-31 102（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fc0f895d18e2` · [字段定义](../../DATASET.md)*
