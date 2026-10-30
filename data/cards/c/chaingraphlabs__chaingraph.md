# chaingraphlabs/chaingraph

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-01-06 · [GitHub](https://github.com/chaingraphlabs/chaingraph) · [官网](https://graphchain.gitbook.io/graphchain/) · 组织维护

**TypeScript 可视化流式编程框架：构建 AI agent 计算图**

源码可得的 flow-based 编程框架，面向用 TypeScript 构建 AI LLM agent、数据处理管道与协作自动化系统的开发者。提供类型安全端口系统（Zod/SuperJSON 运行时校验）、React+XYFlow 可视化流编辑器、支持断点与并发执行的后端引擎，及 tRPC/WebSocket 实时同步。存储默认内存式，可切换 PostgreSQL。通过 git clone + pnpm 安装，支持 Docker/docker-compose 部署。README 声明 API 不稳定、功能未完整、尚未达到生产可用状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 类型安全端口系统（Zod/SuperJSON 校验，含懒实例化与缓存）
- React+XYFlow 拖拽式可视化流编辑器
- 并发执行引擎，支持断点、step-over 与事件日志调试
- Docker/docker-compose 容器化部署，可选 PostgreSQL 持久化存储

## 适用场景

- 可视化设计与执行 AI agent 的工作流计算图
- 构建数据处理管道或协作自动化系统
- 通过流编辑器调试复杂节点图的执行过程

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L5: ChainGraph is a source-available, flow-based programming framework that empowers developers to visually design, exec
> L7: > **Disclaimer:** This version is intended for demonstration and experimentation purposes only. The API and internal

## 星数曲线

```mermaid
xychart-beta
    title "chaingraphlabs/chaingraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e3b19768a3a3` · [字段定义](../../DATASET.md)*
