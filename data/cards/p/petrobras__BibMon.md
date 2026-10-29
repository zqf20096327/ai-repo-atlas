# petrobras/BibMon

⭐ 107 · Python · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/petrobras/BibMon) · [官网](https://bibmon.readthedocs.io/) · 组织维护

**工业过程监控 Python 库：故障检测、软测量与状态监测**

源自 COPPE/UFRJ 与 Petrobras 研究中心合作项目的开源 Python 包，基于偏差的预测模型做过程故障检测、软测量（虚拟传感器）与过程状态监测。使用分训练与预测两步：训练阶段建模变量间正常工况关系，预测阶段比较过程数据与模型预测，基于平方预测误差（SPE）控制图触发报警。提供 PCA、ESN、SBM、自编码器等模型，兼容 scikit-learn 接口的回归器均可接入；支持在线分析、可编程报警逻辑、自动超参数调优，并附带真实与仿真数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两步使用：训练建模正常工况，预测阶段按 SPE 控制图触发报警
- 内置 PCA/ESN/SBM/自编码器，兼容 scikit-learn 接口回归器
- 支持在线分析（单样本与数据窗口）与可编程报警逻辑
- 提供自动超参数调优、控制图表绘制与真实/仿真数据集

## 适用场景

- 化工厂等工业过程的在线故障检测与报警
- 构建软测量（虚拟传感器）估计难以直接测量的变量
- 对比多种监控模型在过程数据上的表现

## 场景标签

 · 领域:工业过程系统工程/化工

## 证据(README 行号)

> L7: `BibMon` (from the Portuguese ***Bib**lioteca de **Mon**itoramento de Processos*, or Process Monitoring Library) is 
> L33: 1. In the training step, a model is generated that captures the relationships between variables in the normal proce

## 星数曲线

```mermaid
xychart-beta
    title "petrobras/BibMon 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 105 --> 108
    line [106, 107, 107]
```

2026-10-18 106 → 2026-10-29 107（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d801b0294d38` · [字段定义](../../DATASET.md)*
