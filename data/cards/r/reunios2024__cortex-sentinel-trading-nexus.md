# reunios2024/cortex-sentinel-trading-nexus

⭐ 123 · HTML · 推送 2026-10-29 · [GitHub](https://github.com/reunios2024/cortex-sentinel-trading-nexus) · 组织维护

**多源舆情融合引擎：六渠道信号聚合产出信念加权共识分**

SolaraX 从六个渠道（Polymarket、Kalshi、社交、链上治理投票、宏观调查、Kronos 基础模型）摄取概率信号，经 Bull/Bear/Judge 三角色辩论仲裁与 Claude Opus 级推理层交叉质证，输出 {共识概率、信念水平、认知风险标志} 三元组及可审计的辩论记录，并通过本地 REST/WebSocket（127.0.0.1:8234）广播。不含交易执行、钱包连接与私钥处理。非商业用途免许可，商业部署需付费。README 的仓库名（trading-nexus）与正文产品名（SolaraX）不一致，且未提供具体安装或运行命令，仅有 'Download' 标题。

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

- 六渠道信号摄取（预测市场/社交/链上投票/宏观调查/Kronos 模型）
- Bull/Bear/Judge 三角色辩论仲裁与辩论记录输出
- 信念元指标：Fleiss κ 共识、Brier 趋势、歧义标志
- 本地零鉴权 REST + WebSocket 输出（127.0.0.1:8234），无交易执行逻辑

## 适用场景

- 预测市场交易者在下注前获取跨源共识参考
- DAO 治理分析者评估多选民基础的提案结果
- 宏观基金将非价格舆情纳入状态识别
- 研究者研究零售预测市场与机构调查的分歧

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L9: **SolaraX** is a sovereign sentiment‑fusion framework that ingests opinion signals from six distinct voter pools—pre
> L15: Conventional sentiment aggregation relies on a single data source or a simple average of polls. SolaraX replaces th

## 星数曲线

```mermaid
xychart-beta
    title "reunios2024/cortex-sentinel-trading-nexus 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 122 --> 125
    line [124, 123, 123]
```

2026-10-18 124 → 2026-10-30 123（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 low · 依据 README sha `1fb8c823a916` · [字段定义](../../DATASET.md)*
