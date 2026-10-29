# Jiansen/clawsquire

⭐ 19 · TypeScript · MIT · 推送 2026-03-30 · [GitHub](https://github.com/Jiansen/clawsquire) · [官网](https://clawsquire.com) · 个人维护

**OpenClaw 的桌面 GUI 伴侣应用，内嵌 AI 修复助手**

基于 Tauri 2（Rust 后端 + React 19 前端）的跨平台桌面应用，为 OpenClaw 提供图形化安装向导（20+ 渠道模板）、可视化健康检查、版本化配置备份与回滚、状态仪表盘、安全预设和系统托盘。AI 功能包括：安装/操作失败时 LLM Agent 诊断错误并生成带风险等级的跨平台修复命令，以及健康检查、配置、VPS、帮助页面的上下文 AI 问答，通过 Anthropic/OpenAI/Google/DeepSeek 直连 API 独立于 OpenClaw 运行。提供 7 种语言界面与 macOS/Windows/Linux 安装包，macOS 版未签名需手动移除隔离属性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 安装/操作失败时 LLM Agent 生成带风险等级的跨平台修复命令
- 直连 Anthropic/OpenAI/Google/DeepSeek API，AI 功能不依赖 OpenClaw
- 版本化配置快照、差异对比与一键回滚
- macOS/Windows/Linux 三平台安装包，7 种语言界面

## 适用场景

- 不想用命令行，通过图形界面安装和管理 OpenClaw
- 出问题时让 AI Agent 诊断并指导修复
- 在健康检查、配置、VPS 管理页面获得内嵌 AI 问答

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: **The AI-powered companion app for OpenClaw** — when things go wrong, your squire's AI agent diagnoses the problem 
> L30: - **Health Check** — Visual diagnostics, friendlier than `openclaw doctor`

## 星数曲线

```mermaid
xychart-beta
    title "Jiansen/clawsquire 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `cf62ee3c928b` · [字段定义](../../DATASET.md)*
