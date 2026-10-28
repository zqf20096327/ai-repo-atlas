# HephaestLab/TraderHarness

⭐ 42 · Python · NOASSERTION · 推送 2026-08-22 · [GitHub](https://github.com/HephaestLab/TraderHarness) · [官网](https://hephaestlab.github.io/TraderHarness/) · 组织维护 · 中文 README

**LLM 交易 Agent 的抗污染回测环境与训练轨迹生成器（A股）**

面向 LLM 交易 Agent 的回测执行环境兼训练数据合成器：用真实 A 股数据（五年日线/5分钟线、公告、基本面）构建历史环境，通过时点掩码、日期与公司匿名化防止数据泄漏；Agent 只能经 TradingBus.place_order() 唯一路径按真实价格撮合成交。每次 LLM 调用被全保真记录为可指纹回放的 cassette，可无 Key 确定性重放，并导出 OpenAI 风格 SFT 轨迹。附带本地研究控制台（FastAPI+React）、四张内置 Agent 卡与 compare/委员会两种运行形态。当前仅虚拟资金、无实盘 Broker 接口，数据集仅覆盖 A 股。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 时点掩码 + 日期/实体双重匿名化的抗污染回测环境
- 全保真轨迹记录与无 API Key 的确定性指纹回放（traderharness audit/export）
- 5 分钟渐进可见 + 分钟级撮合的公平成交与唯一下单路径 TradingBus
- 内置本地研究控制台与 1–4 Agent 同场每日模拟盘

## 适用场景

- 我想在避免数据泄漏的前提下评测 LLM 交易 Agent 的真实表现
- 把回测运行导出为强化学习/行为分析用的训练轨迹
- 在相同掩码市场上对比多个交易 Agent 或模型检查点

## 场景标签

`多智能体` `模型评测` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L17: TraderHarness 就是这套规范：一个抗污染的 LLM 交易 Agent 回测执行环境——同时，由于每次模型调用都被全保真记录，它也是一个把这些运行一键变成轨迹训练数据的数据合成器。
> L63: 2. **指纹回放。** 生成的 cassette 可以在没有 API Key 的情况下确定性重放；分享之前，`traderharness audit` 会扫描序列化产物中泄漏的实体与日期。
> L48: > 这是一组小样本、单 Agent 风格的冒烟基准，用于演示评测链路，不构成模型排名或投资建议。每一次调用都可指纹回放，完整契约见训练数据。

## 星数曲线

```mermaid
xychart-beta
    title "HephaestLab/TraderHarness 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-28 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8912ebef818a` · [字段定义](../../DATASET.md)*
