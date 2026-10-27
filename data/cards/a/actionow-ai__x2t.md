# actionow-ai/x2t

⭐ 22 · TypeScript · MIT · 推送 2026-06-11 · [GitHub](https://github.com/actionow-ai/x2t) · [官网](https://x2t.actionow.ai) · 组织维护 · 中文 README

**自托管应用：AI 读取财经博主帖子并按战绩回测追踪其立场**

X2T 监听 X（Twitter）、Reddit 与新闻源上的财经博主帖子，用 LLM agent 结合实时行情数据，将每条帖子判定为对特定 ticker 的看多/看空/中立立场；立场聚合为个股共识、多空辩论与立场图谱，立场转向即时推送。每条方向性判断以同窗口 SPY 回测 5 个交易日，附 Wilson 置信区间与 FDR 校正的排行榜。支持任意 OpenAI/Anthropic 兼容端点（多供应商降级链），双语界面，单容器部署（Docker 为唯一前置），声明非投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM agent 结合实时行情做多语言帖子的 ticker 级看多/看空标注，带校准置信度
- 每条判断按同窗口 SPY 回测，Wilson 95% 置信区间、最小样本门槛与 Benjamini–Hochberg FDR 校正排行
- 立场转向检测与即时推送、可组合告警规则、结构化 RSS（x2t:stance / x2t:flip）
- 自带 RSSHub 网关多源接入，Docker 一键部署，零 key 可在 mock 上运行

## 适用场景

- 追踪我关注的财经博主实际喊单方向与其真实胜率
- 在多空分歧的个股上查看博主共识与辩论论据
- 自托管接收博主立场转向的推送与结构化 RSS 信号流

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L15: X2T watches the financial influencers you follow on X (Twitter), Reddit and news feeds, and reads every post — with
> L31: |**Grounded AI analysis**|An LLM agent reads each post in its original language, extracts tickers (cashtags + compa

## 星数曲线

```mermaid
xychart-beta
    title "actionow-ai/x2t 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b8898c9abc56` · [字段定义](../../DATASET.md)*
