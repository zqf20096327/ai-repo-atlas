# zjyzhj/harness-system

⭐ 4 · TypeScript · MIT · 推送 2026-11-10 · [GitHub](https://github.com/zjyzhj/harness-system) · 个人维护 · 中文 README

**macOS 本地 AI 智能体指挥中心：统一管理多 bot 与 Coding CLI**

基于 Electron + Bun 的 macOS 菜单栏应用，把分散的 Coding CLI 与 API 中转收进统一界面：一句话创建 bot、主控面板统一对话（@ 点名、bot.ask 交接、群聊接力）、模型/记忆/技能/MCP 一处管理、每工程常驻 PTY 终端可切换 Claude Code / Cursor / Codex。另含 Live2D 桌宠娱乐侧车（可关）、Cloudflare 短链公网桥与 Webhook 的 Connect 层。数据默认只落本机，可整包导入导出；要求本机已配置可用的模型 API 或 CLI。

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

- 一句话创建 bot，主控面板统一指挥多 bot 协作
- 统一接入 OpenAI 兼容 API 与主流 Coding CLI（Claude Code / Cursor / Codex 可切）
- 工具循环、MCP、记忆、技能（SKILL.md）、定时例行任务
- Live2D 桌宠侧车与同意中心/审计日志/命令白名单安全机制

## 适用场景

- 把分散的 Coding CLI 和 API 配置收进一个菜单栏应用统一管理
- 让多个 bot 组队跑日报、产包/改包流水线
- 在 macOS 本地搭建不落云的智能体工作台

## 场景标签

`AI 助手` `多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: macOS 本地优先的 **AI 智能体指挥中心**：一句话创建 bot，主控统一对话；多 bot 可组队协作，统一接入 OpenAI 兼容 API 与主流 Coding CLI。
> L27: - **Coding 终端** — 每工程一块常驻 PTY；可切 Claude Code / Cursor / Codex，界面与 bot 同看一屏

## 星数曲线

```mermaid
xychart-beta
    title "zjyzhj/harness-system 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7e652376c25f` · [字段定义](../../DATASET.md)*
