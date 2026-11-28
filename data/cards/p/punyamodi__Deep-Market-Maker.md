# punyamodi/Deep-Market-Maker

⭐ 10 · Python · 推送 2026-02-28 · [GitHub](https://github.com/punyamodi/Deep-Market-Maker) · 个人维护

**基于订单流毒性预测的自适应做市策略系统**

量化做市研究系统：解析 LOBSTER L3 数据重建限价订单簿，校准二元 Hawkes 过程提取自激发/交叉激发强度特征，与 OFI 多尺度特征、LOB 时序快照一起经交叉注意力融合输入 MHLOBT 神经网络，输出成交毒性概率、预期收益与不确定性；据此对 Avellaneda-Stoikov 报价做毒性门控（扩大/收窄价差、调整规模）。附事件驱动撮合模拟、PnL 归因、HMM 状态识别与多重检验统计验证，面向量化研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MHLOBT 网络融合 LOB 时序、Hawkes 强度与 OFI 三路输入，输出毒性概率与不确定性
- 毒性门控的 Avellaneda-Stoikov 报价：toxicity>0.65 时价差×2.5、规模×0.5
- O(1) 在线 Hawkes 强度追踪器与 L-BFGS-B MLE 校准
- 事件驱动回测含排队位置成交模型、延迟抖动与多重检验（SPA、Deflated Sharpe）

## 适用场景

- 在 LOBSTER L3 数据上研究订单流毒性对做市报价的影响
- 训练与评估订单簿毒性预测模型
- 用带延迟与成交概率的模拟环境回测做市策略

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: Market makers profit from the bid-ask spread but lose to informed traders who know the short-term price direction b
> L61: **MHLOBT (Multi-Horizon LOB-OFI Toxicity Network)** — three input streams fused via cross-attention:

## 星数曲线

```mermaid
xychart-beta
    title "punyamodi/Deep-Market-Maker 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-02 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `8fbbb15fbfea` · [字段定义](../../DATASET.md)*
