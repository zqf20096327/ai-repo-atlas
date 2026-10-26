# tgel0/crssnt

⭐ 97 · JavaScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/tgel0/crssnt) · [官网](https://crssnt.com) · 个人维护

**把 RSS/Atom 订阅源转换为 LLM 友好 Markdown/JSON 的 API 服务**

crssnt 是开源的 feed 转换服务：读取 RSS/Atom 订阅源 URL（最多 10 个），输出面向语言模型的 Markdown 或 JSON，支持 llm_compact 紧凑模式、group_by_feed 按源分组与 max_items 限量；也可从公开 Google Sheet 生成 RSS/Atom/JSON/Markdown 订阅源。以 HTTPS 端点（crssnt.com）形式提供服务，可自托管为 Firebase Cloud Functions，本地用 Firebase Emulator Suite 测试。/preview 端点已弃用。处理过程不存储 feed 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RSS/Atom 转 Markdown/JSON，带 llm_compact 紧凑输出选项
- 多 feed 聚合并按日期自动排序、按源分组
- 从公开 Google Sheet 生成 RSS/Atom/JSON/Markdown
- 可自托管为 Firebase Cloud Functions

## 适用场景

- 把新闻等订阅源内容接入 AI 工作流作为上下文
- 用 Google Sheet 作为数据源发布订阅源
- 聚合多个信息源生成统一的结构化输出

## 场景标签

 · 领域:数据转换/LLM 输入准备

## 证据(README 行号)

> L14: `crssnt` converts RSS/Atom feeds into LLM-friendly Markdown or JSON. This simplifies integrating feed content into 
> L31: * **LLM-Optimized Conversion:** Transforms RSS/Atom feeds into structured Markdown or JSON, with an `llm_compact` o

## 星数曲线

```mermaid
xychart-beta
    title "tgel0/crssnt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-26 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `aa6ef985cacb` · [字段定义](../../DATASET.md)*
