# epam/statgpt-portal-frontend

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/epam/statgpt-portal-frontend) · [官网](https://statgpt.dialx.ai) · 组织维护

**构建 StatGPT 统计数据问答门户的前端代码库**

面向统计机构的 SDMX 驱动平台 StatGPT 的前端仓库：以 Nx 单仓组织，提供会话列表、聊天视图、DIAL API 客户端、SDMX API 客户端等可发布的 React 库，以及一个 Next.js 示例门户应用。应用含对话式界面，通过 DIAL API 以 SSE 流式接收 LLM 回复，支持查询、转换、可视化统计数据，并集成 NextAuth.js 认证与 Tailwind CSS 样式。运行需 Node.js ≥24.14.0 与 DIAL API 访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Nx monorepo 提供多个可发布 npm 库（@epam/statgpt-*）
- 对话界面经 DIAL API 以 Server-Sent Events 流式接收 LLM 回复
- SDMX API 客户端与数据转换工具库
- NextAuth.js 认证集成（可选）

## 适用场景

- 统计机构快速搭建自然语言查询统计数据的门户
- 复用会话管理与聊天界面组件构建自定义 AI 门户
- 通过链接或二维码分享数据问答会话

## 场景标签

`聊天机器人` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: This repository provides reusable libraries and an example application for building StatGPT Portals.
> L37: - **DIAL API** for LLM backend integration

## 星数曲线

```mermaid
xychart-beta
    title "epam/statgpt-portal-frontend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0c14b9884429` · [字段定义](../../DATASET.md)*
