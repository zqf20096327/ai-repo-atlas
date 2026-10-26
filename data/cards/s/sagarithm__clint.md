# sagarithm/clint

⭐ 31 · Python · MIT · 推送 2026-06-10 · [GitHub](https://github.com/sagarithm/clint) · 个人维护

**面向企业的 AI 潜在客户发现与外联自动化库/CLI**

以 Python 库和 CLI 形式提供的线索生成与外联自动化套件：从查询（如『加州牙医』）抓取并丰富线索数据，基于 OpenRouter API 用 LLM 做审计式个性化内容与提案生成，再经邮件/WhatsApp 渠道执行多步跟进。默认 dry-run 安全模式，含本地 dashboard 与数据导出。限制：依赖 Playwright/Chromium 抓取，建议日发送量约 200 邮件加 200 WhatsApp 消息以降低检测风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端自治活动：发现→丰富→个性化→外联
- 基于 AI 的审计与提案生成
- 邮件与 WhatsApp 双渠道多步跟进
- 默认 dry-run 安全模式与本地 dashboard

## 适用场景

- 按行业与地区查询批量发现潜在客户线索
- 基于线索数据生成个性化外联内容并自动发送
- 管理多步跟进活动并通过 dashboard 查看与导出数据

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L25: engine = Engine(api_key="your_openrouter_key")
> L31: - End-to-end autonomous campaigns (discover, enrich, personalize, outreach)
> L32: - AI-based audit and proposal generation

## 星数曲线

```mermaid
xychart-beta
    title "sagarithm/clint 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `523e42b8cdad` · [字段定义](../../DATASET.md)*
