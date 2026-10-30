# semos-labs/attyx

⭐ 245 · Zig · MIT · 推送 2026-08-11 · [GitHub](https://github.com/semos-labs/attyx) · [官网](https://attyx.sh) · 组织维护

**面向 AI agent 工作流的 GPU 加速终端模拟器**

用 Zig 编写的 GPU 渲染终端（Metal/OpenGL），单二进制小于 5 MB，内置 splits/tabs、守护进程支持的会话、命令面板、Kitty 图像协议等终端基础功能。面向运行多个 AI agent 的用户：通过 JSON 生命周期钩子和事件总线插件读取 Claude/Codex/opencode 的 agent 状态并在面板上显示彩色指示点；通过 Unix socket IPC、attyx CLI 和 MCP（stdio 桥与内嵌 loopback HTTP 服务器）暴露终端表面，使一个 agent 能创建、观察和驱动其他 agent 的面板。macOS/Linux 经 Homebrew 安装或 Zig 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跟踪 Claude/Codex/opencode 的 agent 生命周期并以彩色状态点显示
- 通过 Unix socket IPC、attyx CLI 与 MCP（stdio + loopback HTTP）暴露面板/标签/按键/输出等操作
- 会话由守护进程支持，关窗重开后面板保持
- 单二进制小于 5 MB，TOML 配置支持热重载

## 适用场景

- 同时监控多个 AI agent 的运行状态并在终端内切换
- 让一个 agent 通过 MCP 驱动其他 agent 所在的面板
- 替代 tmux+插件组合作为日常 GPU 渲染终端

## 场景标签

 · 领域:终端/开发者工具

## 证据(README 行号)

> L27: **Attyx is a GPU-accelerated terminal built for the agentic era.** It's agent-aware end to end: it tracks agent lif
> L33: Attyx reads each agent's lifecycle — Claude and Codex via JSON lifecycle hooks, opencode via an event-bus plugin — 
> L52: It speaks **MCP**, too: `attyx mcp` is a stdio bridge for every platform, and an embedded loopback HTTP MCP server 

## 星数曲线

```mermaid
xychart-beta
    title "semos-labs/attyx 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 243 --> 246
    line [244, 245, 245]
```

2026-10-18 244 → 2026-10-30 245（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c35ffde83e69` · [字段定义](../../DATASET.md)*
