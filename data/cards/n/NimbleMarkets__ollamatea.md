# NimbleMarkets/ollamatea

⭐ 24 · Go · MIT · 推送 2026-04-20 · [GitHub](https://github.com/NimbleMarkets/ollamatea) · [官网](https://github.com/NimbleMarkets/ollamatea) · 组织维护

**Go/BubbleTea 终端 UI 组件库：在 TUI 中接入 Ollama LLM 服务**

面向 Go 开发者的 Bubble Tea 组件库，将 Ollama API 封装为终端 UI 组件：ollamaTea.Session 处理流式生成请求（每个 Session 对应一个 ollama run 会话）、EmbedSession 封装嵌入 API、ChatPanelModel 提供开箱即用的聊天面板、ModelChooser 选择模型。通过环境变量配置 Ollama 主机（默认 localhost:11434）与模型名。附带 ot- 系列示例 CLI 工具（图片描述、CSV 时序图生成、嵌入提取等），可从 releases 页下载或 Homebrew 安装。README 声明为实验性项目，功能仍在变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ollamaTea.Session 将 Ollama API 封装为 BubbleTea tea.Model，支持流式生成与取消
- EmbedSession 封装 Ollama Embed API
- ChatPanelModel 与 ModelChooser 开箱即用 TUI 组件
- 附 ot- 系列 CLI 工具（PNG 提问、CSV 时序图生成、嵌入提取等）

## 适用场景

- 在 Go TUI 应用中集成本地 Ollama 对话或嵌入能力
- 快速搭建基于终端的 LLM 聊天界面原型
- 将图表渲染为图片后交给多模态模型生成描述

## 场景标签

 · 领域:LLM 基础设施/终端 UI 组件

## 证据(README 行号)

> L14: `ollamatea` is a Bubble Tea Component for integrating terminal experiences with an Ollama LLM server. It offers a b
> L36: The main OllamaTea component is `ollamatea.Session`, which exposes the Ollama API using the BubbleTea framework. Th

## 星数曲线

```mermaid
xychart-beta
    title "NimbleMarkets/ollamatea 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4a02dc9cd093` · [字段定义](../../DATASET.md)*
