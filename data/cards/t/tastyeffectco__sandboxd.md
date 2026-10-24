# tastyeffectco/sandboxd

⭐ 971 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/tastyeffectco/sandboxd) · [官网](https://sandboxd.io/) · 组织维护

**自托管 AI 应用构建引擎：在隔离沙箱中由 agent 生成并运行应用**

用 Go 编写、基于 Docker 的自托管引擎：一次 HTTP 请求即启动隔离容器、在其中运行 AI 编码 agent（内置 OpenCode 与 Claude Code，API key 经代理注入不进沙箱），并为产物分配实时预览 URL；空闲沙箱可休眠唤醒。支持 80+ 策划的开源应用一键部署、自带 Web 控制台（纯 /v1 客户端）与完整 REST API。要求 Linux + Docker + Compose + git，一行脚本安装。Beta 0.x，容器隔离而非 VM，单服务器，API 认证默认关闭；另有付费的 Cloud 与托管服务，自托管引擎为 MIT 全功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一次请求生成隔离容器 + 运行编码 agent + 分配预览 URL
- 内置 OpenCode 与 Claude Code，凭证经代理注入、任务可检查点回滚
- 80+ 策划开源应用一键部署（Ghost/n8n/Grafana 等）
- API-first 设计，Web 控制台为纯 /v1 客户端，可完全无头运行

## 适用场景

- 在我自己的服务器上用 prompt 让 agent 构建 AI 应用并获得预览链接
- 为团队或多用户运营编码沙箱与预览环境
- 一键在自有服务器上部署 Ghost、n8n 等 80+ 开源应用
- 把沙箱生成能力通过 API 集成进自己的产品

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4:  Prompt it and a coding agent builds real apps in isolated sandboxes on your
> L55: 2. runs an **AI coding agent inside it** against your prompt, and
> L65: - **API-first** — everything is a `/v1` call, so you can build sandboxd into your

## 星数曲线

```mermaid
xychart-beta
    title "tastyeffectco/sandboxd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 970 --> 972
    line [971, 971]
```

2026-10-18 971 → 2026-10-24 971（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `d838fdf3187b` · [字段定义](../../DATASET.md)*
