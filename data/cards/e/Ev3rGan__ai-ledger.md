# Ev3rGan/ai-ledger

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/Ev3rGan/ai-ledger) · [官网](https://bench-tencent-hk.ai-ledger.cn/) · 个人维护 · 中文 README

**证据可溯源的 AI 日报服务：审阅发布 Digest 与带引用的研究问答**

一个面向公开情报跟踪的 Web 服务：从版本化来源清单采集信息，生成 Story→Claim→Evidence 结构的草稿记录，由操作员通过受保护控制台审阅并批准不可变的 Digest Plan 后才发布；自动化不能自行发布。研究问答仅检索已接受知识，采用 PostgreSQL 全文+实体候选、MiniLM 向量与 mMARCO 重排的混合检索，带失效关闭的引用校验并明确拒绝无支撑回答。提供 RSS、公开浏览页面与本地/生产运行手册，CLI 可跑确定性样例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 操作员审批不可变 Digest Plan 后才能发布，自动化不可自行发布
- Story→Claim→Evidence 结构化记录并保留原始来源链接
- 混合检索：PostgreSQL 全文/实体候选 + MiniLM 向量 + mMARCO 重排，含无模型回退
- 研究问答仅基于已接受知识，引用校验失效即明确拒绝回答

## 适用场景

- 跟踪 AI 领域动态并获得可溯源到原文的日报
- 运营一个小型、可审计的公开情报发布服务
- 对已发布知识提出带引用的研究型问题

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **An evidence-grounded AI daily that turns approved public sources into reviewed Digests and cited Research.**
> L13: AI Ledger is a compact public-intelligence service for following AI developments without losing the evidence behind
> L38: |Bounded Research|Lookup, comparison, timeline, and bounded multi-hop questions use isolated Evidence Sets, strict 

## 星数曲线

```mermaid
xychart-beta
    title "Ev3rGan/ai-ledger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fd968411e2f5` · [字段定义](../../DATASET.md)*
