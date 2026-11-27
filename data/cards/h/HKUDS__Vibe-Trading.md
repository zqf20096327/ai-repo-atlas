# HKUDS/Vibe-Trading

⭐ 38,992 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/HKUDS/Vibe-Trading) · [官网](https://vibetrading.wiki/) · 组织维护 · 中文 README

**面向个人交易者的量化交易 Agent：研究、回测与模拟交易**

以 Python 包发布的个人交易 Agent，功能覆盖策略研究（Research Lab）、回测（含 A 股、台股、加密货币等市场）、期权分析（Options Lab）、风险分析（Risk X-Ray）、影子账户与模拟交易对账。市场数据经统一网关聚合 Yahoo Finance、Eastmoney、Tencent、AKShare 等来源，LLM 接入经统一网关，支持 Agent/CLI/API/MCP 多种形态，可经飞书、DingTalk、Napcat 等通道交互，实盘交易设有用户授权限额机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 13,180 位贡献者
- 涨星:近 1 天 **+87**(自 20261016 起算)
- 安装:pypi 包 `vibe-trading-ai` 月下载 6,681
- 平台:— · 协议:MCP

## 能力要点

- Research Lab 支持 walk-forward 验证与冻结数据回放
- 统一市场数据网关与统一 LLM 网关（Agent/CLI/API/Swarm 共享）
- Options Lab 期权策略计算与多方案对比导出（JSON/CSV）
- 提供 pip 安装、桌面版（带签名更新）与 MCP 接口

## 适用场景

- 为股票、期权、加密货币策略做多市场回测与验证
- 通过 Agent/MCP 工具做期权策略对比与风险归因
- 在 A 股 5 分钟模拟盘上做模拟交易并独立对账

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5:  Vibe-Trading: Your Personal Trading Agent
> L7:  One Command to Empower Your Agent with Comprehensive Trading Capabilities
> L76: - **2026-11-19** 📄 **Technical report published** — The report describes how Vibe-Trading traces results to source 

## 星数曲线

```mermaid
xychart-beta
    title "HKUDS/Vibe-Trading 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 36264 --> 39240
    line [36512, 36667, 36751, 36858, 37026, 37147, 37227, 37290, 37367, 36512, 37890, 38000, 38056, 38110, 38164, 38227, 38314, 38387, 38442, 38489, 38542, 38612, 38648, 38699, 38740, 38924, 38992]
```

2026-10-25 36,512 → 2026-11-27 38,992（+2,480）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `750d90e84f7f` · [字段定义](../../DATASET.md)*
