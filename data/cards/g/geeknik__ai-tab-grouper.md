# geeknik/ai-tab-grouper

⭐ 16 · JavaScript · GPL-3.0 · 推送 2026-09-06 · [GitHub](https://github.com/geeknik/ai-tab-grouper) · [官网](https://deepforkcyber.com/) · 个人维护

**Brave 浏览器扩展：本地文本分析算法自动分组标签页**

面向 Brave 用户的标签页管理扩展，用 TF-IDF、BM25、关键词短语提取、LSA 及量子混沌（QCO）等文本分析算法将相关标签页自动归组，支持自定义相似度阈值、分组周期与算法参数，固定标签页始终被忽略。所有处理在浏览器本地完成，不收集或传输个人数据。安装方式为克隆源码后通过 brave://extensions 以开发者模式加载未打包扩展；Firefox 支持列为未来计划。以 GPLv3 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 5 种可选分组算法（TF-IDF/BM25/Keyphrase/LSA/QCO）
- 全部处理本地进行，不收集传输个人数据
- 可配置自动分组周期、相似度阈值与算法参数
- 针对研究、工作、购物等场景给出预置配置建议

## 适用场景

- 自动把大量打开的网页按主题整理成标签组
- 研究或购物时按内容相似度归类多个来源的页面
- 隐私敏感环境下本地整理标签页

## 场景标签

 · 领域:浏览器工具/生产力

## 证据(README 行号)

> L3: AI Tab Grouper is a Brave extension that automatically organizes your tabs into groups using AI-powered text analysi
> L20: - Respects user privacy by performing all processing locally
> L157: This extension does not collect or transmit any personal data. All text analysis and grouping operations are **per

## 星数曲线

```mermaid
xychart-beta
    title "geeknik/ai-tab-grouper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ec7ba5734a3f` · [字段定义](../../DATASET.md)*
