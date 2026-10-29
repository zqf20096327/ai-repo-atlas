# Hanzo-Huang/rk3576-home-assistant-voice

⭐ 19 · Python · 推送 2026-10-24 · [GitHub](https://github.com/Hanzo-Huang/rk3576-home-assistant-voice) · 个人维护

**在 RK3576 开发板上本地运行 Home Assistant 语音助手全套服务栈**

面向 Rockchip RK3576 板子的 Docker Compose 语音服务栈：通过 Wyoming 协议提供 Whisper 语音识别与 Piper 语音合成，openWakeWord 唤醒词检测，以及基于 RKLLM 的 OpenAI 兼容 API 运行 Qwen2.5-1.5B 对话模型，三类模型均由 RK3576 NPU 加速。镜像以 Linux ARM64 预构建发布，用户 docker compose 拉取即可运行，随后在 Home Assistant 中添加 Wyoming 集成并配置 Assist pipeline。支持更换唤醒词、LLM、Piper 声音（含中文）与 Whisper 语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper/Piper/openWakeWord/RKLLM 四个服务经 Docker Compose 一键启动
- 三类模型均由 RK3576 NPU 加速，镜像预构建无需本地编译
- RKLLM 提供 OpenAI 兼容 API（端口 8001），可接入 Home Assistant 对话代理
- 可切换中文 Piper 声音与中文 Whisper 识别

## 适用场景

- 在 RK3576 板上搭建完全本地的 Home Assistant 语音助手
- 不依赖云端、私有化运行 STT/TTS/LLM 语音链路
- 为 Home Assistant Assist 接入本地 NPU 加速对话模型

## 场景标签

`语音 Agent` `语音识别` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: A local voice stack for running Home Assistant Assist on a Rockchip RK3576 board.
> L7: - Speech-to-text with Whisper through the Wyoming protocol
> L10: - Local conversation handling with Qwen 2.5 1.5B through an OpenAI-compatible RKLLM API

## 星数曲线

```mermaid
xychart-beta
    title "Hanzo-Huang/rk3576-home-assistant-voice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a6640fc6c151` · [字段定义](../../DATASET.md)*
