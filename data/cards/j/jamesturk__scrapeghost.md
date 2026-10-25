# jamesturk/scrapeghost

⭐ 1,439 · Python · NOASSERTION · 推送 2026-01-14 · [GitHub](https://github.com/jamesturk/scrapeghost) · [官网](https://jamesturk.github.io/scrapeghost/) · 个人维护

**用 GPT API 抓取网页并结构化提取数据的 Python 库（已停止维护）**

2023 年发布的实验性 Python 库，调用 OpenAI GPT API 从网页提取数据：用 Python 对象定义 schema，提供 HTML 清洗、CSS/XPath 预过滤、大页面自动拆分、JSON/pydantic 校验、幻觉检查及 token 计数、预算控制与模型降级回退等机制。面向做 GPT 网页抓取实验的开发者。README 明确声明项目已不再维护，且单次 GPT-4 调用成本较高（约 $0.36），风险自担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Python 对象定义提取数据的 schema
- HTML 清洗、CSS/XPath 预过滤与大页面自动拆分为多次调用
- JSON/pydantic 校验与幻觉检查（数据是否真实存在于页面）
- token 成本追踪、预算上限与 GPT-3.5→GPT-4 回退策略

## 适用场景

- 用 GPT 从网页按自定义 schema 提取结构化数据
- 控制 GPT 抓取的 API 成本与预算
- 校验 GPT 提取结果是否符合 schema 且无幻觉

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: `scrapeghost` **was** an experimental library for scraping websites using OpenAI's GPT.
> L19: The purpose of this library is to provide a convenient interface for exploring web scraping with GPT.

## 星数曲线

```mermaid
xychart-beta
    title "jamesturk/scrapeghost 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 1438 --> 1440
    line [1439, 1439]
```

2026-10-18 1,439 → 2026-10-25 1,439（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `191322bc5c66` · [字段定义](../../DATASET.md)*
