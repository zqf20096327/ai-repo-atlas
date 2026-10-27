# IAIAYN/AmaiGirl

⭐ 24 · C++ · Apache-2.0 · 推送 2026-04-16 · [GitHub](https://github.com/IAIAYN/AmaiGirl) · 个人维护 · 中文 README

**跨平台原生 AI 桌面助手：Live2D 角色陪伴与 OpenAI 兼容对话/TTS**

以 C++20/Qt6/OpenGL 构建的原生桌面助手，提供无边框常驻窗口、托盘控制、Live2D 模型渲染与鼠标交互（移动/切姿势/缩放）。AI 部分：兼容 OpenAI 风格 Chat Completions 接口的对话（支持流式输出与人设系统提示词）与 OpenAI 风格 TTS 语音播报，API 地址/密钥/模型均由用户配置。支持中英文界面与多模型切换，当前可运行于 macOS 13.0+、Windows 10/11（x86_64）与 Linux（x86_64，Wayland），开发与构建细节拆分至 CONTRIBUTING.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Live2D 模型加载、姿态/表情切换与鼠标交互
- 兼容 OpenAI 风格 Chat Completions 与 TTS 接口，支持流式输出
- 多平台原生构建：macOS 13.0+/Windows 10/11/Linux（Wayland）
- 中英文界面与模型切换、聊天上下文随模型加载

## 适用场景

- 在桌面常驻一个可对话、可语音播报的 Live2D 陪伴角色
- 接入自选的 OpenAI 兼容对话与 TTS 服务
- 在多个 Live2D 模型间切换并保留各自聊天上下文

## 场景标签

`AI 助手` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L89: - **AI 对话能力**：兼容 OpenAI 风格 Chat Completions 接口
> L90: - **TTS 语音能力**：兼容 OpenAI 风格 TTS 接口，可语音播报回复

## 星数曲线

```mermaid
xychart-beta
    title "IAIAYN/AmaiGirl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `43b580f98954` · [字段定义](../../DATASET.md)*
