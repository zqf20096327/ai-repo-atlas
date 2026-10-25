# rbc33/Ghostbar

⭐ 110 · Swift · 推送 2026-07-31 · [GitHub](https://github.com/rbc33/Ghostbar) · [官网](https://rbc33.github.io/Ghostbar/) · 个人维护

**macOS 菜单栏 AI 聊天客户端，屏幕共享/录制不可见**

用原生 Swift/AppKit 编写的 macOS 菜单栏 AI 聊天客户端，通过 NSWindow.sharingType = .none 将窗口从 macOS 捕获管线中排除，使 Zoom、Teams、Meet、OBS、QuickTime 等录屏与共享工具不可见。支持 Ollama、OpenAI、Anthropic、OpenRouter、NVIDIA NIM、LM Studio、llama.cpp 及任意 OpenAI 兼容后端；内置 whisper-cpp 端上语音转录与截图发给视觉模型的分析功能，无遥测。面向需要共享屏幕时使用 AI 的终端用户（如面试、会议场景）。未公证，首次启动需右键打开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NSWindow.sharingType = .none 使窗口对所有 macOS 捕获管线不可见
- 7 种后端：Ollama/OpenAI/Anthropic/OpenRouter/NVIDIA NIM/LM Studio/llama.cpp，及 OpenAI 兼容服务器
- whisper-cpp 全端上语音转录（tiny 到 medium 四档模型）
- 截图附到消息发给视觉模型，零遥测

## 适用场景

- 技术面试/系统设计面试中共享屏幕时获取 AI 提示
- 线上会议中实时总结与起草回应
- 配合 Ollama/LM Studio 做完全本地的私密推理

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L30: A macOS menu bar AI client that is **completely invisible to screen capture**.
> L75: |🤖 **Multi-backend**|Ollama, OpenAI, Claude, OpenRouter, NVIDIA NIM, LM Studio, llama.cpp|

## 星数曲线

```mermaid
xychart-beta
    title "rbc33/Ghostbar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-25 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `388246495e47` · [字段定义](../../DATASET.md)*
