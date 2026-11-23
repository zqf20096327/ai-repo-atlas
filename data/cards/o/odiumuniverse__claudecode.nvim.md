# odiumuniverse/claudecode.nvim

⭐ 10 · Lua · MIT · 推送 2026-11-17 · [GitHub](https://github.com/odiumuniverse/claudecode.nvim) · [官网](https://home.odiumuniverse.com/p/claudecode-nvim) · 个人维护

**为 Neovim 用户提供带逐块审查的 Claude Code 集成插件**

一个 Neovim 插件，通过 WebSocket MCP 协议（与 Anthropic VS Code 扩展相同）将 Claude Code CLI 接入编辑器：Claude 可打开文件、读取选区与诊断、以 diff 形式呈现修改。在上游 coder/claudecode.nvim 基础上新增 hunk 级审查（逐块保留或回退）、Claude 权限模式支持、zen 全屏模式和账号切换。Claude 以未修改的 claude 二进制运行，使用用户自己的订阅登录；审查钩子仅对从 Neovim 启动的 Claude 生效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- hunk 级审查：对 Claude 的每处修改逐块保留/回退，支持行级选择
- 行内注释批量发送：多处修改下写备注，一条消息提交全部
- 四种权限模式（Manual/Accept edits/Plan 等）对应不同审查行为
- 被回退的修改会作为上下文反馈给 Claude，避免重复应用

## 适用场景

- 在 Neovim 中使用 Claude Code 并逐块控制其代码修改
- 让 Claude 重做某处修改而不用离开编辑器
- 同一项目多 Claude 会话协作时避免互相覆盖修改

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: The plugin connects the Claude Code CLI to Neovim over the same WebSocket MCP protocol that Anthropic's VS Code ext
> L15: - **Hunk review.** Keep or revert each change Claude makes, the way Cursor does, instead of accepting or rejecting 

## 星数曲线

```mermaid
xychart-beta
    title "odiumuniverse/claudecode.nvim 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `08f1c283b236` · [字段定义](../../DATASET.md)*
