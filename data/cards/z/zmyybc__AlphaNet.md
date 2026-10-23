# zmyybc/AlphaNet

⭐ 122 · Python · GPL-3.0 · 推送 2026-07-26 · [GitHub](https://github.com/zmyybc/AlphaNet) · 个人维护

**局域标架等变机器学习原子间势，用于原子体系模拟**

面向计算材料与催化模拟研究者的神经网络原子间势模型：通过构建等变局域标架与可学习标架变换利用原子环境几何结构，以矩阵_product_state_缩并实现多体消息传递，预测能量、力与应力。基于 PyTorch Lightning 提供训练、checkpoint 转换与评估三套命令行工具，另有 JAX 实现与 ASE calculator，支持 torch→JAX checkpoint 转换、ZBL 势叠加及 LAMMPS 集成分支（triton 加速版）。提供 MPtrj/OMAT24/MATPES/AQCAT25 等预训练模型。限制：训练需开启梯度裁剪并将 weight decay 设为 0，LAMMPS 分支持续合并中，损失权重需按数据能量涨落手动调整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 等变局域标架与可学习标架变换的多体消息传递模型
- 训练/转换/评估三套命令行工具，基于 PyTorch Lightning
- JAX 实现与 ASE calculator，torch→JAX checkpoint 转换，作者实测 2.5-3 倍加速
- 提供材料与催化领域的多个预训练模型及 LAMMPS 分支

## 适用场景

- 为分子动力学模拟训练机器学习力场
- 直接使用预训练通用势预测材料或催化体系的能量、力与应力
- 通过 ASE calculator 接入现有原子模拟工作流

## 场景标签

 · 领域:计算化学/材料模拟

## 证据(README 行号)

> L5: We present **AlphaNet**, a local frame-based equivariant model designed to tackle the challenges of achieving both a
> L192:  The output (energy forces stress) difference from torch model would below 0.001. I ran speed tests on a 4090 GPU,

## 星数曲线

```mermaid
xychart-beta
    title "zmyybc/AlphaNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 121 --> 123
    line [122, 122]
```

2026-10-18 122 → 2026-10-23 122（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `22dad08416fa` · [字段定义](../../DATASET.md)*
