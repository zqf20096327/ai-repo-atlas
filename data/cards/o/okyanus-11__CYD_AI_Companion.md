# okyanus-11/CYD_AI_Companion

⭐ 3 · C++ · MIT · 推送 2026-11-16 · [GitHub](https://github.com/okyanus-11/CYD_AI_Companion) · 个人维护

**ESP32 触摸屏设备上的 Wi-Fi AI 聊天固件，调用 Groq 接口**

面向 ESP32-2432S028（CYD）320x240 触摸屏的聊天固件：通过 Wi-Fi 调用 Groq chat-completions API 获取回复并显示在屏幕上。使用 PlatformIO 从 firmware/ 目录构建，需在本地 config.h 中填写 Wi-Fi 与 API 配置；固件校验 Groq 的 HTTPS 证书，未配置受信根 CA（GROQ_ROOT_CA）或 NTP 时钟不可用时直接拒绝请求而非关闭 TLS 校验，主题设置通过 ESP32 Preferences 持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP32-2432S028 触摸屏聊天固件，经 Wi-Fi 调用 Groq chat-completions API
- HTTPS 证书校验：缺失受信 CA 或时钟不可用时拒绝请求（fail closed）
- 三套界面主题，选择经 ESP32 Preferences 重启后保留
- PlatformIO 构建，CI 固件占用 14.1% RAM / 25.0% flash

## 适用场景

- 把便宜的 CYD 触摸屏改造成桌面 AI 聊天终端
- 学习 ESP32 上安全 TLS 调用 LLM API 的固件写法
- 给自制 IoT 小设备接入 Groq 对话能力

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Recovered ESP32-2432S028 touchscreen chat firmware using Wi-Fi and the Groq
> L52: Requires an ESP32-2432S028 CYD, USB data cable, PlatformIO and a Groq API key. Copy the firmware's `config.example.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `88ec7f00badd` · [字段定义](../../DATASET.md)*
