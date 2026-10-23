# AkshitIreddy/Interactive-LLM-Powered-NPCs

⭐ 733 · Rust · MIT · 推送 2026-10-16 · [GitHub](https://github.com/AkshitIreddy/Interactive-LLM-Powered-NPCs) · [官网](https://www.linkedin.com/company/alystria-ai) · 个人维护

**给已发售游戏加可语音对话的 LLM NPC 系统**

面向玩家的开源项目：在未修改游戏源码的前提下，通过麦克风语音与任意游戏中的 NPC 对话。机制为语音转文本、摄像头面部识别确定当前 NPC、结合向量库记忆与 pre_conversation.json 风格文件，由 LLM（默认 Cohere Trial API）生成回应，再用 SadTalker 生成面部动画视频并替换游戏画面中的脸部像素。通过摄像头识别玩家表情以调整回应。安装流程面向 Windows：需 Python 3.10.6、GIT、wget、Build Tools、FFmpeg，经 git clone 与 pip 安装，并为新游戏配置世界文件与角色模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需修改游戏源码，替换游戏画面中的脸部像素实现 NPC 说话动画
- 面部识别区分背景/配角 NPC，为背景 NPC 生成人格
- 向量库提供 NPC 记忆与世界观信息，pre_conversation.json 塑造对话风格
- 摄像头情绪识别调整 NPC 回应

## 适用场景

- 在 Cyberpunk 2077、GTA 5 等已发售游戏中与任意 NPC 语音对话
- 为背景 NPC 生成独特人格与专属对话
- 骑马或战斗等非面对面场景通过喊名字继续对话

## 场景标签

`语音 Agent` `人脸识别` · 领域:对话与助手

## 证据(README 行号)

> L3: Interactive LLM Powered NPCs, is an open-source project that completely transforms your interaction with non-player 
> L35: 🧠 LLM Integration: The transcribed text and character information are passed to a Large Language Model (LLM), which
> L41: 🕹️ Integration with the Game: The facial animation video and audio are seamlessly integrated into the game by repla

## 星数曲线

```mermaid
xychart-beta
    title "AkshitIreddy/Interactive-LLM-Powered-NPCs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 731 --> 734
    line [732, 733]
```

2026-10-18 732 → 2026-10-23 733（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `13f3892f11a4` · [字段定义](../../DATASET.md)*
