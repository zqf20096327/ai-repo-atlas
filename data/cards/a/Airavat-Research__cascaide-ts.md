# Airavat-Research/cascaide-ts

⭐ 18 · TypeScript · MIT · 推送 2026-05-27 · [GitHub](https://github.com/Airavat-Research/cascaide-ts) · [官网](https://www.cascaide-ts.com) · 个人维护

**TypeScript 全栈 agent 运行时与编排框架，跨 JS 运行时部署**

用 TypeScript 编写的全栈 agent 运行时与 AI 编排框架，本质为分布式、可观测、持久化的图执行器，可在任意 JS/TS 运行环境中运行，覆盖 Web 应用与无头/CLI agent 工作流。通过 create-cascaide-app CLI 生成含 3 个 agent 的全栈应用模板，v0.5.0 提供 Next.js、React+Express、Hono、Fastify 适配器。分持久化完整版（需 Postgres）与非持久化 Lite 版两种模式，核心 gzip 后 23kb。

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

- 图执行器架构，UI 建模为 agent 图节点
- 无需托管运行时，可部署在任意 JS/TS 环境
- 持久化完整版需 Postgres，另有非持久化 Lite 模式
- 开箱提供调试与 timetravel，agent 轨迹存于自有数据库

## 适用场景

- 构建带多 agent 协作的全栈 AI 应用
- 在 Next.js/React+Express/Hono/Fastify 项目中嵌入 agent 工作流
- 开发需要持久化与审计轨迹的商业级 agent 后端

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Fullstack agent runtime and AI orchestration framework in typescript designed to run anywhere JS/TS can. It was orig
> L7: What it really is is a distributed, observable, durable graph executor. The first split just happens to be client/se

## 星数曲线

```mermaid
xychart-beta
    title "Airavat-Research/cascaide-ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `76a2ca4563ea` · [字段定义](../../DATASET.md)*
