# goccy/sheena

⭐ 44 · Go · MIT · 推送 2026-09-10 · [GitHub](https://github.com/goccy/sheena) · 组织维护

**Go 进程内沙箱库：安全执行 AI agent 请求的工具调用**

面向 Go 开发者的 AI agent 工具调用沙箱库：将 agent 的 bash 调用运行在隔离的内存文件系统上，命令全部为 Go 重实现、按允许清单分发，不触碰宿主进程与 PATH。另提供同受约束的 python3/js 解释器，网络默认拒绝并带 SSRF 防护，超时、内存、输出量等限额可配置。工具 API 采用 SDK 中立的 {name, description, input_schema} 形态，可直接接入 anthropic-sdk-go、openai-go、microsoft/agent-framework-go。限制：不是运行不可信原生代码的边界。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- bash 命令为 Go 重实现，按允许清单分发，不运行宿主二进制
- python3/js 解释器纯 Go 无 cgo，进程内运行且有强制内存上限
- 网络默认拒绝，含 SSRF 私有地址防护、跨主机重定向阻断与响应体上限
- 文件系统、网络、资源访问统一经 Policy 配置，文件系统默认内存态、宿主挂载由 os.Root 约束

## 适用场景

- 让 AI agent 的 bash 工具调用在隔离沙箱中执行，避免触碰宿主环境
- 为 agent 提供受限的代码解释器（Python/JS）工具
- 通过统一的工具 API 将沙箱接入任意 Go AI SDK 的工具调用循环

## 场景标签

 · 领域:AI 基础设施/安全

## 证据(README 行号)

> L5: **A lightweight, in-process sandbox for safely executing the tool calls an AI
> L10: Sheena runs an agent's `bash` tool calls against an isolated, in-memory
> L45: - **Adapter-free tool API.** `Sandbox.Tools()` + `Sandbox.CallTool()` speak the

## 星数曲线

```mermaid
xychart-beta
    title "goccy/sheena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `18dd3409fe88` · [字段定义](../../DATASET.md)*
