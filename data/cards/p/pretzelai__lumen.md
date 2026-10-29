# pretzelai/lumen

⭐ 29 · TypeScript · Apache-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/pretzelai/lumen) · [官网](https://getlumen.dev) · 组织维护

**面向 SaaS 的计费与功能授权平台，按功能而非套餐管理访问**

Lumen 是面向 SaaS 开发者的计费与授权（entitlements）平台：以功能（feature）为核心组织访问控制，通过 isFeatureEntitled 等 API 判断用户是否有权使用某功能，替代散落在代码中的套餐判断逻辑。支持基于用量的计费、内置 React 定价表与用量组件，由平台处理 Stripe webhook 编排；非技术成员可通过 Dashboard 修改定价。支付集成覆盖 Stripe 与 Dodo Payments，Paddle、checkout.com、Razorpay、Adyen 为计划中。服务印度、美国与欧洲商户，提供 npm 安装与自托管开发环境（Docker 含 PostgreSQL/MinIO/pgAdmin）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- feature-first 的功能授权 API（isFeatureEntitled/sendEvent）
- 平台代管 Stripe webhook 编排
- 内置 shadcn React 定价表与用量跟踪组件
- 支持基于用量的计费与 Dashboard 免代码改价

## 适用场景

- SaaS 应用快速接入订阅计费与功能门控
- 产品/运营人员不改代码调整套餐与试用策略
- 按功能使用量进行计量计费

## 场景标签

 · 领域:SaaS 计费/支付基础设施

## 证据(README 行号)

> L18: The fastest way to add billing and feature access to your SaaS. Lumen is PSP agnostic and support merchants in Indi
> L29: Lumen is a modern billing and entitlements platform that eliminates the complexity of implementing subscription man
> L50:   await isFeatureEntitled({ feature: "advanced-analytics", userId: user.id })

## 星数曲线

```mermaid
xychart-beta
    title "pretzelai/lumen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [30, 29, 29]
```

2026-10-18 30 → 2026-10-29 29（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8bccdd26b6f1` · [字段定义](../../DATASET.md)*
