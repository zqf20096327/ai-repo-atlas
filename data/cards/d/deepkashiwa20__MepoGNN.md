# deepkashiwa20/MepoGNN

⭐ 33 · Python · MIT · 推送 2026-02-24 · [GitHub](https://github.com/deepkashiwa20/MepoGNN) · 个人维护

**图神经网络混合 SIR 模型预测日本 47 都道府县疫情**

ECMLPKDD22 论文 MepoGNN 的官方代码：将时空图神经网络与图学习机制融入 Metapopulation SIR 模型，进行多步、多区域的每日确诊感染人数预测。使用历史每日感染数据与人类移动数据（OD 流量、通勤调查）对日本 47 都道府县做疫情预测。提供数据文件说明与基于 Python/PyTorch 的训练验证测试脚本，运行需指定 GPU 与图学习类型（Adaptive 或 Dynamic）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GNN 与 Metapopulation SIR 模型结合的多区域多步感染预测
- 支持 Adaptive 与 Dynamic 两种图学习类型
- 提供日本 47 都道府县的感染与移动数据（npy 格式）

## 适用场景

- 复现论文中的日本都道府县级疫情预测实验
- 研究时空图神经网络在流行病建模中的应用
- 基于感染与人口流动数据训练预测模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: #### [ECMLPKDD22] Q. Cao, R. Jiang#, C. Yang, Z. Fan, X. Song, R. Shibasaki, "MepoGNN: Metapopulation Epidemic Forec
> L16: We propose a novel hybrid model called MepoGNN for multi-step (day) multi-region (prefecture) infection number pred

## 星数曲线

```mermaid
xychart-beta
    title "deepkashiwa20/MepoGNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a49c59d514a8` · [字段定义](../../DATASET.md)*
