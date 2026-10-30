# Clarity-Digital-Twin/brain-go-brr-v2

⭐ 22 · Python · Apache-2.0 · 推送 2025-12-29 · [GitHub](https://github.com/Clarity-Digital-Twin/brain-go-brr-v2) · 组织维护

**面向临床 EEG 癫痫检测的双栈状态空间深度学习研究项目**

研究型癫痫检测系统：在相同流水线（TCN 前端 + GNN 后端 + 动态 Laplacian 位置编码 + 门控融合）上对照实验两种 O(N) 状态空间时序核心——BiMamba2 与 Gated DeltaNet（FLA）。输入 19 通道 256Hz 的 60 秒 EEG 窗口，输出癫痫检测结果。在 TUH TUSZ 数据集（504 小时、592 名患者）上训练评估，当前 v4.4.0 的 FLA 实验 4 完成：10 FA/24h 下灵敏度 35.9%、AUROC 0.8654；BiMamba2 训练暂停于第 6 epoch。README 阐明架构原理与临床目标（≤4 FA/24h @ ≥50% 灵敏度），但未展示安装或运行命令，面向科研复现与实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BiMamba2 与 Gated DeltaNet 双栈参数量对齐（各 30.5M）的受控对照实验
- TCN + 双流 SSM（节点/边）+ 动态 Laplacian PE + GNN + 门控融合流水线
- TUSZ 数据集评测：35.9% 灵敏度 @ 10 FA/24h，AUROC 0.8654（FLA Exp4）
- memory-mapped NPY 缓存：启动快 99.6%，内存 <1GB（对比 NPZ 387GB）

## 适用场景

- 在 TUSZ 临床 EEG 数据上复现或扩展癫痫检测实验
- 对比 BiMamba2 与 Gated DeltaNet 在时序医学信号上的表现
- 研究降低 ICU 连续 EEG 监测误报率的检测架构

## 场景标签

 · 领域:医疗健康/医学信号处理

## 证据(README 行号)

> L43: - **Status**: ✅ **Exp4 COMPLETE** - **35.9% sensitivity @ 10 FA/24h** on TUSZ eval (AUROC 0.8654)
> L200: **World's largest open-source seizure dataset** (Temple University):

## 星数曲线

```mermaid
xychart-beta
    title "Clarity-Digital-Twin/brain-go-brr-v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `126471b9a005` · [字段定义](../../DATASET.md)*
