# juangamella/causal-chamber-paper

⭐ 20 · Jupyter Notebook · MIT · 推送 2026-11-09 · [GitHub](https://github.com/juangamella/causal-chamber-paper) · [官网](https://causalchamber.ai) · 组织维护

**复现 2024 年因果箱体论文案例研究的代码仓库**

收录 Juan L. Gamella、Jonas Peters 与 Peter Bühlmann 2024 年论文《The Causal Chambers》全部案例研究的复现代码，以带文档的 Jupyter notebook 组织，覆盖 i.i.d. 与时序因果发现、OOD 泛化（传感器/图像/脉冲响应）、变点检测、独立成分分析、符号回归与机理模型运行，通过 causalchamber 包加载对应数据集；数据集、机理模型与箱体搭建资源在 causalchamber.org。使用 Python 虚拟环境加 requirements.txt 安装依赖（python=3.8.10，兼容更新版本），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个 notebook 覆盖论文全部案例研究（因果发现/OOD/变点/ICA/符号回归等）
- 依赖 causalchamber 包加载论文对应数据集
- 附 UT-IGSP 封装与符号回归算法支撑代码

## 适用场景

- 逐个复现论文中的因果发现与 OOD 案例研究
- 在因果箱体数据上对比自己的方法
- 查看附录图表与校准参考电压的生成代码

## 场景标签

 · 领域:因果推断/机器学习研究

## 证据(README 行号)

> L1: # The Causal Chambers: Experiment Repository
> L3: This repository contains the code to reproduce the case studies of the 2024 paper *The Causal Chambers: Real Physica

## 星数曲线

```mermaid
xychart-beta
    title "juangamella/causal-chamber-paper 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-18"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-11-10 20 → 2026-11-18 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `9aa9e0a953a4` · [字段定义](../../DATASET.md)*
