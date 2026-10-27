# chenxingqiang/dfig-wind-power

⭐ 25 · MATLAB · MIT · 推送 2025-12-22 · [GitHub](https://github.com/chenxingqiang/dfig-wind-power) · 个人维护 · 中文 README

**含储能的 DFIG 风电系统 MATLAB/Simulink 仿真与控制实现**

面向并网双馈感应发电机（DFIG）风电系统研究的 MATLAB/Simulink 实现，集成 0.5MW/1.0MWh 储能系统，提供故障穿越控制、一次调频（虚拟惯量）、并网/构网/紧急模式切换等控制策略。AI 部分为可选项：基于 LSTM 的功率需求预测与深度强化学习的 SOC 分配优化，依赖 Deep Learning Toolbox。附带 GUI 套件（主控中心、参数配置、实时监控仪表盘、性能分析器），支持 IEEE 1547、IEC 61400-27、GB/T 19963 并网标准合规校验。运行需 MATLAB R2021b+ 与 Simulink。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 故障穿越（FRT）与一次调频控制，含虚拟惯量与储能协调
- LSTM 功率预测与 DRL 的 SOC 分配优化（在线学习）
- 并网/构网/紧急模式动态切换
- GUI 套件：主控中心、参数配置、实时监控、性能分析与报告导出

## 适用场景

- 搭建含储能的 DFIG 风电并网仿真模型
- 测试故障穿越与频率支撑等控制策略
- 按并网标准（IEEE 1547/GB/T 19963）做合规性分析
- 验证 LSTM/DRL 在风电控制中的优化效果

## 场景标签

 · 领域:电力系统/可再生能源

## 证据(README 行号)

> L8: A comprehensive MATLAB/Simulink implementation of a Doubly-Fed Induction Generator (DFIG) wind power system with int
> L40: #### **Deep Learning Integration**
> L43: - **Online Learning**: Adaptive model updates during operation

## 星数曲线

```mermaid
xychart-beta
    title "chenxingqiang/dfig-wind-power 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3f4853631ff0` · [字段定义](../../DATASET.md)*
