# nhejazi/txshift

⭐ 14 · R · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/nhejazi/txshift) · [官网](https://codex.nimahejazi.org/txshift) · 个人维护

**R 包：估计随机干预下反事实均值的因果效应**

面向统计学与流行病学研究的 R 包，用于构造随机干预（stochastic interventions）下结果反事实均值的高效估计量，实现并扩展 TML 估计量与一步估计量，并通过 IPC 权重支持两阶段抽样（如疫苗效力试验）设计下的无偏估计。集成 sl3 包以利用集成机器学习估计扰动参数。安装支持 CRAN 与 GitHub（remotes），sl3 为可选增强依赖需另行安装。方法论发表于 Biometrics 与 JOSS，由 NIH 和 NSF 资助，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现随机干预下反事实均值的 TML 与一步估计量
- 通过 IPC 权重支持两阶段抽样设计的估计校正
- 集成 sl3 支持集成机器学习估计扰动参数

## 适用场景

- 疫苗效力试验等两阶段抽样设计下的因果效应估计
- 评估依赖处理自然取值的随机干预效应
- 因果推断研究中的高效非参数估计

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L26: The `txshift` R package is designed to provide facilities for the
> L35: (Pfanzagl and Wefelmeyer 1985). `txshift` integrates with the [`sl3`

## 星数曲线

```mermaid
xychart-beta
    title "nhejazi/txshift 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-22 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `e88f74efb04e` · [字段定义](../../DATASET.md)*
