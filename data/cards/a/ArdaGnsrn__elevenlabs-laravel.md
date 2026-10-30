# ArdaGnsrn/elevenlabs-laravel

⭐ 20 · PHP · MIT · 推送 2026-04-20 · [GitHub](https://github.com/ArdaGnsrn/elevenlabs-laravel) · [官网](https://packagist.org/packages/ardagnsrn/elevenlabs-laravel) · 个人维护

**Laravel 框架的 ElevenLabs 文本转语音 API 封装包**

面向 PHP Laravel 开发者的开源 Composer 包，封装 ElevenLabs.io 文本转语音 API。提供 textToSpeech() 与 getModels() 两个方法，支持指定 voiceId、modelId 与语音参数（stability、similarity_boost、style、speaker_boost），默认模型为 eleven_multilingual_v2，可保存音频文件或获取流。通过 env 配置 API key，限制为需依赖外部 ElevenLabs 云服务方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- textToSpeech() 生成语音，可保存文件或获取流
- getModels() 获取可用模型列表
- 语音参数可配置（stability/similarity_boost/style/speaker_boost）
- 通过 config 与 env 管理 API key

## 适用场景

- 在 Laravel 应用中集成 ElevenLabs 文本转语音功能
- 查询 ElevenLabs 可用模型列表
- 为应用内容生成语音音频文件

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L9: This is an Open Source PHP Laravel package for elevenlabs.io Text to Speech API. You can
> L26: composer require ardagnsrn/elevenlabs-laravel

## 星数曲线

```mermaid
xychart-beta
    title "ArdaGnsrn/elevenlabs-laravel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `004c2e655728` · [字段定义](../../DATASET.md)*
