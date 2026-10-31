# 1024XEngineer/anyclaw

⭐ 15 · Go · 推送 2026-05-13 · [GitHub](https://github.com/1024XEngineer/anyclaw) · 组织维护 · 中文 README

**本地优先的 AI Agent 工作台：CLI、网关与 Web 控制台**

用 Go 编写、React/Vite 前端的本地 AI Agent 工作台，提供 CLI 对话、网关服务与 Web 控制台三种使用方式。支持接入 OpenAI 兼容接口、OpenAI、Anthropic、Qwen、Ollama 等供应商，可调用文件读写、Shell、浏览器自动化、截图、OCR、桌面控制等工具，通过 Skill/Agent/Channel/CLI Hub 扩展能力，并可对接微信、飞书渠道。运行状态与工作区上下文默认保存在本地。安装需 Go 1.25+ 与 Node.js 20+，从源码克隆编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI、网关服务与 Web 控制台三种使用形态
- 支持文件、Shell、浏览器自动化、OCR、桌面控制等工具执行
- Skill / Agent / Channel / CLI Hub 扩展机制
- CLI Hub 可自动发现本地 Browser、ComfyUI、Blender 等可执行能力

## 适用场景

- 在本地搭建可控的 AI Agent 工作台执行真实任务
- 通过 Web 控制台管理模型、会话与工作区
- 把大模型与本地工具调用、外部渠道（微信/飞书）接在一起

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: AnyClaw 是一个面向真实任务执行的 AI Agent 系统。
> L19: - 接入多种大模型供应商
> L20: - 调用文件、Shell、浏览器、桌面自动化等工具

## 星数曲线

```mermaid
xychart-beta
    title "1024XEngineer/anyclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `65cfc80e266f` · [字段定义](../../DATASET.md)*
