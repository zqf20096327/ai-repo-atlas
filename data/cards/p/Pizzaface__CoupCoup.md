# Pizzaface/CoupCoup

⭐ 17 · Python · 推送 2025-11-23 · [GitHub](https://github.com/Pizzaface/CoupCoup) · 个人维护

**AI 驱动的超市优惠券自动匹配与购物路线规划工具**

用 Python（poetry 管理）编写的自动化省钱工具：爬取各超市每周促销广告与优惠券，调用 Google Gemini API（Vertex 或 AI Studio，使用 Function Calling）以结构化方式提取在售商品与优惠券适用商品，再由 AI 匹配优惠券与促销，计算折扣是否划算；并通过 OpenRouteService API 规划到各店的路线，最终生成包含指引与各店优惠信息的单页 HTML。需配置 config.ini 提供 Google API Key、店铺与优惠券来源清单；路线功能依赖 OpenRouteService API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取每周促销广告与优惠券，Gemini Function Calling 提取结构化数据
- AI 匹配优惠券与在售商品，判定折扣价值
- OpenRouteService 规划多店购物路线，生成单页 HTML 指引
- 区分全局（厂商）与门店两级优惠券提取

## 适用场景

- 自动汇总本地超市每周促销与可用优惠券
- 规划一趟覆盖最优折扣的多店购物路线
- 生成可打印的单页购物指引与各店优惠清单

## 场景标签

`网页抓取` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L59: 2. **AI Analysis and Extraction**: CoupCoup uses Google's Gemini API (via Vertex or AI Studio) to analyze the weekl
> L64: 5. **Matching Coupons to Sales**: CoupCoup uses AI to match the coupons to the sales. It compares the items on sale

## 星数曲线

```mermaid
xychart-beta
    title "Pizzaface/CoupCoup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ed90d58a0d52` · [字段定义](../../DATASET.md)*
