# yuluyangguang1/hermes-portable

⭐ 62 · HTML · MIT · 推送 2026-09-16 · [GitHub](https://github.com/yuluyangguang1/hermes-portable) · 个人维护 · 中文 README

**Hermes Agent 便携打包：解压到 U 盘即用的零安装运行环境**

为 Hermes Agent 制作的便携发行包：将 Python 3.12、Node.js 24、Hermes Agent 与 hermes-web-ui 打包进单一目录，解压即可运行，数据存于包内 data/ 目录、与宿主 ~/.hermes 隔离。提供终端 CLI（默认）、Web UI(:8648) 与可选 Electron 桌面版三种模式，并内置常驻配置中心(:17520)，管理 74+ LLM 提供商的 API Key、模型与消息渠道。覆盖 macOS(arm64/x64)、Windows(x64，CI 偶发故障可能延迟发布)与 Linux(自行构建)。

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

- 零安装单目录打包：Python 3.12、Node.js 24、Hermes Agent、hermes-web-ui 均内置
- 配置中心 Web 界面(:17520)管理 74+ LLM 提供商的 API Key/模型/渠道
- 三种使用模式：终端 CLI、Web UI(:8648)、可选 Electron 桌面版
- 数据隔离：配置、会话、历史全存包内 data/，不污染宿主环境

## 适用场景

- 在 U 盘或公共电脑上免安装运行 Hermes Agent
- 多台机器间整体迁移 Agent 配置与会话数据
- 通过 Web 界面统一管理多家 LLM 提供商的 API Key 与模型切换

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: - 🚀 **零安装** — 解压即用，所有依赖（Python 3.12、Node.js 24、Hermes Agent、hermes-web-ui）已打包
> L69: - ✅ **74+ LLM 提供商**：OpenRouter、Anthropic、OpenAI、DeepSeek、Google Gemini、xAI Grok、智谱 GLM、通义千问、Kimi、豆包、MiniMax、Mistral

## 星数曲线

```mermaid
xychart-beta
    title "yuluyangguang1/hermes-portable 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 59 --> 63
    line [60, 61, 62, 62]
```

2026-10-18 60 → 2026-10-24 62（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `943ae5e60a71` · [字段定义](../../DATASET.md)*
