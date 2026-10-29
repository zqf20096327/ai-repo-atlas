# yu20103983/xiaolong-openclaw

⭐ 27 · Python · MIT · 推送 2026-04-09 · [GitHub](https://github.com/yu20103983/xiaolong-openclaw) · [官网](https://github.com/yu20103983/xiaolong-openclaw#-快速开始) · 个人维护 · 中文 README

**中文语音助手：唤醒词+ASR+OpenClaw Agent+TTS，语音指挥 AI 干活**

面向终端用户的 Windows 中文语音助手：本地 SenseVoice+Silero VAD 实现离线唤醒词（'小龙小龙'，含大量近音变体容错），识别指令后交给 OpenClaw Agent 执行文件操作、命令执行、联网搜索等任务，结果经 TTS 三级回退（Edge TTS→Matcha-TTS→Windows SAPI）流式播报。支持连续对话、语音打断、蓝牙耳机全双工/半双工。需 Python 3.10+ 与 Node.js 18+，通过 OpenClaw Gateway 接入 LLM（需自配 API Key），setup.bat 一键安装依赖并下载模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线唤醒：SenseVoice + Silero VAD 纯本地运行，无需联网
- 唤醒词近音容错：16 种'小'+14 种'龙'变体
- TTS 三级回退：Edge TTS → Matcha-TTS（本地）→ Windows SAPI
- 通过 OpenClaw Skills 生态扩展能力，支持自定义 Skill

## 适用场景

- 戴耳机用语音让 AI 在后台读代码、执行命令并汇报结果
- 语音连续对话与口语练习
- 国内网络下使用本地离线唤醒与本地 TTS 兜底

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: **说"小龙小龙"唤醒 → 语音发指令 → OpenClaw 干活 → 语音报结果**
> L15: - 🔧 **完整 AI 能力**：通过 OpenClaw 获得文件操作、命令执行、联网搜索、编程等能力
> L28: 麦克风 → [Silero VAD + SenseVoice ASR] → 文字

## 星数曲线

```mermaid
xychart-beta
    title "yu20103983/xiaolong-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `e699cf82e67b` · [字段定义](../../DATASET.md)*
