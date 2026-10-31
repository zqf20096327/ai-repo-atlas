# Irenezhangtt/AskingMe-Agent

⭐ 17 · Python · 推送 2026-09-24 · [GitHub](https://github.com/Irenezhangtt/AskingMe-Agent) · [官网](https://irenezhangtt.github.io/AskingMe-Agent/) · 个人维护 · 中文 README

**促销规则最终价格计算 Agent：证据检索+规则解读+精确算术**

面向需要从复杂促销规则得出实付金额的用户的应用：上传政策文件或截图，系统经视觉/文本抽取、有效期与标签审核、订单事实核验后，由 LLM 解读证据生成带引用的计算计划，再用 Decimal 工具执行有界算术并输出中间步骤。自然语言问答路径经 Elasticsearch BM25+BGE 向量混合检索（RRF 融合）与 Cross-Encoder 重排。提供 Docker Compose 部署，需 Anthropic 兼容 API key；附带 500 例合成评测集，README 自述重排后召回出现回退。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 上传文档/截图→抽取→日期门控→计划→Decimal 计算的可审计流水线
- Elasticsearch BM25+BGE 混合检索以 RRF 融合，Cross-Encoder 重排
- 有界 Decimal 表达式工具与最终 half-up 舍入，暴露中间结果
- 规则文档治理：草稿、审批、替换、归档、删除

## 适用场景

- 上传促销政策文档，核验条件后计算订单最终实付价
- 自然语言询问叠加多种优惠后的应付金额并获得带引用的计算过程
- 企业维护审批后的规则知识库供检索计算

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L23: The full application opens with **Final Price Agent** chat. Select **Policy Calculator** for your own documents. Up
> L46: In the current source, natural-language questions pass through Elasticsearch hybrid retrieval and evidence selectio
> L58: AskingMe connects **evidence retrieval**, **rule interpretation**, and **executable arithmetic**. The agent produce

## 星数曲线

```mermaid
xychart-beta
    title "Irenezhangtt/AskingMe-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d0b289ba0461` · [字段定义](../../DATASET.md)*
