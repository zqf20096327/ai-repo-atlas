# AuraVixStudio/caelo

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/AuraVixStudio/caelo) · [官网](https://auravixstudio.github.io/caelo/) · 组织维护

**面向消费者的多模型桌面客户端：Grok/Gemini/GPT 聊天、图像视频、语音与编程代理**

Electron + Python sidecar 架构的开源桌面应用，将 xAI Grok、Google Gemini/Vertex AI 与 OpenAI GPT 统一在一个客户端中：流式聊天（带实时网络/X 搜索与引用）、图像与视频生成编辑、语音（TTS/STT/对话/实时）、带沙箱文件工具与 diff 审批的 agentic 编程模块，以及 MCP 服务器、技能等扩展机制。采用自带密钥（BYOK）模式，密钥经操作系统加密存储，无遥测。提供 Windows/macOS(Apple Silicon)/Linux 安装包，也可从源码运行（Node.js ≥20 + Python 3.10+）。限制：不发布 Intel Mac 构建；Linux 包未签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接入 xAI/Google/OpenAI 三家 API，聊天、图像视频、语音、编程代理共用上下文与历史
- 自带密钥（BYOK），密钥经 OS 凭据设施加密，无遥测、无账号
- 编程代理：沙箱文件工具、diff 审批、4 种信任模式、检查点与子代理团队
- 扩展体系：MCP 服务器、slash 命令、hooks、技能、包市场与 headless CLI

## 适用场景

- 在一个桌面应用里使用 Grok/Gemini/GPT 的聊天、生图、语音等多种能力
- 用 agentic 编程模块在本地工作区执行带审批的文件与终端操作
- 自带 API 密钥、无遥测地使用多家模型服务

## 场景标签

`AI 助手` `编码 Agent` `图像生成` `视频生成` · 领域:编码与开发

## 证据(README 行号)

> L26: **Caelo** is an independent, open-source **desktop client for xAI Grok, Google Gemini / Vertex AI and OpenAI GPT**.
> L68: - **💬 Chat** — streaming multi-conversation chat with a per-conversation xAI/Google/OpenAI

## 星数曲线

```mermaid
xychart-beta
    title "AuraVixStudio/caelo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c08e45da6df5` · [字段定义](../../DATASET.md)*
