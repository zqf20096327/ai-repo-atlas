# Jaxton07/percho

⭐ 454 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Jaxton07/percho) · [官网](https://www.percho.org/) · 个人维护 · 中文 README

**Pi 编码代理的桌面 GUI 客户端：多会话与可视化工具审批**

基于 Electron 的桌面应用，在主进程中内嵌官方 Pi SDK（@earendil-works/pi-coding-agent），运行与 Pi CLI 相同的引擎而非分支重实现。面向偏好 GUI 的 Pi CLI 用户，提供多会话聊天、逐次工具调用的可视化审批（每工具规则引擎）、内置子代理与并行任务分发、UI 插件与自定义主题、上下文蒸发以控制长会话预算；支持订阅登录（Claude Pro/Max、ChatGPT Codex、GitHub Copilot）与多家 API key，共享 ~/.pi/agent/ 配置目录。跨 macOS/Windows/Linux 提供预构建安装包。

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

- 内嵌官方 Pi SDK，与 Pi CLI 共享配置与会话
- 可视化工具调用审批，基于每工具规则引擎
- 内置子代理与并行任务分发、只读子会话检查
- UI 插件、桌面宠物、自定义背景与主题；手机浏览器远程监控会话

## 适用场景

- 用图形界面替代终端使用 Pi 编码代理
- 在 GUI 中逐条审批代理的工具调用
- 在终端与 GUI 之间无缝继续同一会话
- 通过手机浏览器远程查看并干预代理会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  Highly customizable desktop GUI for the Pi coding agent — the same engine as the Pi CLI, in a clean visual interfac
> L37: Percho embeds the official Pi SDK (`@earendil-works/pi-coding-agent`) in the Electron main process. It is **not a f

## 星数曲线

```mermaid
xychart-beta
    title "Jaxton07/percho 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 437 --> 455
    line [438, 452, 454]
```

2026-10-18 438 → 2026-10-22 454（+16）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c8409c7712da` · [字段定义](../../DATASET.md)*
