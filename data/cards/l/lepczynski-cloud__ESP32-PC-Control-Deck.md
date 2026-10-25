# lepczynski-cloud/ESP32-PC-Control-Deck

⭐ 38 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/lepczynski-cloud/ESP32-PC-Control-Deck) · 个人维护

**USB 连接的 ESP32 桌面触摸控制面板：显示 PC 遥测并触发快捷操作**

面向 Elecrow 2.8 英寸 ESP32 显示屏（ESP32-WROOM-32 + ILI9341 + XPT2046 触摸）的固件加 Python 主机桥项目。USB 线供电并传输数据：PC 读取 CPU/RAM/GPU/VRAM/网络/磁盘遥测显示到屏幕，触摸按钮把宏 ID 发回主机执行动作，如打开 ChatGPT 网页、检测并启动本地 Ollama、启动本地语音服务脚本、锁屏等，按钮与动作在 config.json 中配置。键盘类动作由主机桥代发，因板卡不暴露原生 USB HID。需 PlatformIO 烧录固件，Windows/macOS/Linux 均支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU/RAM/GPU/VRAM/网络/磁盘遥测实时显示，GPU 温度经 nvidia-smi 读取
- 六个可配置触摸按钮：ChatGPT/Ollama/语音服务/终端/任务管理器/锁屏
- Ollama 按钮检测 127.0.0.1:11434 并按需执行 ollama serve，避免重复进程
- newline-delimited JSON（DD: 前缀）串口协议，ESP32 不存储任何凭据

## 适用场景

- 在桌面小屏上随时查看电脑的 CPU/GPU/内存等状态
- 用触摸按钮快速启动本地 Ollama 或语音服务
- 一键打开终端、任务管理器或锁定电脑

## 场景标签

 · 领域:硬件/桌面监控外设

## 证据(README 行号)

> L3: A USB-connected ESP32 desktop display that monitors a Windows, macOS or Linux computer and works as a small touch co
> L38: |ChatGPT|Open `https://chatgpt.com/`|
> L39: |Ollama|Check local Ollama and start it when needed|

## 星数曲线

```mermaid
xychart-beta
    title "lepczynski-cloud/ESP32-PC-Control-Deck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eb454965dd01` · [字段定义](../../DATASET.md)*
