# paulburgess1357/nvim-mcp

⭐ 66 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/paulburgess1357/nvim-mcp) · 个人维护

**连接 AI agent 与运行中 Neovim 会话的 MCP 服务器**

通过 Neovim 原生 msgpack-RPC socket 将 AI agent 接入正在运行的 Neovim 会话，无需安装 Neovim 插件。agent 可读取编辑器状态（缓冲区、窗口布局、诊断等）、内存中编辑缓冲区、执行 Vim 命令、发送按键、查询 LSP 诊断并添加高亮注释。支持自动发现多个运行实例，兼容 Cursor、Claude Code、Codex 等 MCP 客户端。通过 uv 或 Nix 运行，要求 Linux、Python ≥3.10、Neovim ≥0.11。

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

- 经 msgpack-RPC socket 接入运行中的 Neovim，无需插件
- agent 可编辑内存缓冲区（带完整撤销）、执行 Vim 命令、发送按键
- 查询 LSP 诊断、添加不改动缓冲区内容的高亮与虚拟文本
- 自动发现并连接多个 Neovim 实例

## 适用场景

- 让 Cursor/Claude Code 等 agent 直接操作我的 Neovim 会话
- 在编辑器内与 AI 结对编程并保持撤销历史
- 同时向多个 Neovim 实例分派 agent 任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: nvim-mcp MCP server
> L9: Works with Cursor, Claude Code, Codex, OpenCode, and any MCP-compatible client.

## 星数曲线

```mermaid
xychart-beta
    title "paulburgess1357/nvim-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-28 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `29b9ee2b76eb` · [字段定义](../../DATASET.md)*
