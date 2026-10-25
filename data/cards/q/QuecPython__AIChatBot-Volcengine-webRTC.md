# QuecPython/AIChatBot-Volcengine-webRTC

⭐ 37 · Python · NOASSERTION · 推送 2026-05-06 · [GitHub](https://github.com/QuecPython/AIChatBot-Volcengine-webRTC) · 组织维护 · 中文 README

**基于豆包 webRTC 的 QuecPython 嵌入式 AI 语音聊天机器人方案**

移远 QuecPython 推出的、运行在 EC600M/EC800M/EG810M 等蜂窝模组开发板上的 AI 对话机器人方案，通过火山引擎 RTC 库与豆包 webRTC 服务通信。功能包括 agent 切换、音色切换、ASR/TTS 字幕、语音打断、语音唤醒与服务器切换，代码用 Python 编写便于二次开发。运行需配套 ST7789 LCD、扬声器等硬件，通过 QPYcom 工具下载代码到模组文件系统执行；固件内含的火山引擎 token 仅临时测试用，正式使用需自行配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于火山引擎 RTC 库的豆包 webRTC 实时对话
- 支持语音唤醒、打断、ASR/TTS 字幕与音色切换
- Python 编写，支持二次开发

## 适用场景

- 在蜂窝物联网开发板上搭建语音 AI 对话终端
- 作为 QuecPython AI 应用二次开发的起点

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: QuecPython has launched an AI chatbot solution based on Doubao webRTC\. This solution is based on Volcengine RTC lib
> L19: - Support for agent switching\.
> L23: - Support for ASR subtitles\.

## 星数曲线

```mermaid
xychart-beta
    title "QuecPython/AIChatBot-Volcengine-webRTC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ea77766a616e` · [字段定义](../../DATASET.md)*
