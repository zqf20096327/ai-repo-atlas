# phydra-labs/phydrax

⭐ 17 · Python · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/phydra-labs/phydrax) · [官网](https://phydra-labs.github.io/phydrax) · 组织维护

**基于 JAX+Equinox 的 PDE 科学机器学习工具包，供科研人员构建物理约束模型**

面向科学机器学习（SciML）研究的 Python 工具包，基于 JAX 与 Equinox 构建，用于求解偏微分方程、约束与领域感知模型。核心机制是以单一模式组织 PDE 学习：选择域与组件、将场定义为域上函数、组合算子（梯度、Laplacian、时间导数、积分等）构建标量泛函目标，再由 FunctionalSolver 求和为可微目标并运行优化；支持通过构造 ansatz 强制满足边界/初始条件。要求 Python 3.11+，需先安装 JAX 发行版（默认 CPU 版），通过 uv add phydrax 安装，无需特殊构建或容器。源码以 Phydra Non-Production License 提供（源可得、非生产用途）。

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

- 以泛函最小化统一组织 PDE/物理学习（域→场→算子→约束→求解）
- 提供 Domain/Component/DomainFunction/Operators/Constraints/FunctionalSolver 等可组合原语
- 支持 enforced constraints：构造性满足边界/初始条件的 ansatz
- 基于 JAX+Equinox，声明与 JAX SciML 生态兼容

## 适用场景

- 用神经场求解带边界条件的偏微分方程
- 构建带物理约束或数据拟合项的可微训练目标
- 在 JAX SciML 生态中组合使用的研究工作流

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Phydrax is a scientific machine learning toolkit for PDEs, constraints, and domain-aware models, built on JAX + Equi
> L11: Phydrax organizes PDE/physics learning around a single pattern:
> L37: - **FunctionalSolver**: sums constraints and model losses into a differentiable scalar objective and runs optimizat

## 星数曲线

```mermaid
xychart-beta
    title "phydra-labs/phydrax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8955ab8045ed` · [字段定义](../../DATASET.md)*
