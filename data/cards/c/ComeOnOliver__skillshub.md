# ComeOnOliver/skillshub

⭐ 64 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/ComeOnOliver/skillshub) · [官网](https://skillshub.wtf) · 个人维护 · 中文 README

**面向 AI agent 的技能注册与检索 API 服务（10,000+ 技能）**

AI agent 技能（SKILL.md）开放注册平台：聚合来自 Microsoft、OpenAI、Trail of Bits、HashiCorp 等 230+ 仓库的 10,000+ 技能，提供无需鉴权的 REST API——自然语言任务描述经 resolve 端点返回最佳匹配技能（BM25/IDF 加权排序），可按 format=md 拉取原始技能内容；注册 API key 后可发布、star 与管理技能。本体为 Next.js + PostgreSQL/Drizzle 的开源 Web 服务，本地运行需 Node.js 20+、pnpm 与 Docker（Postgres），仅 DATABASE_URL 为必需环境变量；读接口限流 60 次/分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10,000+ 技能来自 230+ 仓库，含 anthropics/skills 等源
- resolve 端点按自然语言任务返回最佳匹配技能
- 搜索/解析/拉取均无需注册或 API key
- 支持 agent 注册获得 API key 后发布/更新/删除技能

## 适用场景

- AI agent 在运行时按任务描述一次性获取适配技能
- 浏览或按 tag/stars 检索可用 agent 技能
- 开发者通过 PR 或 API 发布自建技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: **🔗 skillshub.wtf** — 10,000+ skills from 230+ repos (Microsoft, OpenAI, Trail of Bits, HashiCorp, Sentry, and more
> L389: |📦 **10,000+ Skills**|From Microsoft, OpenAI, Trail of Bits, HashiCorp, Sentry, Snyk, and 230+ repos|
> L390: |🤖 **Agent-First API**|No auth needed to search, resolve, or fetch skills. Built for programmatic use|

## 星数曲线

```mermaid
xychart-beta
    title "ComeOnOliver/skillshub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-30 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `21622482fae3` · [字段定义](../../DATASET.md)*
