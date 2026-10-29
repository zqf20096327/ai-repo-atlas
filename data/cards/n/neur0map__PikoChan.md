# neur0map/PikoChan

⭐ 23 · Swift · MIT · 推送 2026-03-12 · [GitHub](https://github.com/neur0map/PikoChan) · 个人维护

**驻留 macOS 刘海区的本地 AI 伙伴应用（Mac 用户）**

以 Swift/SwiftUI 原生编写的 macOS 桌面 AI 伙伴，常驻 MacBook 刘海区，以活动流聊天界面与用户互动。支持九种 LLM 提供商（含本地 Ollama 全离线运行，云端可选），具备 YAML 人格配置与心情系统、Snowflake Arctic Embed XS 语义记忆（CoreML）、语音输入输出、终端命令与浏览器自动化（三级审批）、Markdown 技能文件系统、正在播放音乐检测。人格/记忆/行为配置为可版本管理的 YAML 与 Markdown 文件。尚未实现本地 TTS/STT 与 MCP 客户端。需从源码用 Xcode 16 构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 九种 LLM 提供商接入，本地模型经 Ollama 全离线运行
- 人格/心情/记忆均为可编辑的 YAML 与 Markdown 配置
- 终端命令与浏览器自动化带三级审批（Deny/Allow/Always）
- Markdown 技能文件系统可扩展新能力

## 适用场景

- 在 Mac 刘海区常驻一个有性格的本地 AI 伙伴
- 对话与数据完全留在本机地使用 AI 助手功能
- 通过编辑 YAML/Markdown 定制伙伴的人格与技能

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An open-source AI companion that lives in your Mac's notch.
> L12: PikoChan is a macOS AI companion that sits inside the hardware notch on your MacBook. She has personality, opinions
> L14: Think of her as a desktop buddy who happens to be powered by a local language model. She can control your terminal,

## 星数曲线

```mermaid
xychart-beta
    title "neur0map/PikoChan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `de6c3580b2a2` · [字段定义](../../DATASET.md)*
