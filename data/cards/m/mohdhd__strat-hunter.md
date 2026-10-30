# mohdhd/strat-hunter

⭐ 18 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/mohdhd/strat-hunter) · 个人维护

**自托管仪表盘：用 AI 编程助手研究并回测交易策略**

面向单一可信操作者的自托管 Web 仪表盘：用户以日常语言描述交易想法，应用启动 AI 编程助手（如 claude CLI）编写策略代码、运行历史回测并记录迭代过程；也可用 Scout 扫描器批量提出假设。支持 Freqtrade（Binance USDT 加密期货）与 NautilusTrader（外汇/股票/ETF 等）两种引擎，可对比迭代历史、独立验证结果，并导出含代码与指标的 ZIP。无应用层登录，仪表盘与 API 可启动程序和修改文件，结果需人工复核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 驱动 AI 编程助手生成策略代码并运行历史回测
- Scout 扫描器批量提出交易假设供人工放行
- 支持 Freqtrade 与 NautilusTrader 两种回测引擎
- 导出含策略代码、指标与引擎说明的 ZIP 包

## 适用场景

- 不用写代码，用自然语言让 AI 助手研究我的交易想法
- 批量扫描候选交易假设并挑选一个深入研究
- 对比多轮回测迭代与独立验证结果后导出策略

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **Use AI coding assistants to investigate trading ideas and organize the results in a web dashboard.**
> L9: Describe an idea in everyday language. Strat Hunter starts a coding assistant that writes strategy code, runs histor
> L53: docker compose exec backend claude

## 星数曲线

```mermaid
xychart-beta
    title "mohdhd/strat-hunter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f37417d638c4` · [字段定义](../../DATASET.md)*
