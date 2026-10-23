# weibocom/rill-flow

⭐ 410 · Java · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/weibocom/rill-flow) · [官网](https://rill-flow.github.io) · 组织维护 · 中文 README

**面向分布式工作负载与 LLM 的流程编排引擎**

由微博团队开源的分布式工作流编排服务：以 DAG 方式编排与调度异构分布式系统任务，声称支持每天千万级任务执行、任务执行延迟低于 100ms；提供可视化流程编排界面与插件接入，支持云原生容器部署与云原生函数编排，并支持接入 LLM 模型服务。通过 git clone 源码后用 Docker-Compose 一键启动，默认部署 MySQL 等依赖服务，经 http://localhost 管理后台以 YAML 导入流程定义并提交执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DAG 工作流编排与分布式任务调度
- 可视化流程编排与插件式接入
- 支持接入 LLM 模型服务
- Docker-Compose 一键部署，自带管理后台

## 适用场景

- 编排与调度分布式系统中的批量任务
- 以可视化方式定义并执行 DAG 流程
- 将 LLM 服务作为流程节点接入任务编排

## 场景标签

 · 领域:后端/工作流编排基础设施

## 证据(README 行号)

> L13: - AIGC: supports rapid integration of LLM model services
> L7: Rill Flow is a high-performance, scalable distributed workflow orchestration service with the following core feature

## 星数曲线

```mermaid
xychart-beta
    title "weibocom/rill-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 409 --> 411
    line [410, 410]
```

2026-10-18 410 → 2026-10-23 410（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d9f69bae8312` · [字段定义](../../DATASET.md)*
