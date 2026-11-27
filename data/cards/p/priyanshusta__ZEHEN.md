# priyanshusta/ZEHEN

⭐ 8 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/priyanshusta/ZEHEN) · [官网](https://priyanshusta.github.io/ZEHEN/) · 个人维护

**Windows 手势虚拟鼠标加离线语音桌面助手**

面向 Windows 10/11 的开源 Python 单文件桌面工具：用普通摄像头经 MediaPipe 跟踪双手 21 个关键点，实现光标移动、捏合点击、滚动、缩放与空中书写（Windows 墨迹识别）；唤醒词后由本地 faster-whisper 转录语音，通过 Windows UI Automation 与 PowerShell 执行多步操作（最多 6 步），以 Kokoro 82M 离线语音回复。AI 规划可选云端 API 或内置离线 Qwen3 1.7B；含安全防火墙拦截破坏性命令。需 Python 3.10+、摄像头与麦克风，无需额外硬件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MediaPipe 双手 21 点跟踪的捏合点击、滚动、缩放与空中书写
- 本地 faster-whisper 转录加 Vosk 备份，离线 Kokoro 82M 语音回复
- 经 Windows UI Automation 与 PowerShell 执行最多 6 步的多步操作
- 安全防火墙拦截破坏性命令并要求语音确认

## 适用场景

- 用摄像头手势代替鼠标控制 Windows 桌面
- 语音口令让助手打开应用、输入文字、执行 PowerShell 操作
- 无网络或不愿数据出机的离线语音控制场景

## 场景标签

`GUI 自动化` `AI 助手` `语音 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L23: **ZEHEN** is a free, open-source **J.A.R.V.I.S. / Iron Man–inspired desktop interface for Windows 10 and Windows 11
> L25: Using MediaPipe to track **21 landmarks per hand across both hands**, ZEHEN filters out hand jitter with a One Euro
> L131: |**Supported Providers**|**Groq** (`openai/gpt-oss-120b`), **Gemini** (`gemini-flash-latest`), **OpenRouter** (`op


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `205b404b8d89` · [字段定义](../../DATASET.md)*
