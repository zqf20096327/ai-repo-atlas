# themanyone/whisper_dictation

⭐ 294 · Python · GPL-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/themanyone/whisper_dictation) · 个人维护

**本地语音键盘与语音控制助手，含 AI 聊天与画图**

面向个人用户的本地语音助手应用：以 whisper.cpp 做语音转文字充当语音键盘，llama.cpp 运行本地 LLM 回答问题，支持语音控制摄像头、录音、启动应用（pyautogui）、调用 stable-diffusion-webui 画图，可选接入 ChatGPT/Gemini，用 mimic3 朗读回答。支持 X11 与 Wayland，客户端-服务器架构可在局域网多机部署。安装需自行编译 whisper.cpp 与 llama.cpp，并配置 GStreamer、CUDA 等系统依赖，最低约 4GiB VRAM（也可 CPU 运行）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- whisper.cpp 语音键盘 + llama.cpp 本地 LLM 聊天
- 语音命令控制摄像头、录音、应用启动与网页搜索
- X11/Wayland 双支持（evdev/PyAutoGUI 自动切换）
- mimic3 语音合成，可跨局域网设备朗读

## 适用场景

- 用语音代替键盘进行听写输入
- 离线环境下用语音向本地 AI 提问并获得语音回答
- 免手操作控制电脑：拍照、录音、开终端、搜索网页

## 场景标签

 · 领域:语音交互/桌面助手

## 证据(README 行号)

> L3: Private voice keyboard, AI chat, images, webcam, recordings, voice control in >= 4 GiB of VRAM. "The works" all AI f
> L10: - Voice keyboard depends on `whisper.cpp`Whisper.cpp
> L11: - LLM inference depends on Llama.cpp

## 星数曲线

```mermaid
xychart-beta
    title "themanyone/whisper_dictation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 293 --> 295
    line [294, 294]
```

2026-10-18 294 → 2026-10-22 294（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `e56cc27555ef` · [字段定义](../../DATASET.md)*
