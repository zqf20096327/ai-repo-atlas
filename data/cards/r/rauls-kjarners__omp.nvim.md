# rauls-kjarners/omp.nvim

⭐ 24 · Lua · MIT · 推送 2026-09-24 · [GitHub](https://github.com/rauls-kjarners/omp.nvim) · 个人维护

**Neovim 与 OMP 编码代理的上下文桥接插件**

连接 Neovim 与 Oh My Pi (OMP) 编码代理的集成插件：Lua 端挂接 BufEnter/CursorMoved/CursorHold 事件，通过 libuv Unix 套接字把当前文件路径、精确行号与可视选区广播给活跃的 OMP 终端会话；OMP 扩展端（TypeScript，运行于 Bun 引擎）建立套接字并将上下文注入提示词。需 Neovim >= 0.10.0 与 Oh My Pi >= 18.2.1，通过 omp plugin install 与 lazy.nvim 配置安装，提供 :checkhealth omp 验证命令。

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

- 向 OMP 会话同步活动文件路径、行号与可视选区
- 基于 libuv Unix 套接字的非阻塞通信
- OMP 扩展以 TypeScript 编写，运行于 Bun 引擎无需编译
- 提供 :checkhealth omp 集成验证命令

## 适用场景

- 在 Neovim 中使用 OMP 编码代理时自动同步编辑上下文
- 让 AI 代理获知当前浏览的文件与选中代码块
- 通过快捷键在侧面板唤起 OMP 终端会话

## 场景标签

 · 领域:开发工具/编辑器插件

## 证据(README 行号)

> L6: A seamless integration bridge between Neovim and the Oh My Pi (OMP) coding agent.
> L8: This plugin allows an active OMP terminal session to perfectly track your cursor, active file, and visual selections

## 星数曲线

```mermaid
xychart-beta
    title "rauls-kjarners/omp.nvim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `17e71f8103f6` · [字段定义](../../DATASET.md)*
