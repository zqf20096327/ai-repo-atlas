# mir-group/allegro-pol

⭐ 41 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/mir-group/allegro-pol) · [官网](https://www.nature.com/articles/s41467-025-59304-1) · 组织维护

**预测材料电极化响应的 Allegro 扩展模型（含能量与力）**

基于 NequIP 框架的扩展包，将 Allegro 架构扩展为在单一 ML 模型中同时预测材料的电极化响应（极化、Born 电荷、极化率）以及能量和力。通过 nequip-train 训练，支持 nequip-package 打包与 nequip-compile 编译为 ASE、TorchSim 和 LAMMPS pair style 集成（含仅极化与含 Born 电荷/极化率两种目标），提供 BaTiO3 示例数据与配置及前后处理脚本。方法源于论文 "Unified differentiable learning of electric response"。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一模型同时预测极化、Born 电荷、极化率与能量、力
- 可编译为 ASE / TorchSim / LAMMPS pair style 集成
- 提供 BaTiO3 训练示例数据与配置文件
- 附前后处理脚本及教程

## 适用场景

- 铁电等功能材料的电极化响应建模
- 在分子动力学模拟（ASE/LAMMPS/TorchSim）中使用含电极化的机器学习势
- 复现论文并训练自己的电响应模型

## 场景标签

 · 领域:计算材料科学/机器学习原子间势

## 证据(README 行号)

> L5: `allegro-pol` is an extension package of the `nequip` framework that adapts the Allegro architecture (another `nequi
> L118: BaTiO3 data and an associated config file are provided for training, which is all based on the `nequip` framework 

## 星数曲线

```mermaid
xychart-beta
    title "mir-group/allegro-pol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `dafe4fda000a` · [字段定义](../../DATASET.md)*
