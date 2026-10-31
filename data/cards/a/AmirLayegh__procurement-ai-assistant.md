# AmirLayegh/procurement-ai-assistant

⭐ 37 · TypeScript · MIT · 推送 2026-01-26 · [GitHub](https://github.com/AmirLayegh/procurement-ai-assistant) · 个人维护

**零售采购人员的自然语言语义搜索助手**

面向零售采购（及营销）团队的应用：买家用英语提问（如“50 美元以下可持续连衣裙且供应商可靠”），系统通过 Superlinked 语义检索框架 + Qdrant/内存向量库返回商品与供应商指标（利润率、退货率、供应商可靠性）。后端为 Python/FastAPI，部署到 Google Cloud Run，用 OpenAI GPT-4 处理自然语言；前端生产用 Next.js，本地开发用 Streamlit。数据来源为含供应商指标的 CSV 目录。系 Firebase Studio 黑客松 2025 获奖项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言采购查询，响应时间低于 3 秒
- 基于 Superlinked 框架与 Qdrant/内存向量库的语义检索
- 供应商可靠性、利润率、退货率等指标分析
- 后端可部署至 Google Cloud Run，前端部署至 Firebase Hosting

## 适用场景

- 采购人员用自然语言查找符合成本与供应商要求的商品
- 营销团队复用同一查询获取商品表现数据
- 在等待工程团队出数据前自助完成采购决策查询

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L14: Procurement AI Assistant transforms how retail buyers make purchasing decisions by providing instant, intelligent i
> L18: - 🗣️ **Natural Language Search** - Query using plain English

## 星数曲线

```mermaid
xychart-beta
    title "AmirLayegh/procurement-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `50ebaac78c08` · [字段定义](../../DATASET.md)*
