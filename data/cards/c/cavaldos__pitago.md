# cavaldos/pitago

⭐ 30 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/cavaldos/pitago) · 个人维护

**pi 编码 agent 的终端 TUI 前端：聊天、会话与工具管理**

用 Go 与 Bubble Tea 构建的终端界面，作为 `pi` agent（以 `pi --mode rpc` 运行）的前端，通过 JSONL 通信。pi 后端提供多 provider 模型、工具、会话与上下文压缩，pitago 负责终端交互：命令面板（/model、/mcp、/tree、/theme 等）、快捷键、本地 shell 模式、消息复制、截图粘贴与只读附加到运行中的会话。安装提供 curl 脚本、Windows 可执行文件下载与源码构建，发布覆盖 linux/darwin/windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 JSONL RPC 与 `pi --mode rpc` 后端通信
- 内置 MCP server 管理器（添加/登录/重连/启停）
- 本地 shell 模式：命令独立于模型运行且保留 cwd 与变量
- 会话树、运行轨迹追踪与只读附加到运行中会话

## 适用场景

- 在终端里以图形化界面使用 pi 编码 agent
- 管理多个 LLM provider 登录与模型切换
- 边跑 agent 边在本地 shell 执行命令并保留上下文

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: _A polished Terminal User Interface (TUI) frontend for the `pi` agent, built with Bubble Tea. `pi --mode rpc` serve
> L67: Type `/` to open the command popup. Builtins are intercepted locally and re-implemented over

## 星数曲线

```mermaid
xychart-beta
    title "cavaldos/pitago 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `65538610cac3` · [字段定义](../../DATASET.md)*
