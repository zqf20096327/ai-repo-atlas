# praveen-ks-2001/hermes-agent-template

⭐ 323 · Python · 推送 2026-10-21 · [GitHub](https://github.com/praveen-ks-2001/hermes-agent-template) · [官网](https://railway.com/deploy/hermes-agent-ai?referralCode=QXdhdr) · 个人维护

**在 Railway 一键部署 Hermes Agent 并通过 Web 管理面板运维**

面向 Hermes Agent（Nous Research 的自主 AI agent）的一键 Railway 部署模板：单容器内以 Starlette+Uvicorn 前端进程代理原生 Hermes 面板与管理网关子进程，提供设置向导（LLM 提供商/频道/工具勾选配置，无需改配置文件）、网关启停与崩溃自动重启、配对审批、备份恢复与实时日志。支持 25+ 提供商下拉选择、7 种消息频道、多种工具集成，配置存于 /data 卷以跨重部署持久化。也可通过 Docker 本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web 设置向导配置提供商/频道/工具，无需编辑配置文件
- 网关监管：崩溃/OOM 后自动退避重启，日志环形缓冲流式查看
- 备份恢复：Hermes-home 数据打包下载（6 小时内有效，未加密），恢复前自动安全快照
- 单 cookie 登录同时守卫设置向导与代理的 Hermes 原生面板

## 适用场景

- 在 Railway 上一键部署自己的 Telegram/Discord AI 机器人
- 通过浏览器管理 Hermes 网关状态、日志与用户配对
- 无需命令行即可配置 LLM 提供商并升级 Hermes 版本

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Deploy Hermes Agent on Railway with a web-based admin dashboard for configuration, gateway management, and user pair
> L7: > Hermes Agent is an autonomous AI agent by Nous Research that lives on your server, connects to your messaging chan
> L95: One container runs a single public process that fronts two managed Hermes subprocesses:

## 星数曲线

```mermaid
xychart-beta
    title "praveen-ks-2001/hermes-agent-template 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-27"]
    y-axis "stars" 321 --> 325
    line [322, 324, 323, 323]
```

2026-10-18 322 → 2026-10-27 323（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ddbef078bbd7` · [字段定义](../../DATASET.md)*
