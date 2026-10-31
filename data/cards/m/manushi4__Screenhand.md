# manushi4/Screenhand

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-04-02 · [GitHub](https://github.com/manushi4/Screenhand) · [官网](https://screenhand.com) · 组织维护

**让 AI 客户端直接控制桌面与浏览器的开源 MCP 服务器**

面向 macOS 与 Windows 的 MCP 服务器（stdio 协议），供 Claude、Cursor、Codex CLI 等 MCP 客户端调用，共 111 个工具：通过原生 Accessibility API 点击/输入/读 UI 树（约 50ms、零额外 LLM 调用）、经 CDP 后台控制 Chrome（约 10ms）、OCR 感知、任务队列与多 agent 会话租约、以及从使用中学习并构建每应用空间蓝图（App Mastery Map）。内置 36 个应用的预置知识与 Claude Code 插件（13 技能/5 agent）。macOS 需授予终端 Accessibility 权限，Windows 构建 native 组件需 .NET 8 SDK，浏览器工具需 Chrome 开启远程调试端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 111 个工具：桌面控制/浏览器自动化/OCR/任务编排/感知规划
- 原生 Accessibility API 直接操作 UI，点击约 50ms 且零额外 LLM 调用
- Smart Fallbacks 自动在 Accessibility→CDP→OCR→坐标间降级
- 内置 37 参考 + 49 Playbook + 15 App Map 的预置平台知识
- 多 agent 会话租约与后台 worker 守护进程，任务可跨客户端重启存活

## 适用场景

- 让 Claude/Cursor 等客户端自动操作桌面应用完成表单填写、跨应用流程
- 后台无焦点地自动化 Chrome 页面操作与数据抓取
- 为 AI agent 提供带学习与恢复能力的长期桌面自动化能力

## 场景标签

`GUI 自动化` `浏览器自动化` `OCR` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Let AI control your desktop — click buttons, fill forms, automate workflows in ~50ms with zero extra AI calls.**
> L5: An open-source MCP server for macOS and Windows. Works with Claude, Cursor, Codex CLI, and any MCP-compatible client
> L73: ScreenHand is a standard MCP server over stdio. Run with `npx -y screenhand`.

## 星数曲线

```mermaid
xychart-beta
    title "manushi4/Screenhand 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7fd1a9df38cf` · [字段定义](../../DATASET.md)*
