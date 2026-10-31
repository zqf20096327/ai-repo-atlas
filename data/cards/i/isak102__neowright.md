# isak102/neowright

⭐ 14 · Rust · GPL-3.0 · 推送 2026-06-18 · [GitHub](https://github.com/isak102/neowright) · 个人维护

**让编码 Agent 驱动真实 Neovim 会话的 CLI 调试工具**

Rust 编写的 CLI 工具，供编码 agent 在真实 Neovim TUI 会话中调试配置与复现 UI 行为：可打开带用户真实配置的 Neovim、按键映射、执行命令、eval Lua、等待异步状态、捕获终端网格快照，并在 PTY 阻塞时提供 PTY 逃逸通道。附带 agent skill 教导 agent 何时及如何使用 CLI。主要用户是 agent 而非人类；通过 GitHub Releases 安装脚本或 Cargo 安装，快照产物写入项目 .neowright/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 驱动真实 Neovim 配置会话：keys/exec/eval/wait/snapshot 命令面
- RPC 默认按键通道 + PTY 字节直写逃逸通道
- 终端网格文本快照，产物写入 .neowright/
- 附带可全局或项目级安装的 agent skill

## 适用场景

- 插件更新后让 agent 复现并修复 Neovim UI 问题
- agent 在真实配置中检查浮动窗口、补全菜单、映射等交互状态
- 演示或人工调试时附加可见的远程 headed UI

## 场景标签

 · 领域:开发工具/编辑器自动化

## 证据(README 行号)

> L3: `neowright` is a CLI tool for agents to interact with a real Neovim TUI session. Think Playwright CLI, but for Neovi
> L7: This is mostly not a human-facing tool. Humans can run it, but the primary user is an agent that needs a reliable wa

## 星数曲线

```mermaid
xychart-beta
    title "isak102/neowright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7e7b288d2391` · [字段定义](../../DATASET.md)*
