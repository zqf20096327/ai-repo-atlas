# qingyu321/Little-Claude

⭐ 21 · HTML · Apache-2.0 · 推送 2026-08-25 · [GitHub](https://github.com/qingyu321/Little-Claude) · [官网](https://snowshadowdoll.online/) · 个人维护 · 中文 README

**Claude Code CLI 的桌面 GUI 客户端，含多会话与多供应商配置**

基于 Tauri 2 + React 19 的 Claude Code 非官方桌面客户端，通过 SDK 控制协议与 CLI 双向通信：权限请求、计划、提问渲染为结构化卡片。功能包括多会话标签页（独立进程并发）、文件浏览器与编辑器、基于 CLI 原生检查点的 Rewind 轮次回退、MCP 服务器管理、多 Provider API 配置（Anthropic / OpenAI 兼容格式，内置 DeepSeek、智谱 GLM、通义千问、Kimi、OpenRouter 等预设）、Claude Code / Codex / DeepSeek Harness 三引擎后端与跨 harness 交接、token 统计看板，以及视频分析、语音输入等扩展。以便携单 EXE 形式分发（Windows），数据存本地 JSONL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 SDK 控制协议将权限/计划/提问渲染为结构化卡片
- 多会话标签页独立进程并发，后台流式输出不丢失
- 多 Provider 配置：Anthropic / OpenAI 兼容格式 + 国内模型预设 + 代理
- 三引擎后端（Claude Code / Codex / DeepSeek Harness）支持会话跨引擎交接

## 适用场景

- 在桌面 GUI 中管理多个并发的 Claude Code 会话
- 用可视化卡片审批工具调用权限并按轮次回退
- 在同一客户端内切换不同 API 供应商与模型
- 查看本机全部会话的 token 用量统计

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Little Claude 是 Claude Code CLI 的原生桌面客户端，基于 **Tauri 2 + React 19 + TypeScript** 构建。它没有把终端输出简单地搬进一个窗口，而是通过 Claude Cod
> L41: - **协议级而非画面级** — 通过 `--permission-prompt-tool stdio` 与 CLI 双向通信：权限、计划、提问都以结构化数据进入界面，而不是从终端文本里"抠"状态

## 星数曲线

```mermaid
xychart-beta
    title "qingyu321/Little-Claude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `213ae8f02589` · [字段定义](../../DATASET.md)*
