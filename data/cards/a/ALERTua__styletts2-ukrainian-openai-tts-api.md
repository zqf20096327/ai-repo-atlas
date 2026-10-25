# ALERTua/styletts2-ukrainian-openai-tts-api

⭐ 45 · Python · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/ALERTua/styletts2-ukrainian-openai-tts-api) · 个人维护 · 中文 README

**为乌克兰语 StyleTTS2 提供 OpenAI 兼容 TTS API 的自托管网关**

基于 FastAPI 的 Docker 服务，将 patriotyk/styletts2-ukrainian Gradio 应用包装为 OpenAI TTS 兼容端点（POST /v1/audio/speech、GET /v1/audio/voices），输出 wav/mp3 音频。面向 Home Assistant（经 sfortis/openai_tts 集成）与 Music Assistant 等 OpenAI TTS 客户端用户，自托管部署。作者自述为临时过渡方案，待出现 Piper 兼容格式的同质量模型后可被替代。语音列表从 Gradio 应用描述读取，新增语音需重启；verbalizer 关闭时模型不处理数字，verbalization 结果可能不符合预期。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI TTS 兼容端点 /v1/audio/speech 与 /v1/audio/voices
- 以 docker-compose 部署，通过 GRADIO_URL 指向 StyleTTS2 Gradio 应用
- 内置数字转词的 verbalizer（AUTO_USE_VERBALIZER，默认开启）
- API key 留空即可，端点不做鉴权

## 适用场景

- 在 Home Assistant 中接入乌克兰语 TTS 语音播报
- 在 Music Assistant 中作为 OpenAI TTS 提供方使用
- 为任意 OpenAI TTS 客户端提供自托管乌克兰语语音合成服务

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L12: Provides OpenAI TTS API endpoints for the patriotyk/styletts2-ukrainian Gradio app, based on the Docker image ALERT
> L81: **Endpoint:** `POST /v1/audio/speech`

## 星数曲线

```mermaid
xychart-beta
    title "ALERTua/styletts2-ukrainian-openai-tts-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ca76dc452e96` · [字段定义](../../DATASET.md)*
