# stfc/aiida-mlip

⭐ 26 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/stfc/aiida-mlip) · [官网](https://stfc.github.io/aiida-mlip/) · 组织维护

**AiiDA 插件：在工作流中运行机器学习原子间势计算与训练**

stfc 维护的 AiiDA 插件，将机器学习原子间势（MLIP）计算接入 AiiDA 工作流管理：支持 MACE、M3GNET、CHGNET 三种势模型，覆盖单点计算、几何优化、分子动力学（NVE/NVT/NPT 多种控温控压方案）、训练与微调（MACE）及描述符计算。计算由 janus-core 基于 ASE 执行，通过 verdi 命令与 CalcJob 提交，需配置 AiiDA profile，推荐安装 RabbitMQ 作为消息代理以启用完整功能。功能清单标注为开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 MACE/M3GNET/CHGNET 三种机器学习原子间势
- 单点计算、几何优化与 NVE/NVT/NPT 分子动力学
- MACE 模型的训练、微调与描述符计算
- 通过 AiiDA CalcJob 与 verdi 命令提交计算

## 适用场景

- 在 AiiDA 工作流中提交 MLIP 单点计算与几何优化
- 用 MACE 训练或微调原子间势模型并纳入数据管理
- 对材料结构运行多种系综的分子动力学模拟

## 场景标签

`工作流自动化` `微调` · 领域:效率与自动化

## 证据(README 行号)

> L12: machine learning interatomic potentials aiida plugin
> L33: The code relies heavily on janus-core, which handles mlip calculations using ASE.
> L16: - [x] Supports multiple MLIPs

## 星数曲线

```mermaid
xychart-beta
    title "stfc/aiida-mlip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c985335a7363` · [字段定义](../../DATASET.md)*
