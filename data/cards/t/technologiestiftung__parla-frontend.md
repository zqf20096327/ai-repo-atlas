# technologiestiftung/parla-frontend

⭐ 16 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/technologiestiftung/parla-frontend) · [官网](https://www.parla.berlin/) · 组织维护

**柏林州议会公文 RAG 问答系统的前端应用**

Parla 项目的前端，基于 Next.js 构建并部署于 Vercel。Parla 整体面向公共行政文档检索：将议会文档（PARDOK 中超过 11,000 份）做嵌入与向量相似度检索，通过 RAG 生成回答并附带来源文档引用。本前端需配合 parla-api 后端实例与已填充的数据库（用 parla-document-processor 处理文档）运行，需 Vercel 与 Supabase 账号；项目自称原型，仍在缓解 AI 不准确问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于向量相似度检索的 RAG 文档问答前端
- 回答附带来源文档引用
- 基于 Supabase 社区示例，用 Next.js 构建
- 支持可选的 Matomo 统计

## 适用场景

- 检索柏林州议会书面质询与委员会程序文档
- 在政府公开数据上做带引用的 AI 问答
- 公共行政场景下原型验证 RAG 应用

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: Parla operates by scanning through a wide array of public documents available on the parliamentary documentation sy
> L29: This is the frontend for the project _Parla_. Currently we explore if we can make the parliamentary documentation p

## 星数曲线

```mermaid
xychart-beta
    title "technologiestiftung/parla-frontend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ec09da7c781e` · [字段定义](../../DATASET.md)*
