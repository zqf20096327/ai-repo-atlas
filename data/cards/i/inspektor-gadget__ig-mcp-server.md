# inspektor-gadget/ig-mcp-server

⭐ 28 · Go · Apache-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/inspektor-gadget/ig-mcp-server) · [官网](https://inspektor-gadget.io) · 组织维护

**把 Inspektor Gadget eBPF 内核遥测接入 LLM 的 MCP 服务器**

通过 Model Context Protocol 将 Inspektor Gadget 的 eBPF 内核级遥测（DNS、TCP、进程执行、文件活动、系统调用等）暴露为 MCP 工具，供 AI agent 在 IDE 或聊天界面中自主选择、运行 gadget 并基于内核证据做根因分析。每个 gadget 动态注册为独立 MCP 工具，支持前台/后台运行模式、字段级过滤、结构化 JSON 输出、只读模式与 -gadget-images 控制注册数量以节省上下文窗口。可本地二进制（stdio）、Docker 或部署到 Kubernetes 集群（HTTP）运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 gadget 动态注册为独立 MCP 工具，参数与字段描述自动生成
- 前台/后台两种运行模式与结构化 JSON 输出
- -read-only 模式限制为非破坏性操作
- -gadget-images 可指定少量 gadget 注册以节省 LLM 上下文窗口

## 适用场景

- 在 AI 聊天界面中排查 Kubernetes 的 DNS/TCP/OOM 等内核层问题
- 让 AI agent 关联多个 gadget 输出做数据驱动的根因分析
- 安全观测：监控进程执行与文件访问模式

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: The Inspektor Gadget MCP Server bridges Inspektor Gadget's low-level kernel observability with LLMs through the Mod
> L24: - **Dynamic tool registration** — Each gadget becomes its own MCP tool (e.g., `gadget_trace_dns`, `gadget_trace_tcp

## 星数曲线

```mermaid
xychart-beta
    title "inspektor-gadget/ig-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3ffd4e270aca` · [字段定义](../../DATASET.md)*
