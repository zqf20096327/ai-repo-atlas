# web3spreads/quant-flow

⭐ 41 · Python · 推送 2026-09-18 · [GitHub](https://github.com/web3spreads/quant-flow) · [官网](https://web3spreads.github.io/quant-flow/) · 个人维护 · 中文 README

**面向 Hyperliquid DEX 的 LLM 决策加密合约自动交易机器人**

Python 编写的 Hyperliquid 永续合约自动交易系统：LLM 仅输出结构化 JSON 交易决策（BUY/SELL_SHORT/CLOSE/HOLD），下单、止盈止损与风控由确定性代码执行，LLM 故障不影响交易动作。包含永续与网格两种策略，可独立或并行运行，默认测试网环境。通过 uv 管理依赖，提供 Docker Compose 部署方式与 pytest 测试。README 声明仅供学习研究，合约交易可能损失全部本金。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 产出结构化 JSON 决策，下单与风控由确定性代码完成
- 永续与网格两种策略，可独立或并行开关运行
- 默认测试网运行（HYPERLIQUID_TESTNET=true）
- 提供 Docker Compose 部署与 pytest/ruff 测试

## 适用场景

- 在 Hyperliquid 测试网学习 LLM 辅助交易流程
- 研究 LLM 决策与确定性风控代码分离的架构
- 运行永续或网格策略的自动化交易实验

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: AI 驱动的 Hyperliquid 自动交易系统。 **LLM 只产出结构化
> L8: - **永续**：K 线收盘后 LLM 输出 BUY / SELL_SHORT / CLOSE / HOLD，校验后执行并自动挂止盈止损

## 星数曲线

```mermaid
xychart-beta
    title "web3spreads/quant-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-30 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5eba27efd2ca` · [字段定义](../../DATASET.md)*
