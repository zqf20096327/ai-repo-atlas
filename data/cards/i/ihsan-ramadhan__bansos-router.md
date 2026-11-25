# ihsan-ramadhan/bansos-router

⭐ 248 · TypeScript · GPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/ihsan-ramadhan/bansos-router) · [官网](https://ihsan-ramadhan.github.io/bansos-router/) · 个人维护

**本地守护进程：为编程工具免密钥路由免费编码模型**

运行于 127.0.0.1:17070 的本地守护进程，对外提供 OpenAI Chat Completions、Anthropic Messages、OpenAI Responses 三种协议端点，将 OpenCode Zen、KiloCode、LLM7、OVHcloud 等免费模型档接入各类编码工具。内置故障转移：模型返回 401/403/429/5xx 时进入冷却期，并按推理模式、消息格式能力与上下文窗口（不低于原 90%）在最多两个其他上游模型上重试。附带仪表盘、延迟探测、用量统计与严格安全模式；通过 npm 全局安装，需 Node ≥ 22.5，也提供 Docker 镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单端点同时支持 OpenAI Chat Completions、Anthropic Messages、OpenAI Responses 协议
- 故障转移按推理模式、消息格式能力与上下文窗口匹配备选模型
- 内置仪表盘展示模型目录、实时延迟与健康状态
- 严格模式：SSRF 防护、Host 校验、凭据脱敏，非回环绑定需显式开关

## 适用场景

- 为 claude-code、opencode、aider 等编码工具统一接入免费模型档
- 免注册免 API key 地在本地试用多种免费编码模型
- 通过故障转移与冷却机制应对免费档的限流与轮换

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: One daemon on `127.0.0.1:17070` that speaks OpenAI Chat Completions, Anthropic Messages and OpenAI Responses, so an
> L18: Free tiers rate-limit and rotate. A model that answers `401`/`403`/`429`/`5xx` is parked for a cooldown, and the re

## 星数曲线

```mermaid
xychart-beta
    title "ihsan-ramadhan/bansos-router 星数(近 19 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 141 --> 257
    line [150, 151, 153, 164, 178, 218, 225, 151, 237, 238, 240, 241, 243, 244, 247, 246, 247, 248, 248]
```

2026-10-23 150 → 2026-11-25 248（+98）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `fa8753e4a56a` · [字段定义](../../DATASET.md)*
