# asimonder/geometricVoFCartesian

⭐ 22 · C++ · GPL-3.0 · 推送 2026-08-05 · [GitHub](https://github.com/asimonder/geometricVoFCartesian) · 个人维护

**OpenFOAM 两相流界面法向与曲率估计扩展库，含 MLP 模型**

面向 OpenFOAM 两相流仿真的几何 Volume-of-Fluid 扩展库，在均匀笛卡尔网格上估计流体-流体界面的法向向量与曲率。提供传统方法（Youngs、Central-Columns、Height Function 等）与基于 MLP 的机器学习曲率模型（目前仅 2D）；MLP 类仅用 C++ 标准库实现，无额外依赖，读取 TensorFlow 训练后转换的权重文本文件。模型经 TensorFlow 脚本训练与 OpenFOAM 基准测试筛选，需 OpenFOAM v2006 及以上，从源码编译安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 传统方法（Youngs/Central-Columns/Height Function）与 MLP 曲率模型并存
- multilayerPerceptron 类纯 C++ 标准库实现，无需额外软件包
- 提供 TensorFlow 训练脚本与权重格式转换流程
- 附 benchmark 基准算例目录

## 适用场景

- 两相流仿真中在笛卡尔网格区带估计界面曲率
- 用自训 MLP 模型替代 Height Function 曲率计算（2D）
- 复现 Önder & Liu (2023) 的曲率模型基准测试

## 场景标签

 · 领域:计算流体力学/科学计算

## 证据(README 行号)

> L2: *geometricVoFCartesian* is an extension library for two-phase flow simulations in OpenFOAM. It features conventional
> L13: - ```multilayerPerceptron```: Basic functionalities and data structures for an MLP. Implementation is done using ex
> L39: ## Prerequisites

## 星数曲线

```mermaid
xychart-beta
    title "asimonder/geometricVoFCartesian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d55f443e546a` · [字段定义](../../DATASET.md)*
