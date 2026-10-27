# al1enjesus/polyclawster

⭐ 22 · JavaScript · 推送 2026-03-16 · [GitHub](https://github.com/al1enjesus/polyclawster) · 个人维护

**AI agent 自动交易 Polymarket：读语音/推文/视频信号下单**

面向预测市场交易者：部署基于 OpenClaw 的交易 agent，读取语音、推文、YouTube/文章等信号，匹配 Polymarket 市场，0-10 打分后（7 分以上）自动下单。私钥本地生成与签名，非托管。提供对话模式、监控 200+ 巨鲸钱包的自动模式、外部 agent 协议同步交易记录、Telegram 应用与公开排行榜。安装方式为 clawhub install，另有 setup/trade/auto 等 Node.js 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音/推文/视频多源信号触发交易，置信度 7+ 才执行
- 监控 200+ 巨鲸钱包的自动交易模式
- 非托管：私钥本地生成，签名不离本机
- 提供 Telegram 应用与公开 agent 排行榜

## 适用场景

- 用自然语言指令在 Polymarket 下单或查询持仓
- 让 agent 跟随巨鲸钱包信号自动交易
- 通过 Telegram 无代码参与预测市场交易

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **Deploy an AI agent that reads any signal — voice, tweet, YouTube video — and trades Polymarket autonomously. 24/7.
> L42: The agent reads the content, finds the best matching market, scores confidence, and places the trade — or explains 

## 星数曲线

```mermaid
xychart-beta
    title "al1enjesus/polyclawster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4c16093f9cc2` · [字段定义](../../DATASET.md)*
