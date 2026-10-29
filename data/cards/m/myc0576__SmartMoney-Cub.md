# myc0576/SmartMoney-Cub

⭐ 27 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/myc0576/SmartMoney-Cub) · 个人维护 · 中文 README

**只读式交易复盘记录与评审工具：给主观交易者留存证据链**

面向主观 A 股交易者的本地优先交易日志与复盘框架：对市场与执行只读（不下单、不撤单、不连券商），对用户自己的日志可写。外部 Agent 或 CLI 调用产生 Run Envelope 与 Evidence Pack，经确定性重放、D1/D3 结果评审与人工晋级门槛后进入规则演化。支持 Jev（TypeSafe/OpenRouter）可选类型化判断层，内置含 240 案例的冻结离线基准 finance-jev-v1；另提供自托管 OpenAI 兼容网关 alphatech.net.cn（可选，人民币计费）。核心无内嵌 LLM、无券商连接，Python 包不在 PyPI，经 GitHub Releases 的 wheel 或源码 pip -e 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Run Envelope / Evidence Pack 冻结工件与确定性重放，SHA256 封存清单防篡改
- 内置 240 案例、四赛道的 finance-jev-v1 冻结离线基准
- 可选 Jev 类型化判断层（TypeSafe 直连 / OpenRouter 双后端），算术与时间校验仍由确定性 Python 执行
- 声明式只读策略 READ_ONLY_NO_ORDER_NO_CANCEL_NO_TRADE，规则晋级需人工门槛

## 适用场景

- 把每日交易计划、持仓截图与成交记录整理成可复盘的证据链
- D1/D3 结果出来后评审规则应晋级、降级还是删除
- 用冻结基准离线评测 LLM 在金融判断任务上的表现
- 让外部 Agent 跑离线任务并生成可审计、可重放的评审工件

## 场景标签

`金融量化` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: `smartmoney-cub-harness` is a **local-first, agent-agnostic trading journal and review harness**: read-only over ma
> L20: External Agent or CLI caller → Run Envelope → frozen Benchmark/Evidence Pack → deterministic replay → explicit huma
> L26: SmartMoney-Cub supports Jev (TypeSafe | OpenRouter) as an optional typed-judgment layer with two pluggable backends

## 星数曲线

```mermaid
xychart-beta
    title "myc0576/SmartMoney-Cub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1174ac581b80` · [字段定义](../../DATASET.md)*
