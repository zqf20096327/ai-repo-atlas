# bold-ronin/lira

⭐ 15 · Dart · MIT · 推送 2026-03-02 · [GitHub](https://github.com/bold-ronin/lira) · 个人维护

**语音优先的 AI 陪伴移动应用：实时对话与情绪关怀**

Flutter 移动应用（iOS/Android），以“祖母”克隆语音提供日常建议、情绪问候、规划提醒等陪伴对话，并支持按需图像生成。流程为：Flutter 采集语音→STT（Whisper/Vosk）→Python FastAPI 后端调用免费 LLM（OpenRouter/HuggingFace，Mistral/LLaMA 等）→Coqui TTS 或 flutter_tts 合成语音回放。对话记忆仅在内存中保留最近 3–5 条，定位隐私优先、多为端侧/本地。目标用户为埃塞俄比亚及全球离散社区的忙碌人群。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音实时对话：STT（Whisper/Vosk）+ LLM + TTS（Coqui/flutter_tts）链路
- 通过 LLM_MODEL 环境变量切换 OpenRouter/HuggingFace/本地推理，无需改 Flutter 代码
- 对话记忆仅在 RAM 中保留最近 3–5 条（隐私优先）
- 规划多语言支持（阿姆哈拉语、英语）与按需图像生成

## 适用场景

- 用语音与 AI 陪伴助手进行日常倾诉和情绪问候
- 获取生活建议、日程提醒等陪伴式对话
- 在本地/免费 LLM 上搭建低成本的语音对话应用

## 场景标签

`语音 Agent` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L3: **Lira** is a sleek Flutter mobile app (iOS/Android) that acts as your always-on voice buddy—like ChatGPT’s voice mo
> L79:     B --> C[Speech-to-Text (Whisper / Vosk / Coqui STT)]
> L87: 4. LLM generates empathetic, agentic response

## 星数曲线

```mermaid
xychart-beta
    title "bold-ronin/lira 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `af35be756d3c` · [字段定义](../../DATASET.md)*
