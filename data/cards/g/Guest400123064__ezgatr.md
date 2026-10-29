# Guest400123064/ezgatr

⭐ 24 · Python · MIT · 推送 2026-08-19 · [GitHub](https://github.com/Guest400123064/ezgatr) · [官网](https://guest400123064.github.io/ezgatr/) · 个人维护

**构建 3D 几何代数 Transformer 的轻量 PyTorch 库**

基于 PyTorch 的 Python 库，提供构建 3D 几何代数 Transformer（GATr）的算子、模块与工具集：ezgatr.nn 包含核心层与函数式算子，ezgatr.interfaces 提供 3D 对象与多向量间的编解码，ezgatr.nets 提供现成网络。面向需要等变网络（如点云）的研究与开发场景，附带文档解释数学公式与实现的对应关系。需 Python 3.10+ 与 PyTorch 2.4.1+，项目基于 GATr（NeurIPS 2023）的工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ezgatr.nn 提供几何注意力和几何 MLP 等核心模块
- ezgatr.interfaces 支持 3D 对象与多向量的编码/解码
- ezgatr.nets 提供现成网络作参考
- 配套文档解释数学表述与实现的对应

## 适用场景

- 用等变几何注意力构建 3D 点云等网络
- 学习几何代数 Transformer 的数学与实现对应
- 复用现成 GATr 网络或搭建自定义网络

## 场景标签

 · 领域:几何深度学习

## 证据(README 行号)

> L17: ## What is EzGATr?
> L18: **EzGATr** (Easy Geometric Algebra Transformer) intends to be a simple-to-use and lightweight Python library for bu

## 星数曲线

```mermaid
xychart-beta
    title "Guest400123064/ezgatr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `06633ff9977a` · [字段定义](../../DATASET.md)*
