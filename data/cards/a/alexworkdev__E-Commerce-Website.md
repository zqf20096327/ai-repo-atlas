# alexworkdev/E-Commerce-Website

⭐ 18 · JavaScript · 推送 2026-06-23 · [GitHub](https://github.com/alexworkdev/E-Commerce-Website) · 个人维护

**带 AI 商品推荐的 MERN 全栈电商网站**

全栈电商平台：React 前端、Node.js/Express 后端、MongoDB Atlas 数据库，商品数据来自 MongoDB 与 DummyJSON API。功能包括 Auth0 认证、实时联想搜索、购物车、管理员添加商品面板。AI 部分为独立 Python Flask 推荐服务（部署于 Render），按购买历史、类别偏好、相似属性、价格区间和热门趋势生成商品推荐，可扩展接入更高级 ML 模型。部署依赖 Vercel/Render，需在 .env 中配置 MongoDB URI 与 Auth0 凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python Flask 推荐服务：按购买历史/类别/相似属性/价格区间/热门生成推荐
- Auth0 认证与实时联想搜索（类 Amazon）
- 管理员商品添加面板与购物车功能
- 前端、后端、ML 服务三部分分别本地可运行

## 适用场景

- 搭建带商品推荐的电商网站
- 学习 MERN 全栈加 Flask ML 服务的分体架构
- 作为 AI 推荐集成到电商业务的示例项目

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L11:  💡 AI-powered Smart Recommendations (Category-based, Similar Products, Price Range, Popular Items)
> L22:  AI/ML: Python Flask Recommendation System (Deployed on Render)
> L79: Fully extendable to integrate advanced ML models using the Python-based <code>ml-backend</code>.

## 星数曲线

```mermaid
xychart-beta
    title "alexworkdev/E-Commerce-Website 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `13f537e810fe` · [字段定义](../../DATASET.md)*
