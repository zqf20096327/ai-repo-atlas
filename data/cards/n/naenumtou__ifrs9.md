# naenumtou/ifrs9

⭐ 133 · Jupyter Notebook · 推送 2025-11-08 · [GitHub](https://github.com/naenumtou/ifrs9) · 个人维护

**IFRS 9 减值模型实现：PD/LGD/EAD 与 ECL 计算及分阶**

提供 IFRS 9 会计准则下预期信用损失（ECL）的完整模型组件：PD（违约概率）、LGD（违约损失）、EAD（违约风险敞口）建模，三者结合分阶标准（12个月 ECL 的 Stage 1 与全生命周期 ECL 的 Stages 2/3）计算 ECL。计算流程中结合宏观经济预测等外部数据生成 12 个月与全生命周期预期损失预测，按 EIR 折现，并将阶段 1/2/3 的分配结果输出至会计系统。以 Python notebook 形式在 Google Colab 运行，面向银行拨备流程使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PD / LGD / EAD 三个模型组件
- staging criteria 分阶标准下的 ECL 计算
- 结合宏观经济预测输出 12 个月与全生命周期预期损失并按 EIR 折现

## 适用场景

- 实现银行贷款组合的 IFRS 9 预期信用损失计量
- 构建 PD/LGD/EAD 模型并按风险分段计算拨备
- 将阶段 1/2/3 分配结果对接会计系统的最终 EL 拨备

## 场景标签

 · 领域:金融风险管理

## 证据(README 行号)

> L23: * **PD** is a probability of default model to estimate potential loss that likely to occur in given time period.
> L27: The model components will be appiled together with **staging criteria**, which is allowed ECL Calculation of differ
> L33: From this data, the Bank can implement models on PD, LGD, and EAD, combining external data such as macroeconomic fo

## 星数曲线

```mermaid
xychart-beta
    title "naenumtou/ifrs9 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 131 --> 134
    line [132, 133, 133]
```

2026-10-18 132 → 2026-10-27 133（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3354bdc303c2` · [字段定义](../../DATASET.md)*
