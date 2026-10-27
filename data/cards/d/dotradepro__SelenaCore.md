# dotradepro/SelenaCore

⭐ 25 · Python · MIT · 推送 2026-06-27 · [GitHub](https://github.com/dotradepro/SelenaCore) · [官网](https://selenehome.tech/) · 个人维护 · 中文 README

**本地优先的智能家居中枢：语音、自动化、设备控制全离线**

基于 FastAPI 的自托管智能家居中枢，核心为 24 个进程内模块：设备控制（Tuya/Gree/MQTT/Hue/ESPHome 插件式 provider）、气候、照明、能耗监控、YAML 自动化、在场检测、OTA 更新等。AI 部分为离线语音助手：Vosk/Whisper STT、Piper TTS、经 Ollama 做本地 LLM 意图理解，云端 LLM（OpenAI/Anthropic/Groq）为可选回退。面向消费者，一条 install.sh 加浏览器向导即可在树莓派 4 上运行，整个栈约占 1.5 GB 内存；界面提供 16 种语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线 STT/TTS（Vosk/Whisper + Piper）与 Ollama 本地 LLM 意图路由
- 24 个内置模块 + Docker 隔离用户模块与 WebSocket 模块总线
- 插件式设备 provider（Tuya/Gree/MQTT/Hue/ESPHome），UI 一键安装
- Integrity Agent 每 30 秒校验核心文件 SHA256，被改即回滚进入安全模式

## 适用场景

- 在树莓派上自建无需订阅的智能家居控制中枢
- 用本地离线语音助手控制灯光、空调与媒体
- 追踪每个设备的用电量并按房间查看

## 场景标签

`语音 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Local-first smart home hub. No cloud required. No subscription. Just your hardware.**
> L22: - **100% offline** — voice assistant, automations, device control all run on your hardware. The internet is optiona
> L31: Full offline STT (Vosk / Whisper) and TTS (Piper) pipeline. Local LLM inference via Ollama for natural language und

## 星数曲线

```mermaid
xychart-beta
    title "dotradepro/SelenaCore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `eb575b76a4aa` · [字段定义](../../DATASET.md)*
