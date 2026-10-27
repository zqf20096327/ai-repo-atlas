# Dyan-Dev/loopi

⭐ 197 · TypeScript · NOASSERTION · 推送 2026-06-09 · [GitHub](https://github.com/Dyan-Dev/loopi) · [官网](https://loopi.dyan.live/) · 个人维护

**本地运行的桌面自动化平台：可视化工作流+浏览器/光标键盘/命令行控制+AI agent**

基于 Electron 的开源桌面自动化平台：拖拽式节点编辑器编排多步骤工作流，能力覆盖真实 Chromium 浏览器操作、跨平台（Windows/macOS/Linux X11/Wayland）鼠标键盘控制、shell 命令执行与 80+ API 集成。AI 部分为目标驱动的 agent：可按计划运行工作流，运行后由反思引擎评估进度并改写工作流图。模型接入支持 OpenAI、Anthropic、Claude Code CLI 或 Ollama 本地运行。提供安装包（Windows .exe、Linux .deb）与源码构建两种方式，附 CLI 与 30+ 示例工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化节点编辑器构建多步骤自动化，30+ 示例工作流
- 真实浏览器控制 + 桌面鼠标键盘控制（含 Wayland via ydotool）+ shell 命令执行
- 目标驱动 agent：按计划运行、运行后反思并自动修补工作流
- 80+ 内置 API 集成，模型可选 OpenAI/Anthropic/Claude Code/Ollama（本地）

## 适用场景

- 把浏览器操作、桌面点击、命令行和服务 API 串成一条自动化流程
- 让 AI agent 定时运行并自我修正自动化工作流
- 用 Ollama 搭建不联网、不花钱的本地 AI 自动化流水线

## 场景标签

`工作流自动化` `GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L35: **AI Agents** — Goal-driven agents that run your workflows on a schedule, reflect on every run, and self-patch brok
> L39: **Visual Workflow Builder** — Drag-and-drop node editor. Build complex multi-step automations without writing code.
> L83: **Visual Workflow Builder** — Drag-and-drop node editor powered by ReactFlow. Build complex automations without wri

## 星数曲线

```mermaid
xychart-beta
    title "Dyan-Dev/loopi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-27 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `5c03d21ec2e1` · [字段定义](../../DATASET.md)*
