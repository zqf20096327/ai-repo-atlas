# manascb1344/zonos-api

⭐ 42 · Python · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/manascb1344/zonos-api) · 个人维护

**面向开发者的 Zonos 零样本 TTS FastAPI 服务**

以 FastAPI 封装 Zyphra 的 Zonos-v0.1-transformer 模型，提供文本转语音 REST 服务：支持零样本声音克隆（speaker_audio/prefix_audio）、eSpeak NG 覆盖 100+ 语言、44 kHz 输出，并可控制语速、音高与情感。提供 OpenAI 兼容的 /v1/audio/speech 端点（model 别名 tts-1 等），响应支持 wav/pcm/mp3/opus/aac/flac 格式（压缩格式需 ffmpeg）。版本 0.1.0，作者声明不稳定，可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容端点 POST /v1/audio/speech 与模型列表端点
- 零样本声音克隆与音频续写（speaker_audio/prefix_audio）
- Docker/docker-compose 部署，NVIDIA GPU 加速
- Swagger 文档、健康检查与结构化日志

## 适用场景

- 为应用接入 OpenAI 兼容格式的文本转语音接口
- 用参考音频克隆指定声音生成语音
- 自托管 TTS 服务以替代调用外部语音 API

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: A FastAPI service for Zonos text-to-speech with an OpenAI-compatible speech endpoint.
> L9: This service is built on the Zonos models created by Zyphra. The models provide zero-shot voice cloning, more than 1
> L101: - `POST /v1/audio/speech`: OpenAI-compatible speech generation


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `9e636e2bf33f` · [字段定义](../../DATASET.md)*
