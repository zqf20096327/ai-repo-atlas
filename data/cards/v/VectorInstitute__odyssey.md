# VectorInstitute/odyssey

⭐ 62 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/VectorInstitute/odyssey) · 组织维护

**可解释临床时间线 EHR 基础模型：事件预测与预警评测框架**

流式 EHR 基础模型及配套评测工具：以概念瓶颈架构预测患者时间线上的下一事件与时间，输出各临床事件（血管升压药启用、AKI、ICU 入住、死亡、Sepsis-3、30 天再入院等）的离散时间风险，隐状态分解为 29 个规则衍生的临床概念、未命名概念与残差。支持在 MIMIC-IV、eICU-CRD 与 GEMINI 上经 MEDS 标准流水线训练评测，并提供概念干预（steering）、消融与配对置信区间脚本。默认混合骨干依赖 CUDA 训练，推理可在 CPU/Apple silicon 运行。

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

- 概念瓶颈架构：29 个规则衍生临床概念与残差分解，支持按概念方向干预
- 下一事件预测、时间预测与逐临床事件的离散时间风险头
- MIMIC-IV/eICU-CRD/GEMINI 三数据源经 MEDS 统一流水线
- 实验注册表与 JSON 数据银行保证论文数字可溯源

## 适用场景

- 在 MIMIC-IV/eICU 数据上训练可解释的临床风险预警模型
- 检验概念瓶颈模型的读出精度、完备性与可干预性
- 与 GBM、TabICLv2、生存分析基线做配对评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L30: Odyssey is a streaming EHR foundation model with a concept bottleneck, and the evaluation harness that asks whether
> L34: 1. **Is the readout accurate?** Each concept head is scored by held-out AUROC against its rule label (mean 0.93 on 

## 星数曲线

```mermaid
xychart-beta
    title "VectorInstitute/odyssey 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-28 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `5be5f306ffbc` · [字段定义](../../DATASET.md)*
