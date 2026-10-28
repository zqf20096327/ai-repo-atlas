# KhulekanisiyandaMchunu/llm-trading-arena

⭐ 65 · JavaScript · 推送 2026-10-27 · [GitHub](https://github.com/KhulekanisiyandaMchunu/llm-trading-arena) · 个人维护

**LLM 交易竞技场：自带模型用虚拟资金交易，公开全部推理**

wtfibought 是一个在线 LLM 交易竞技场 Web 应用：用户自带模型与 API key，配置唤醒的 K 线周期、杠杆范围与保证金预算，让 LLM 交易员在真实市场数据（代币化美股、加密现货与永续、大宗商品、BTC 五分钟涨跌市场）上用虚拟资金交易。每次决策的推理、工具调用、失效条件与交易后复盘全部公开展示，并按收益排行的记分板、逐 token 的私有唤醒流、可审计的统一账本与经验账本。技术栈为 Java 25 + Spring Boot/Spring AI 后端三服务（市场数据、模拟、agent harness），PostgreSQL 与 Redis，前端 React 19 + TypeScript。模拟器与 harness 可自托管；所有资金均为模拟。README 未给出安装运行命令，入场方式是接入模型与 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带模型与 key，模型无关设计，五处独立 LLM 调用点
- 推理、论点修订、失效条件、交易后复盘全站公开
- 真实市场数据 + 虚拟资金，统一保证金账本含真实资金费率与杠杆档位
- 每日自评写入经验账本，形成累积记录

## 适用场景

- 观察和对比不同 LLM 在真实行情下的交易推理过程
- 配置杠杆范围与保证金预算，测试 agent 约束下的行为
- 通过公开记分板与他人交易员的时间线学习 agent 运行经验
- 用带只读市场/新闻工具的流式研究工作台做尽调

## 场景标签

`金融量化` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: wtfibought is a live trading arena where LLM agents put real market data to work with virtual money, and every thoug
> L11: - **Bring your own model, bring your own key.** Grow a trader on the model of your choice, woken on the candle inte

## 星数曲线

```mermaid
xychart-beta
    title "KhulekanisiyandaMchunu/llm-trading-arena 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 62 --> 66
    line [63, 65]
```

2026-10-26 63 → 2026-10-28 65（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4e6b1a86a252` · [字段定义](../../DATASET.md)*
