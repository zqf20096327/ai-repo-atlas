# jackccrawford/reachy-mini-mcp

⭐ 29 · Python · MIT · 推送 2026-07-29 · [GitHub](https://github.com/jackccrawford/reachy-mini-mcp) · 个人维护

**让 AI 通过 MCP 控制 Reachy Mini 机器人的服务器**

面向 Pollen Robotics Reachy Mini 机器人的 MCP 服务器：向 Claude、GPT、Grok 等 MCP 兼容 AI 暴露 7 个工具（说话、聆听、拍照、表情、头部姿态、休眠、动作发现），实现语音对话、视觉采集与 12 种内置情绪表达、81 个预录动作。语音链路支持 xAI Grok Voice（设置 XAI_API_KEY 时自动启用）与 Deepgram（Aura 2 TTS / Nova-2 STT，listen 功能必需）。通过 Poetry 安装，需 Python 3.10+、reachy-mini SDK、MuJoCo 仿真器与 Deepgram API key，可连接真实硬件或仿真器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个 MCP 工具：speak/listen/snap/show/look/rest/discover
- 12 种内置情绪与 81 个 Pollen 预录动作，语音中可嵌入动作标记
- Grok Voice 与 Deepgram 双语音后端，自动切换
- 同一服务器支持真实硬件与 MuJoCo 仿真器

## 适用场景

- 让 Claude 等 MCP 兼容 AI 通过自然语言驱动机器人
- 为机器人构建能说话、聆听和表达情绪的具身 agent
- 无实体硬件时用 MuJoCo 仿真器先行开发

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: This MCP server lets AI systems control Pollen Robotics' Reachy Mini robot—speak, listen, see, and express emotions 
> L61: AI (Claude/GPT/Grok) → MCP Server → SDK → Daemon → Robot/Simulator

## 星数曲线

```mermaid
xychart-beta
    title "jackccrawford/reachy-mini-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2bed5b3b2691` · [字段定义](../../DATASET.md)*
