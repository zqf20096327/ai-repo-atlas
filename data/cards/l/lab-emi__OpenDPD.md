# lab-emi/OpenDPD

⭐ 181 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/lab-emi/OpenDPD) · [官网](https://www.tudemi.com) · 组织维护

**PyTorch 功放建模与数字预失真端到端学习框架**

代尔夫特理工大学 EMI 实验室开发的 PyTorch 框架，面向射频功放（PA）行为建模与数字预失真（DPD）：生成或导入 I/Q 数据、训练 PA 行为模型、在其前级训练预失真器并导出预失真信号。提供浏览器/本地 Studio（uv 安装 GUI）、headless CLI 与 Python API 三种使用方式，共享同一训练核心。Studio 2.3 起含 DPD Arena 基准（冻结 TRes-GRU PA 上比较 EVM/ACLR/复杂度）。明确说明经 PA 模型评估的 DPD 结果是仿真，实测需物理 PA 测量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PA 建模→DPD 训练→测试导出的四步工作流
- Studio（浏览器/本地）、CLI、Python API 共用同一训练核心
- DPD Arena 基准：冻结 TRes-GRU PA 上 250-2,000 参数扫描与 Pareto 图
- 支持自建数据集、自选 PyTorch 后端（CUDA/Apple MPS/CPU 自适应）

## 适用场景

- 用实测或仿真 I/Q 数据训练功放行为模型
- 在训练好的 PA 模型前级设计并评估数字预失真器
- 导出预失真信号用于物理功放测量实验
- 复现论文结果或比较不同 DPD 模型结构

## 场景标签

 · 领域:射频/无线通信信号处理

## 证据(README 行号)

> L19: OpenDPD is a PyTorch framework for power amplifier (PA) modeling and digital predistortion (DPD), developed by the 
> L77: |2. Model the PA|Train a behavioral model, then test it on held-out data.|How closely it predicts the dataset respo

## 星数曲线

```mermaid
xychart-beta
    title "lab-emi/OpenDPD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 179 --> 182
    line [180, 181, 181]
```

2026-10-18 180 → 2026-10-23 181（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c4ff1199d0cc` · [字段定义](../../DATASET.md)*
