# EchoSentiment/Echo

⭐ 23 · TypeScript · 推送 2026-06-22 · [GitHub](https://github.com/EchoSentiment/Echo) · 组织维护

**扫描 Crypto Twitter、按叙事持久度打分的 Solana 交易信号工具**

Echo 追踪 Solana 代币的 Crypto Twitter 提及，将相似声明聚类为叙事通道，按可信度、来源多样性、持久度与矛盾度四个维度计算持久性得分（固定权重公式），再由 Claude agent 判定每条叙事为 durable、contested 或 fading，输出带操作提示的排序叙事看板。内置风险控制：过滤单集群回声、弱账号刷量与高矛盾叙事。面向需要区分炒作与持久叙事的交易操作者。以 TypeScript/Bun 提供，git clone 源码运行，需 ANTHROPIC_API_KEY 与 TWITTER_BEARER_TOKEN。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四维度持久性评分公式（credibility/source_diversity/persistence/contradiction）
- Claude agent 对叙事做 durable/contested/fading 判定
- 矛盾检测与单集群回声过滤等风险控制
- 输出带操作提示的排序叙事信号看板

## 适用场景

- 追踪 Solana 代币叙事是持续还是一小时热度
- 在采取交易动作前查看叙事的矛盾与可信度证据
- 过滤弱账号刷量形成的高声量叙事

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: `Echo` fetches recent tweets for tracked Solana symbols, models author credibility and source diversity, and then a
> L3: **Crypto Twitter narrative durability engine for Solana.**

## 星数曲线

```mermaid
xychart-beta
    title "EchoSentiment/Echo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `34b0fcc9befb` · [字段定义](../../DATASET.md)*
