# Eric-Song-Nop/mobvibe

⭐ 145 · TypeScript · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/Eric-Song-Nop/mobvibe) · [官网](https://app.mobvibe.net) · 个人维护 · 中文 README

**远程连接本地 AI 编程代理的跨设备 ACP WebUI**

分布式 Agent Client Protocol（ACP）WebUI，通过 CLI 守护进程连接本机已安装的 ACP 兼容编程代理（Claude Code、OpenCode、Gemini CLI 等 20+ 种），实现桌面与移动端的多会话聊天、实时流式输出、文件浏览（Tree-sitter 大纲）、@提及与 Git 变更预览。会话内容在 CLI 端加密、WebUI 端解密，网关只转发加密事件。安装仅需 npx 两条命令，浏览器打开 app.mobvibe.net 使用；支持基于 render.yaml 自托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动扫描系统检测 20+ 种 ACP 兼容代理并管理其生命周期
- CLI 端到端加密：网关仅路由加密事件，无法读取会话内容
- Tauri v2 单代码库覆盖 Web/桌面/移动端
- 会话级文件浏览器、Tree-sitter 代码大纲与 @提及注入上下文

## 适用场景

- 在手机或其他设备上继续操控本机运行的编程代理
- 同时管理多个 AI 编程代理的多会话对话
- 无需反向代理配置即可远程访问本地代理会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L17: Mobvibe is a distributed ACP (Agent Client Protocol) WebUI for local agent workflows. It connects to ACP-compatible
> L193: - **CLI Daemon** — Bun-based local process that manages ACP agent lifecycles

## 星数曲线

```mermaid
xychart-beta
    title "Eric-Song-Nop/mobvibe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 143 --> 146
    line [144, 145, 145]
```

2026-10-18 144 → 2026-10-28 145（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6652031a236c` · [字段定义](../../DATASET.md)*
