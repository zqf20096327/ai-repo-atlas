# aserhat81/kivil

⭐ 14 · C# · MIT · 推送 2026-07-21 · [GitHub](https://github.com/aserhat81/kivil) · 个人维护

**ESP32-S3 桌面助手固件与 Windows Bridge，带可选本地 AI 语音**

运行于 LILYGO T-Display-S3 (ESP32-S3R8) 的开源桌面助手，由两部分组成：ESP32 固件提供表盘动画、时钟、ICS 日历、天气、汇率、PC 系统信息显示、Windows 通知转发、秒表与两个小游戏；Windows 端 Kıvıl Bridge（C#/.NET 8）提供日历/数据服务与通知传输。AI 为可选功能：经 Bridge 接入 Ollama 本地模型（默认 gemma3:1b），Vosk/Whisper 可选语音识别、Piper 可选 TTS。固件需在 LILYGO 官方 PlatformIO 环境编译，Bridge 提供安装包；面向可信局域网场景，默认密码需自行修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP32 固件 + Windows Bridge 双组件架构，经 HTTP/UDP 局域网发现
- 可选 Ollama 本地 AI（默认 gemma3:1b）、Vosk/Whisper STT、Piper TTS
- Windows 通知转发到设备屏幕、Web 控制面板、OTA 固件更新
- Bridge 提供 Windows 安装包（Inno Setup）与源码构建脚本

## 适用场景

- 在桌面摆一个显示时钟、日程、天气与 PC 状态的小屏设备
- 把 Windows 通知转发到桌上设备查看
- 接入本地 Ollama 与离线语音做可选的语音助手

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **Kıvıl**, LILYGO T-Display-S3 (ESP32-S3) üzerinde çalışan açık kaynak bir masaüstü asistanı projesidir. Proje iki a
> L5: 1. **ESP32 firmware** — ekran, Kıvıl yüz animasyonları, saat, takvim, hava durumu, sistem bilgileri, bildirimler, kr
> L6: 2. **Kıvıl Bridge (Windows)** — takvim/veri servisleri, bilgisayar sistem bilgileri, Windows bildirim aktarımı, Olla

## 星数曲线

```mermaid
xychart-beta
    title "aserhat81/kivil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `00c351076d0f` · [字段定义](../../DATASET.md)*
