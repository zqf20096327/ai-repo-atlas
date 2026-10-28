# Xenolphthalein/toolbox-for-firefly-iii

⭐ 25 · TypeScript · Unlicense · 推送 2026-04-04 · [GitHub](https://github.com/Xenolphthalein/toolbox-for-firefly-iii) · 个人维护

**Firefly III 交易管理工具箱：去重、订阅分析、AI 分类与银行导入**

面向 Firefly III 自托管记账用户的 Web 工具套件，通过 Firefly III API 代理操作交易数据。功能含重复交易检测（多因子置信度评分）、订阅模式识别、基于 OpenAI 或本地 Ollama 的 AI 分类与标签建议、Amazon/PayPal 导出数据补全、可视化列映射的 CSV 导入及德国银行 FinTS 直连导入（支持 TAN）。提供 Docker 与 Node.js 20+ 源码两种安装方式，单租户架构，支持 Basic/OIDC/Firefly OAuth 认证。README 披露代码由 AI 工具生成并由开发者监督。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重复交易检测与订阅模式识别并可转 Firefly III 周期交易
- AI 分类/标签建议支持 OpenAI 或本地 Ollama，含置信度评分与批量应用
- Amazon/PayPal 导出数据补全交易明细
- FinTS 直连德国银行导入（支持 TAN）与可视化 CSV 导入

## 适用场景

- 清理 Firefly III 中的重复与未分类交易
- 识别周期性订阅支出并转为周期交易
- 从德国银行、CSV 或 Amazon/PayPal 导入补全账单明细

## 场景标签

 · 领域:个人财务/记账工具

## 证据(README 行号)

> L10: Web automation suite for Firefly III. Includes tools for duplicate detection, subscription analysis, AI-powered cat
> L33: Suggests categories for uncategorized transactions using OpenAI or Ollama. Matching is done against existing Firefl
> L142: AI features (category and tag suggestions) require either OpenAI or a local Ollama instance.

## 星数曲线

```mermaid
xychart-beta
    title "Xenolphthalein/toolbox-for-firefly-iii 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `323408ec81b7` · [字段定义](../../DATASET.md)*
