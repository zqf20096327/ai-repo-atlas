# GustikS/NeuraLogic

⭐ 122 · Java · MIT · 推送 2026-10-01 · [GitHub](https://github.com/GustikS/NeuraLogic) · 组织维护

**通过可微逻辑编程整合深度与关系学习的 Java 框架**

Lifted Relational Neural Networks 概念的官方 Java 后端实现：用类 Datalog 的声明式语言定义输入事实、输出查询与带可学习参数的规则，模板经逻辑 grounding 自动生成参数化计算图并通过梯度下降优化，可直接编码图神经网络、知识库补全、神经符号整合等关系学习场景。以多模块 Maven 项目提供，含 CLI 与独立子模块（Algebra/Logic/Neural 等），Python 前端在 PyNeuralogic 仓库。声明面向学术用途、开发进展缓慢，不适合常规大规模张量深度学习。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 声明式（类 Datalog）语言编写可微学习程序，规则参数 W 经梯度下降自动优化
- 模板自动生成参数化计算图，可直接编码 GNN、知识库补全、神经符号整合等场景
- 多模块 Maven 架构，Algebra/Logic/Neural/Pipelines 等子模块可独立使用
- CLI 可运行 XOR、mutagenesis 分子分类、nations 知识库补全等内置示例数据集

## 适用场景

- 用关系/图结构数据做分类或回归原型实验
- 在 GNN 基础上编码更复杂的关系学习模型或逻辑先验
- 神经符号研究：将（模糊）逻辑推理与神经网络结合

## 场景标签

 · 领域:机器学习/神经符号计算

## 证据(README 行号)

> L9: _Integrating **deep** and **relational** learning through **differentiable logic programming**._
> L17: At the core of the framework, there is a custom language you can use to write differentiable programs encoding your
> L41: These 2 rules, parameterized with the tensors `W_*`'s, then form a _learning program_, which can be used to classif

## 星数曲线

```mermaid
xychart-beta
    title "GustikS/NeuraLogic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 121 --> 123
    line [122, 122]
```

2026-10-18 122 → 2026-10-25 122（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a76bd0fcff68` · [字段定义](../../DATASET.md)*
