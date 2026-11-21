# oficcejo/alphapilot

⭐ 10 · Python · 推送 2026-11-19 · [GitHub](https://github.com/oficcejo/alphapilot) · [官网](https://discord.gg/jk4mnW53gK) · 个人维护 · 中文 README

**面向 OKX 交易所的 AI 量化交易平台：自动挖掘 Alpha 因子并支持实盘交易**

基于强化学习（REINFORCE）与 Looped Transformer 的量化研究与交易平台，覆盖数据下载、因子挖掘、回测、实盘交易与自进化闭环。模型从 81 个因果特征与 79 个算子中搜索因子公式，支持多因子组合、WebSocket 实时推送、波动率体制感知与 5 重影子门禁的策略原子热交付。默认模拟盘（paper）模式，实盘需显式开启并配置 OKX API 凭证；README 明示不保证收益。提供 Python 源码与 Docker 两种部署方式。

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

- REINFORCE + Looped Transformer 自动搜索因子公式（81 特征 / 79 算子）
- Reef 自进化闭环：实盘因果归因、遗传变异繁衍与 5 重门禁原子交付
- OKX v5 WebSocket 实时行情/持仓推送，自动断线重连
- 7 页 Web 平台覆盖训练、回测、实时分析、实盘与自进化监控

## 适用场景

- 在 OKX 上自动挖掘并回测 Alpha 因子策略
- 以 paper 模式验证策略后再分级切换实盘
- 基于实盘账单对齐做策略归因与持续迭代

## 场景标签

`金融量化` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L5: **OKX AlphaPilot** 是一个面向 OKX 交易所的独立量化研究与自进化交易平台。它基于强化学习（REINFORCE）+ Looped Transformer 架构，自动搜索由 **81 个因果特征**和 **79 个
> L43: - **强化学习搜索**：REINFORCE 策略梯度 + Actor-Critic baseline，搜索 8-token 公式序列
> L44: - **Looped Transformer**：GPT 风格模型 + QK-Norm 注意力 + 权重共享输出头


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `baf71ceba610` · [字段定义](../../DATASET.md)*
