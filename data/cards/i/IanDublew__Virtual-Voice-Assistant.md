# IanDublew/Virtual-Voice-Assistant

⭐ 23 · Jupyter Notebook · 推送 2026-03-11 · [GitHub](https://github.com/IanDublew/Virtual-Voice-Assistant) · 个人维护

**语音助手：Whisper 转写语音，GPT 处理文本，gTTS 合成语音输出**

个人开发的虚拟语音助手项目，串接三项技术完成一次对话流程：用 Whisper 语音识别模型将用户语音转写为文本，将文本查询交给 GPT（OpenAI）生成回答，再用 gTTS（Google Text-to-Speech）将回答文本合成为语音并以 MP3 保存。面向想体验或学习语音→LLM→语音全链路的开发者。README 仅描述所用技术，未提供安装或运行命令细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 完成多语言语音识别与转写
- GPT 处理文本查询并生成回答
- gTTS 将文本转语音并保存为 MP3

## 适用场景

- 我想用语音提问并获得语音回答的桌面助手
- 学习语音识别与 LLM 串接的示例项目

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: This project uses three different technologies to transcribe speech to text, search text query using GPT and give ou
> L7: Whisper:

## 星数曲线

```mermaid
xychart-beta
    title "IanDublew/Virtual-Voice-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `633ee8a66696` · [字段定义](../../DATASET.md)*
