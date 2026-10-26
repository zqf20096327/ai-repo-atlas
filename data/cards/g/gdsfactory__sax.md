# gdsfactory/sax

⭐ 131 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/gdsfactory/sax) · [官网](https://gdsfactory.github.io/sax/) · 组织维护

**基于 JAX 的 S 参数频域光子集成电路仿真与优化库**

SAX 是构建在 JAX 之上的散射参数（S-parameter）电路仿真器与优化器，面向频域仿真，最初为光子集成电路（PIC）开发，也可用于任意基于 S 参数的电路仿真。定位为 JAX 的薄封装：不引入特殊数据结构，模型即返回 S 字典的普通 Python 函数，组件模型经 netlist 组合成电路后仍是函数，可随参数调用仿真。默认使用 KLU 电路后端（klujax 为必装依赖，无缺失回退）。需 Python>=3.11，pip 安装；开发环境用 uv 与 Python 3.12。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型即函数 + 标准 Python 字典，保持 JAX 函数式风格
- 通过 netlist 将组件模型组合为电路模型，支持全局参数分发
- 默认 KLU 后端（klujax 自动安装为必需依赖）
- 面向光子集成电路的频域 S 参数仿真与优化

## 适用场景

- 仿真由方向耦合器、波导等组件构成的光子集成电路
- 对电路参数做基于自动微分的优化
- 在 JAX 工作流中做可微分的 S 参数频域仿真

## 场景标签

 · 领域:光子学/物理仿真

## 证据(README 行号)

> L7: SAX: S-Matrices with Autograd and XLA - a scatter parameter circuit simulator and
> L10: The simulator was developed for simulating Photonic Integrated Circuits but in fact is
> L12: thin wrapper around JAX with some basic tools for S-parameter based circuit simulation

## 星数曲线

```mermaid
xychart-beta
    title "gdsfactory/sax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 130 --> 132
    line [131, 131]
```

2026-10-18 131 → 2026-10-26 131（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b19c975fe33d` · [字段定义](../../DATASET.md)*
