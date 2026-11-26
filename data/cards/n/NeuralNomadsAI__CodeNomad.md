# NeuralNomadsAI/CodeNomad

⭐ 2,682 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/NeuralNomadsAI/CodeNomad) · [官网](https://neuralnomadsai.github.io/CodeNomad/) · 组织维护

**面向 OpenCode V2 的桌面/浏览器编程 Agent 工作台**

CodeNomad 是为 OpenCode V2 提供的桌面与浏览器工作区，面向跨项目、长会话和 Git worktree 工作的开发者。它连接 OpenCode 共享后台服务，提供项目多窗口标签、嵌套会话与全历史时间线导航、worktree 创建与变更审查、富文本会话（Markdown/diff/工具结果图）、文件引用与附件、密码认证的远程访问与 OpenTunnel 中继、MCP 连接与插件管理、语音输入，以及以 SideCar 形式嵌入 VSCode/终端等 Web 工具。依赖 OpenCode V2（≥2.4.0）与 Git。

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

- 桌面提供 Electron 与 Tauri 双构建，含 Windows 安装包与 macOS/Linux 包
- 嵌套会话、分叉对话、时间线全历史导航与 worktree 管理
- SideCar 机制可在应用内嵌入 VSCode（OpenVSCode Server）与 ttyd 终端
- 远程访问支持密码认证、HTTPS 与 OpenTunnel 中继配对

## 适用场景

- 在一个桌面工作区管理多个项目的 OpenCode 编程会话
- 用 Git worktree 隔离并行开发并就地审查变更
- 通过浏览器或手机远程接入开发机上的 Agent 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: CodeNomad is a **desktop and browser workspace for OpenCode V2** — built for developers who work across projects, lo
> L91: - **One shared OpenCode service** owns sessions and messages. Closing a CodeNomad tab, window, or backend leaves th
> L164: |**packages/server**|Core logic & CLI — workspaces, OpenCode proxy, API, auth, speech|

## 星数曲线

```mermaid
xychart-beta
    title "NeuralNomadsAI/CodeNomad 星数(近 13 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-26"]
    y-axis "stars" 2655 --> 2684
    line [2657, 2663, 2667, 2669, 2670, 2672, 2677, 2676, 2675, 2676, 2678, 2680, 2682]
```

2026-11-02 2,657 → 2026-11-26 2,682（+25）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `c2f2f12a2a33` · [字段定义](../../DATASET.md)*
