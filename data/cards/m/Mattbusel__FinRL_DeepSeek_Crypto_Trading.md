# Mattbusel/FinRL_DeepSeek_Crypto_Trading

⭐ 18 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Mattbusel/FinRL_DeepSeek_Crypto_Trading) · 个人维护 · 中文 README

**FinRL竞赛参赛研究代码：DQN集成+DeepSeek新闻信号的BTC交易agent**

FinRL竞赛Task 1的研究代码：D3QN、DoubleDQN、TwinD3QN三个DQN agent在1秒BTC限价订单簿数据上训练，状态包含持仓、持有时长、8个RNN因子及DeepSeek V3生成的新闻情绪与风险分数（1-5，无新闻时中性3）。三agent多数投票决定买/卖/持有，由竞赛的市场回放模拟器执行（1 BTC上限、止损、滑点）。面向深度强化学习交易的学习者。README如实报告该次训练中集成从未交易（两agent收敛为始终持有）。仅单一种子、2021年九天数据，明确声明为研究代码非投资建议。演示可在笔记本CPU约15秒运行，无需API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DQN集成（D3QN/DoubleDQN/TwinD3QN）多数投票，状态含12个数字
- DeepSeek V3将BTC新闻转为情绪与风险分数纳入状态
- 演示无需下载完整数据与API key，笔记本CPU约15秒
- README如实披露集成未交易的结果与单一种子局限

## 适用场景

- 学习深度强化学习在交易中的应用与LLM信号接入
- 复现FinRL竞赛Task 1的完整流水线
- 观察新闻情绪信号如何影响交易决策

## 场景标签

`金融量化` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L17: LARSA is a crypto trading bot research project for Task 1 of the FinRL contest: a DQN ensemble (D3QN, DoubleDQN, Tw
> L5: **A crypto trading agent that changes strategy when the news changes: DeepSeek V3 turns BTC headlines into sentiment

## 星数曲线

```mermaid
xychart-beta
    title "Mattbusel/FinRL_DeepSeek_Crypto_Trading 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `5e16747057bb` · [字段定义](../../DATASET.md)*
