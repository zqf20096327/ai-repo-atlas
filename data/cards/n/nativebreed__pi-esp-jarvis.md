# nativebreed/pi-esp-jarvis

⭐ 4 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/nativebreed/pi-esp-jarvis) · [官网](https://mothcloud.com/build-your-own-ai-voice-assistant-with-a-raspberry-pi-a-tiny-esp32-screen-and-claude/) · 个人维护

**在树莓派 5 与 ESP32 屏上自建语音助手**

由 Raspberry Pi 5、Waveshare ESP32-S3 触摸屏与 AI 模型组成的语音助手搭建项目：屏幕端芯片监听唤醒词 "Jarvis" 并经 Wi-Fi 流式传输语音，Pi 端用 Whisper 转文字，路由器按请求分配给免 AI 的技能（计时/清单/天气/音乐/Pi 控制）、本地 Llama 3.2 3B 或 Claude（联网搜索），再由 Piper 合成语音播报，屏幕显示动画脸 Visor。板端运行 xiaozhi-esp32 开源固件并指向本地 Pi。两个脚本完成安装，无需编码；可选 USB 摄像头由 Claude 描述画面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Llama 3.2 3B 回答日常问题，无 API key 时全部本地运行
- 路由机制在技能/本地模型/Claude 间分配请求
- Whisper 语音识别 + Piper 语音合成 + ESP32 端唤醒词
- 手势交互：双击说话、翻面暂停、摇动停止

## 适用场景

- 在桌面搭建一个私有语音助手
- 用语音管理计时器、闹钟、清单和记忆
- 通过语音控制树莓派和摄像头看家

## 场景标签

`语音 Agent` `语音识别` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L10: * 🧠 **Private by default.** Everyday questions are answered by an AI model running *on your Pi* (Llama 3.2 3B).
> L42: 1. **The board** listens for the wake word "Jarvis" on its own chip. When it hears it, it streams your voice to the
> L44: 3. **The router** decides who answers:

## 星数曲线

```mermaid
xychart-beta
    title "nativebreed/pi-esp-jarvis 星数(近 3 点)"
    x-axis ["2026-11-01", "2026-11-08", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-01 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a4d8a492fdd3` · [字段定义](../../DATASET.md)*
