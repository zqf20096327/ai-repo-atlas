# systems-mechanobiology/DeTime

⭐ 54 · Jupyter Notebook · BSD-3-Clause · 推送 2026-10-29 · [GitHub](https://github.com/systems-mechanobiology/DeTime) · [官网](https://systems-mechanobiology.github.io/DeTime/) · 组织维护

**面向科研的统一时序分解 Python/CLI 工具库**

DeTime 是一个开源 Python 时序分解工具包，以单一 decompose() 入口与统一 DecompositionConfig/DecompResult 契约，封装 SSA、STD、STDR、MSSA 等核心方法及 STL、EMD、小波等可选后端，配套 detime CLI（run/batch/profile/recommend/benchmark 等命令）、JSON schema 与机器可读元数据。部分方法提供 C++ 原生加速，支持多元分解工作流。面向需要跨方法族统一工作流的研究与工程用户；状态为 Beta（0.1.3），实验性神经分解块默认不推荐使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 decompose() 入口与统一的 DecompositionConfig/DecompResult 契约
- SSA/STD/STDR/MSSA 四个核心维护方法，另有 C++ 原生加速路径
- detime CLI 提供 run/batch/profile/schema/recommend/benchmark 七个命令
- JSON schema 与低 token 结果导出模式（full/summary/meta）支持自动化

## 适用场景

- 用统一接口在多个时序分解方法间切换与对比
- 通过 CLI 批量处理时序数据并生成带 schema 的机器可读结果
- 复现时序分解工作流并保存可追溯的运行元数据

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: DeTime is an open-source Python time-series decomposition toolkit with a CLI for
> L64: - `SSA`
> L80: Experimental neural decomposition blocks extracted as standalone DeTime

## 星数曲线

```mermaid
xychart-beta
    title "systems-mechanobiology/DeTime 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-31 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `db3da3736def` · [字段定义](../../DATASET.md)*
