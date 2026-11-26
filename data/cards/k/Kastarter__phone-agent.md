# Kastarter/phone-agent

⭐ 4 · Swift · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Kastarter/phone-agent) · 个人维护

**用 ESP32 蓝牙棒操控真实 iPhone 的 AI 手机代理**

该项目由一个 SwiftUI iOS 应用与一块 ESP32-S3 蓝牙棒组成：蓝牙棒模拟鼠标键盘，应用通过屏幕共享读取屏幕帧，Fast agent 每次截屏调用一次模型并返回最多六个动作，由指针点击完成操作。内置快速路径（文本识别开 App、键击输入、指针瞄准校正）以减少模型调用次数，并支持接入 LiveKit 语音通话由 agent 下发 control_phone 指令。需要 iOS 27、Xcode 与 ESP-IDF 构建，仅支持竖屏，发送消息前会先请求确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ESP32-S3 棒模拟蓝牙鼠标键盘，通过 AssistiveTouch 点击与滑动
- Fast agent 截屏-动作循环，单次查看返回最多六个动作
- 设备端文本识别与键盘布局校准，减少模型调用
- LiveKit 语音通话中通过 control_phone 驱动手机操作

## 适用场景

- 让 AI 代理代替我在 iPhone 上打开应用、输入文字、完成任务
- 通过语音通话让代理操作手机并汇报结果
- 在 iOS 不开放自动化的限制下用蓝牙外设实现点击控制

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: An AI agent that uses a real iPhone the way you do: it looks at the screen and moves a pointer. A small Bluetooth st
> L30: - **Actor loop.** Each look sends one screenshot and gets back up to six actions. A planner writes a plan only when
> L36: Model calls go to any OpenAI-compatible Chat Completions endpoint. The default is GPT-6 Luna on OpenRouter. The cha

## 星数曲线

```mermaid
xychart-beta
    title "Kastarter/phone-agent 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `2a2e58584a9f` · [字段定义](../../DATASET.md)*
