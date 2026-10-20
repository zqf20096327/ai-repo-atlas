# triggerdotdev/trigger.dev

⭐ 16,580 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/triggerdotdev/trigger.dev) · [官网](https://trigger.dev/changelog) · 组织维护

**为开发者提供 TypeScript 平台构建部署持久化 AI 工作流**

开源的 TypeScript AI 工作流构建平台：以 SDK 形式在用户代码库中编写任务，部署后获得无超时的长运行任务、自动重试、队列与幂等、检查点与版本化，并附全量日志追踪的可观测面板。支持人审节点暂停、流式输出回传前端、批量触发与多环境管理；可使用云托管或通过 Docker Compose / Helm 自托管。任务运行时可运行浏览器、Python 脚本、FFmpeg 等系统包。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 1.0 天,年发版 100,145 位贡献者
- 涨星:近 1 天 **+11**(自 20261016 起算)

## 能力要点

- 长运行任务无超时，带自动重试、队列与幂等机制
- 人机协同节点：任务可暂停等待人工审批或反馈
- 实时运行订阅与 LLM 流式输出支持
- 提供 Docker Compose 与 Kubernetes Helm chart 自托管路径

## 适用场景

- 把需要长时间运行的 AI 代理任务从 serverless 平台迁移到无超时环境
- 在关键决策点加入人工审核的自动化工作流
- 为前端应用实时订阅任务进度和流式 AI 输出

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: Trigger.dev is the open-source platform for building AI workflows in TypeScript. Long-running tasks with retries, q
> L103: - Docker self-hosting guide - use Docker Compose to spin up a Trigger.dev instance

## 星数曲线

```mermaid
xychart-beta
    title "triggerdotdev/trigger.dev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 16561 --> 16581
    line [16562, 16580, 16580]
```

2026-10-18 16,562 → 2026-10-20 16,580（+18）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `684a54c08fd0` · [字段定义](../../DATASET.md)*
