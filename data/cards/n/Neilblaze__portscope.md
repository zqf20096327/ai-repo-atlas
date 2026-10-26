# Neilblaze/portscope

⭐ 41 · JavaScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Neilblaze/portscope) · [官网](https://portscope.apps.neilblaze.live) · 个人维护

**查看与管理本机端口进程的 CLI，附自然语言 AI 助手**

面向开发者的端口观测 CLI：列出监听端口与进程详情（进程树、git 分支、内存），支持按端口/PID/范围 kill、pause/resume（POSIX 信号，macOS/Linux）、restart、查看日志、孤儿进程清理、实时 watch（含流量/带宽指标）与端口拓扑映射。本体是非 AI 的进程管理工具，AI 为附加功能：内置交互式 AI 聊天，支持多模态图片分析，可接入 Anthropic/OpenAI/Gemini/Ollama 等提供商；另可运行 MCP 服务器向 Claude Desktop、Cursor 等暴露 11 个工具。通过 npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端口/进程检查、kill、pause/resume、restart、日志查看与孤儿进程清理
- watch 模式实时展示内存、req/s、带宽等指标，支持 --fe/--be 等角色过滤
- AI 聊天支持自然语言管理端口与图片分析，可接 9 类提供商含本地 Ollama
- 可作为 MCP 服务器向 Claude Desktop、Cursor 等外部 agent 暴露 11 个工具

## 适用场景

- 排查哪个进程占用了端口并快速终止
- 本地开发时实时监控前后端服务与流量
- 让 AI 用自然语言诊断系统性能或执行端口操作

## 场景标签

 · 领域:开发者工具/系统观测

## 证据(README 行号)

> L15: Eliminate the operational friction of diagnosing port collisions and orphaned workloads. PortScope is an advanced C
> L216: PortScope's AI lets you manage ports with natural language — *"kill whatever's on 3000"*, *"show me what's using t

## 星数曲线

```mermaid
xychart-beta
    title "Neilblaze/portscope 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `62ed85eacfce` · [字段定义](../../DATASET.md)*
