# iloveitaly/lunchmoney-amazon

⭐ 27 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/iloveitaly/lunchmoney-amazon) · 个人维护

**用 LLM 自动分类 LunchMoney 中 Amazon 交易的个人记账工具**

命令行工具：读取浏览器扩展导出的 Amazon 订单 CSV（或 amazon-shopping-mcp 的 JSONL），将订单条目发给 LLM（经 Pydantic AI，默认 Google Gemini）按 LunchMoney 账户中已有的类别分类，匹配交易并把商品摘要与订单号写入交易备注；收件人非账户所有者时标记为礼物。支持 OpenAI/Anthropic/Gemini 等多种 AI 提供商，可先 dry-run 校验缺失类别。面向使用 LunchMoney 记账的个人用户，依赖订单导出扩展提供数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM（Pydantic AI，默认 gemini）按 LunchMoney 类别对 Amazon 订单分类
- 交易备注写入商品摘要与订单号
- 支持 azad CSV 与 amazon-shopping-mcp JSONL 两种订单格式
- 礼物检测：收件人非所有者时标记

## 适用场景

- 把我一个月的 Amazon 消费拆到具体记账类别
- 给 LunchMoney 交易补充订单号和商品明细备注
- 识别代他人购买并标记为礼物

## 场景标签

 · 领域:个人财务/工具

## 证据(README 行号)

> L13: mapping between transaction and category. To solve this, we pipe the list of items to an LLM via Pydantic AI and as
> L19: - Support for multiple AI providers via Pydantic AI, with Google Gemini as the default (`google:gemini-3.8-flash`)

## 星数曲线

```mermaid
xychart-beta
    title "iloveitaly/lunchmoney-amazon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e2de7619e2a8` · [字段定义](../../DATASET.md)*
