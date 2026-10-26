# vorojar/VibeVoice

⭐ 27 · JavaScript · 推送 2026-02-20 · [GitHub](https://github.com/vorojar/VibeVoice) · 个人维护 · 中文 README

**本地运行的 AI 有声书工作室：文本转多角色语音（TTS）**

基于 Qwen3-TTS 模型的开源有声书制作工具，提供三种语音创建模式（9 个预置音色、3 秒参考音频克隆、自然语言描述设计音色）。核心为逐句编辑器：每句可独立设置音色与情绪指令，支持多角色混音生成；内置 Qwen3-4B 自动识别文本中的角色与情绪并一键分配音色。附带 Demucs 人声提取、Silero VAD 静音裁剪、wetext 中文文本规范化、-16 LUFS 响度归一化等音频预处理（均为可选依赖）。以 FastAPI 服务器加 Web UI 形式运行，100% 本地 GPU 推理，支持 10 种语言与 REST API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐句音色与情绪独立控制的句子编辑器
- 三种语音模式：预置音色/参考音频克隆/自然语言描述设计
- Qwen3-4B 自动识别角色与情绪并分配音色
- 参考音频三级自动预处理（人声提取/静音裁剪/文本规范化）与 -16 LUFS 响度归一化

## 适用场景

- 把小说或多角色文本制作成有声书，对话与旁白用不同音色
- 克隆特定人声用于配音或朗读生成
- 通过 REST API 将本地 TTS 能力集成到其他流程

## 场景标签

 · 领域:语音合成/有声书制作

## 证据(README 行号)

> L7: Powered by Qwen3-TTS models. Three voice creation modes, per-sentence granular control, LLM-powered smart character 
> L5: **Open-source AI audiobook studio** — a free, local alternative to ElevenLabs.

## 星数曲线

```mermaid
xychart-beta
    title "vorojar/VibeVoice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `aa3d688a0725` · [字段定义](../../DATASET.md)*
