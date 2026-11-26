# Neizvestnyj/DockSight

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/Neizvestnyj/DockSight) · 个人维护

**本地 Web 界面：结合 LLM 诊断 Docker 容器、Compose 与 Swarm 故障**

DockSight 提供运行在本地的 Web 界面，面向使用 Docker 的开发者/运维人员。后端采集 Docker 状态、健康检查、日志、指标与 Compose 上下文，发送给模型，并校验返回的证据引用、生成关联证据的诊断卡片；重启/停止等动作需用户确认后执行。支持单 Docker 主机内追问并每轮重新采集观察。状态存于 SQLite，要求单后端进程；不支持持久监控历史与部署栈。通过安装脚本或源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 诊断卡片将模型解释链接到 Docker 观察证据，动作需确认
- 支持本地 Ollama 及 OpenAI/Anthropic/Gemini/兼容 API
- 采集容器状态、健康检查、日志、指标与 Compose 上下文
- 只读模型工具与带过期时间的动作 ID 由后端准备

## 适用场景

- 容器异常退出时结合日志与状态排查原因
- 诊断 Compose 项目或 Swarm 栈的故障
- 确认后执行容器重启/停止操作

## 场景标签

 · 领域:开发运维/Docker 诊断

## 证据(README 行号)

> L12: DockSight is a local web interface for diagnosing Docker containers, Compose projects, and Swarm stacks.
> L122: The backend collects Docker observations and sends them to the model. It validates the returned evidence reference


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `f0d436ab5c66` · [字段定义](../../DATASET.md)*
