# CaptCanadaMan/pi-ollama

⭐ 12 · TypeScript · MIT · 推送 2026-09-25 · [GitHub](https://github.com/CaptCanadaMan/pi-ollama) · 个人维护

**为 pi 编码代理提供 Ollama 本地模型原生接入的扩展**

pi-ollama 是 pi coding agent 的 TypeScript 扩展，直接对接 Ollama 原生 /api/chat API 并自行构建请求，弥补 pi 内置 Ollama 路由（经 OpenAI 兼容端点）无法传递部分设置的问题。功能包括：每请求携带 num_ctx 上下文长度并可会话内修改、禁用 Ollama 静默截断历史并在溢出时让 pi 压缩重试、按模型控制的 thinking 级别、会话启动预热以缩短首轮响应、自动拉起本地 Ollama 进程、保留模型采样默认值、远程 Ollama 代理的 API key 支持，以及流式失败防护与 tok/s 遥测。提供 9 个 slash 命令与多个环境变量，需 Ollama 0.12.5+ 才能生效截断控制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- 每请求发送 num_ctx，上下文长度可控且与 pi 计数一致
- truncate: false 禁止 Ollama 静默丢弃历史，溢出时报错并触发 pi 压缩
- 会话预热使首轮响应从约 57 秒降至 3 秒（12B 模型实测）
- 9 个 slash 命令与 10 个环境变量用于配置与遥测

## 适用场景

- 在 pi 编码代理中使用 Ollama 本地模型并精确控制上下文窗口
- 本地/远程 Ollama 服务器的工具调用与流式调试
- 长时间会话中避免历史被静默截断导致模型失忆

## 场景标签

 · 领域:LLM 基础设施/编码代理

## 证据(README 行号)

> L3: Native Ollama provider extension for the pi coding agent.
> L5: pi-ollama connects pi to Ollama's native `/api/chat` API and builds every request itself. That's what the features b

## 星数曲线

```mermaid
xychart-beta
    title "CaptCanadaMan/pi-ollama 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-18 11 → 2026-10-25 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `c9f0b5940b4e` · [字段定义](../../DATASET.md)*
