# stepfun-ai/StepAudio-Skills

⭐ 29 · Python · Apache-2.0 · 推送 2026-04-16 · [GitHub](https://github.com/stepfun-ai/StepAudio-Skills) · 组织维护 · 中文 README

**给 Claw 类 agent 的 StepFun 语音三技能包：TTS/ASR/语音推理**

仓库聚合三个独立的 SKILL.md 格式 agent 技能：step-tts（shell 实现的文本转语音与声音克隆，默认 step-tts-2 模型）、step-asr（Python 实现的流式语音转文字）、stepfun-step-audio-r1-1（基于 Chat Completions 的非流式语音推理，文本进音频出）。三项均通过 StepFun 云端 API 调用，共享 ~/.stepfun_api_key 或 STEPFUN_API_KEY 环境变量；用 npx skills add 安装到 OpenClaw 等 agent。附 CLI 冒烟测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- step-tts 提供语音合成与基于 Files API file_id 的声音克隆
- step-asr 支持音频转文字并输出文本/JSON
- stepfun-step-audio-r1-1 支持文本+本地音频输入的语音推理轮次，含 --dry-run 载荷检查
- 三技能共享 StepFun API key（支持环境变量与文件两种方式）

## 适用场景

- 为 Claw/OpenClaw 类 agent 安装语音合成或语音识别能力
- 通过 agent 用自然语言触发声音克隆与转写
- 构建文本提问、语音回答的对话流程

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L3: This repository combines three standalone StepFun skills:
> L5: - `step-tts`: text-to-speech and voice cloning via StepFun TTS
> L7: - `stepfun-step-audio-r1-1`: non-streaming speech reasoning turns via StepFun Chat Completions (`step-audio-r1.1`)

## 星数曲线

```mermaid
xychart-beta
    title "stepfun-ai/StepAudio-Skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `002e911cc124` · [字段定义](../../DATASET.md)*
