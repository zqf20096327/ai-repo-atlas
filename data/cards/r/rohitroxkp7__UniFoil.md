# rohitroxkp7/UniFoil

⭐ 15 · Python · CC-BY-SA-4.0 · 推送 2026-04-07 · [GitHub](https://github.com/rohitroxkp7/UniFoil) · [官网](https://doi.org/10.7910/DVN/VQGWC4) · 组织维护

**50 万条翼型流场仿真数据集及存取接口**

面向计算流体力学与机器学习研究的公开数据集：覆盖 2D 翼型在不可压到可压、转捩与全湍流流域的 50 万次仿真，其中 40 万为全湍流仿真、10 万为自然层流翼型仿真。数据托管于 Harvard Dataverse，仓库提供 Python 接口用于数据可视化与提取，安装方式为克隆后 pip install .，文档托管在 Read the Docs，采用 CC BY-SA 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 500,000 次翼型仿真，覆盖转捩与全湍流、不可压到可压流域
- 400,000 全湍流 + 50,000 NLF 全湍流 + 50,000 NLF 转捩仿真
- 提供 Python 接口做数据可视化与提取
- 数据托管于 Harvard Dataverse（DOI:10.7910/DVN/VQGWC4）

## 适用场景

- 训练或评测翼型气动性能预测的机器学习模型
- 获取跨流域（亚音速/跨音速、转捩/湍流）的 CFD 仿真数据
- 做翼型设计与流场可视化研究

## 场景标签

 · 领域:计算流体力学/科学数据集

## 证据(README 行号)

> L1: **UniFoil** is a Universal Dataset of Airfoils in Transitional and Turbulent Regimes for Subsonic and Transonic Flow
> L2: It consists of 500,000 simulations covering transitional and fully turbulent flows across incompressible to compress

## 星数曲线

```mermaid
xychart-beta
    title "rohitroxkp7/UniFoil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e8ae54261d09` · [字段定义](../../DATASET.md)*
