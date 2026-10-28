# ruguo0119/AI-Desktop-Pet

⭐ 22 · JavaScript · 推送 2026-01-22 · [GitHub](https://github.com/ruguo0119/AI-Desktop-Pet) · 个人维护 · 中文 README

**带语音交互与长期记忆的 Live2D AI 桌面宠物**

基于 Electron + React + Python FastAPI 的桌面宠物应用：集成 Live2D 模型（Haru/Hiyori/PinkFox），通过 Gemini/DeepSeek 等兼容 OpenAI 格式的 LLM 实现陪聊，CosyVoice 做 TTS、SenseVoice 做语音识别，支持麦克风实时语音输入与文字输入。记忆采用 ChromaDB 向量长期记忆加 JSON 事实库（带时间戳），并支持屏幕截图视觉感知。前后端通过 WebSocket 双向通信，AI 可主动发言。需分别启动 Python 后端与 npm 前端，并配置 API 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Live2D 多角色模型，实时表情/动作同步
- ChromaDB 向量长期记忆 + JSON 事实库（带时间戳）
- 语音输入（F2 快捷键）+ TTS 发声 + 屏幕截图视觉感知
- WebSocket 双向通信，支持 AI 主动发言与打断

## 适用场景

- 桌面上与 AI 角色进行语音或文字陪伴对话
- 让桌宠记住用户信息并持久化学习
- 通过截屏让桌宠感知当前屏幕内容

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: - 🤖 **多 AI 模型集成**：Gemini/deepseek LLM + CosyVoice TTS + SenseVoice STT
> L12: - 🎙️ **实时语音交互**：麦克风输入识别 + 文字转语音输出(长按F2可以用快捷键启用语音输入) 你可以让她闭嘴(AI会自行判定），进入静默模式（AI将不会主动说话)
> L16: - 👀 **视觉感知系统**:输入内容含有“看看”等关键词，可以给AI桌宠传入当前电脑屏幕的截屏照片

## 星数曲线

```mermaid
xychart-beta
    title "ruguo0119/AI-Desktop-Pet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4e84bd3ecf1a` · [字段定义](../../DATASET.md)*
