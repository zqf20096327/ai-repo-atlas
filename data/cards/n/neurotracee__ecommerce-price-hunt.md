# neurotracee/ecommerce-price-hunt

⭐ 3 · Python · MIT · 推送 2026-11-09 · [GitHub](https://github.com/neurotracee/ecommerce-price-hunt) · [官网](https://github.com/ccch1mneyyy/dsh-go/) · 个人维护 · 中文 README

**给 AI Agent 用的电商全网比价 Skill 包（含国药准字药品专项）**

为 DSH go（DeepSeek Harness 二开方向）制作的附属 Skill 仓库：内容只有提示词与操作手册，不含可执行采集代码。Agent 依赖自身的读屏/UI 操作能力，逐平台读取同一商品到手价、发货地与时效，按统一口径（元/克、元/ml、元/片）换算后交付单文件 HTML 报告。含药品专项：以国药准字+OTC/RX 闸门排除妆/食/健/消/械字号产品。通过 Release zip 交给 DSH 一句话安装，也支持其他宿主的手动放置；文档 CC BY-SA 4.0、代码 MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨平台比价：京东、拼多多、淘宝网页版、抖音商城、快手商城、美团买药
- 药品专项：国药准字+OTC/RX 闸门，默认排除非药字号产品
- 提示词+操作手册形式，按需加载手册以减少每轮输入 token
- 随包内置 HTML 报告与可视化技能（vendor/），不绑定宿主

## 适用场景

- 让具备读屏能力的 Agent 帮我在多个电商平台比同一商品的到手价
- 买药时避免把国药准字药品误买成食字号/妆字号产品
- 给自定义 Harness 或 Claude Code 之类的宿主添加比价提示词

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: > 这是为 **DSH go** 做的一个**附属功能的开源项目**：把「让 AI 自动完成商品全网比价」这项能力，以一份可复用的 Skill（提示词 + 操作手册）形式沉淀下来，供 DSH go 及其他具备读屏能力的 AI Age
> L111: **不是**爬虫库，**不是**价格 API，**不是**自动化脚本。它是**提示词 + 操作手册**，靠 Agent 自身的 UI 操作能力落地。仓库里没有可执行的价格采集代码，也不会有。

## 星数曲线

```mermaid
xychart-beta
    title "neurotracee/ecommerce-price-hunt 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5bb2a8de4686` · [字段定义](../../DATASET.md)*
