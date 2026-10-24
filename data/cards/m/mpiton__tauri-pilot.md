# mpiton/tauri-pilot

⭐ 87 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/mpiton/tauri-pilot) · 个人维护

**面向 AI 代理的 Tauri v2 应用交互式测试 CLI**

由插件与 CLI 组成的 Tauri v2 应用测试工具：插件嵌入应用（仅 debug 构建）启动 Unix socket/Named Pipe 服务，CLI 通过 JSON-RPC 连接并向 WebView 注入 JS 桥，实现 DOM 检查与交互。提供 30 余个命令（snapshot/click/fill/assert/eval/截图/录放等），输出面向 LLM 消费优化，可运行 TOML 声明式场景并输出 JUnit 结果，另可作为 stdio MCP server 供 agent 调用。要求 Rust 1.95+、Tauri 2.12.1+（不支持 v1），支持 Linux/macOS/Windows 及 Android（ADB）、iOS 模拟器；已知限制包括物理 iOS 设备不可用、X11 下部分快捷键测试问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件+CLI 架构，通过 Unix socket/Named Pipe 以 JSON-RPC 通信
- 30+ 测试命令：无障碍树快照、交互、断言、网络/日志捕获、录放
- 可作为 stdio MCP server 运行，工具命名空间为 pilot.*
- 支持声明式 TOML 场景运行并输出 JUnit 报告

## 适用场景

- 让 AI 代理（如 Claude Code）实时检查和操作 Tauri 应用 UI
- 为 Tauri 应用编写端到端测试并在 CI 中运行
- 录制并回放应用交互会话

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: **Interactive testing CLI for Tauri v2 apps** — lets AI agents (Claude Code) and developers inspect, interact with,
> L133: ## For AI Agents
> L150: For agents with native MCP support, run tauri-pilot as a stdio MCP server instead

## 星数曲线

```mermaid
xychart-beta
    title "mpiton/tauri-pilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-24 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `9490e6c5c5e3` · [字段定义](../../DATASET.md)*
