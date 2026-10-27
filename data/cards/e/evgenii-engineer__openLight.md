# evgenii-engineer/openLight

⭐ 39 · Go · MIT · 推送 2026-08-30 · [GitHub](https://github.com/evgenii-engineer/openLight) · 个人维护

**面向家庭实验室的轻量级基础设施 Agent，通过 Telegram 运维**

Go 编写的单二进制 Telegram 运维机器人：状态检查、日志查看、重启白名单内的 systemd/Docker 服务，支持多 SSH 节点、服务/CPU/端口/证书监控告警、SQLite 持久笔记与记忆，以及可选的本地语音转写（whisper.cpp+ffmpeg）。LLM 仅作可选的回退分类器，只能从已注册技能与白名单中选取；默认为无 LLM 的确定性模式，可搭配本地 Ollama 或远程 OpenAI 运行。提供安装脚本、Docker Compose 与树莓派/Mac mini 部署目标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性优先路由：斜杠命令与语义规则先于 LLM，LLM 仅作回退分类器且受白名单约束
- 单一 Go 二进制 + YAML 配置 + SQLite，无框架依赖
- 服务/CPU/端口/TLS 证书监控并在 Telegram 推送带操作按钮的告警
- 可选本地长期记忆：原文归档 + 本地 Qdrant RAG 索引 + 提炼记忆

## 适用场景

- 在 Telegram 里查看和重启自管服务器上的白名单服务
- 为家庭实验室设置 CPU、端口与 TLS 证书过期告警
- 通过语音留言远程下发运维指令并本地转写
- 在树莓派上部署本地 LLM 驱动（可选）的运维助手

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L35: before any LLM is consulted. When the LLM is enabled, it is a
> L61: For deterministic-only mode (no LLM at all), set `LLM_ENABLED=false` before
> L124: deterministic, no-LLM, no-extra-deps Telegram bot for safe service

## 星数曲线

```mermaid
xychart-beta
    title "evgenii-engineer/openLight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `285e0a0867a8` · [字段定义](../../DATASET.md)*
