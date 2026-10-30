# Lyahn-Huang/FullStackAutoQuant

⭐ 20 · Python · NOASSERTION · 推送 2026-08-06 · [GitHub](https://github.com/Lyahn-Huang/FullStackAutoQuant) · 个人维护 · 中文 README

**端到端深度学习 A 股量化交易系统：数据到实盘全流程**

覆盖数据获取、因子合成、模型推理、风险管理、回测与实盘下单的自动化量化交易系统。核心模型为 TCN+局部注意力+GRU 混合架构（约 18 万参数），用于横截面股票排序，采用 MC Dropout 产出置信度并过滤低置信信号。数据通过 Tushare（轻量）或 Docker/Dolt（全历史）获取，实盘经 JoinQuant/GM Trade API 执行，提供 Streamlit 面板。需 Tushare Pro 账号（2000+ 积分）与预训练权重；许可为 CC BY-NC-SA 4.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TCN+局部注意力+GRU 模型用于横截面股票排序（约 18 万参数）
- MC Dropout 16 次前向产出每只股票置信度，低置信信号过滤
- 全流程模块：数据/因子（Alpha158+2 自有因子）/风控/回测/实盘/WebUI
- CSI300 回测：含成本年化超额 16.72%，信息比率 1.96

## 适用场景

- 我要跑一个从数据到下单的自动化 A 股量化流水线
- 用深度学习模型做股票横截面排序与组合再平衡
- 用回测与绩效指标验证排序信号质量

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L24: |**Deep Learning Model**|Proprietary TCN Attention GRU architecture with strict temporal causality for cross sectio
> L37: A hybrid deep learning architecture (~180K parameters) designed for **cross sectional stock ranking**. The pipeline

## 星数曲线

```mermaid
xychart-beta
    title "Lyahn-Huang/FullStackAutoQuant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8882c46a2758` · [字段定义](../../DATASET.md)*
