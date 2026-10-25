# ribaunt/tekir

⭐ 45 · TypeScript · AGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/ribaunt/tekir) · [官网](https://tekir.co) · 个人维护

**隐私优先的开源网页/图片/新闻搜索引擎，内建 AI 助手**

基于 Next.js App Router + React 18 构建的搜索体验，覆盖网页、图片与新闻检索，主打不追踪、不收集个人数据。后端使用 Convex 实时存储用户、设置、会话与统计，采用 HttpOnly JWT 与 RBAC 鉴权；搜索 Provider 以 Brave 为主并支持降级回退，Dive 将 AI 回答与所选网页来源混合以提供可核验结果，内建 AI 助手 Karakulak 通过轻量 API 路由接入多个模型后端。注意：托管版 tekir.co 已宣布将于 2026 年 10 月 1 日停止服务，本仓库为其公开源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模态搜索（网页/图片/新闻）经统一 API 规范化，含请求去重与 10 分钟缓存
- 内建 AI 助手 Karakulak 接入多个模型后端，缓存/流式行为一致
- Brave 为主 Provider 并带降级回退策略
- Convex 实时后端 + HttpOnly JWT 自动刷新与 RBAC

## 适用场景

- 自部署一个不追踪用户的搜索引擎
- 在搜索结果旁获得带来源引用的 AI 回答
- 研究 Next.js + Convex 构建的搜索应用实现

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L12: Tekir is a fast, privacy‑first search experience that helps you find what you need across the web, images, and news
> L21: - Karakulak (the built‑in AI) integrates multiple model backends via lightweight API routes and consistent caching/

## 星数曲线

```mermaid
xychart-beta
    title "ribaunt/tekir 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5c9af282eb54` · [字段定义](../../DATASET.md)*
