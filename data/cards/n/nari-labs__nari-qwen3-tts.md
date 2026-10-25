# nari-labs/nari-qwen3-tts

⭐ 188 · Python · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/nari-labs/nari-qwen3-tts) · [官网](https://nari-labs.com/) · 组织维护

**单卡 H100 上高性能服务 Qwen3-TTS 的流式推理引擎**

Nari Labs 开发的 Qwen3-TTS 1.7B CustomVoice 单 GPU 服务实现：通过 HTTP 与 WebSocket 提供流式/非流式语音生成及增量文本输入。官方数据为在单张 NVIDIA H100 SXM 上达到 10 RPS、p95 首音频延迟低于 50 ms；20 RPS 时低于 80 ms。提供 ttfa/balanced/throughput 三种延迟-吞吐配置档与 YAML 覆盖调优，API 兼容 OpenAI Audio Speech 请求格式，仅支持该模型、wav/pcm 输出与 speed:1.0。以 Docker 镜像或 uv 环境运行，需 CUDA 13.0 兼容驱动，仅测试过英文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单张 H100 上 10 RPS、p95 TTFA < 50 ms（20 RPS 时 < 80 ms）
- HTTP 流式/非流式与 WebSocket 增量文本输入
- ttfa/balanced/throughput 三档配置与严格 YAML 覆盖
- POST /v1/audio/speech 遵循 OpenAI Audio Speech 请求格式

## 适用场景

- 在单张 H100 上部署低延迟流式 TTS 服务
- 为对话或实时应用提供增量文本的语音生成
- 按负载特征切换延迟或吞吐优先档位

## 场景标签

`语音合成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L5: Nari Qwen3-TTS is a high-performance, single-H100 serving implementation of
> L7: It exposes streaming and non-streaming speech generation over HTTP, plus
> L120: `POST /v1/audio/speech` follows the OpenAI Audio Speech request shape. Nari Qwen3-TTS

## 星数曲线

```mermaid
xychart-beta
    title "nari-labs/nari-qwen3-tts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 186 --> 189
    line [187, 188, 188]
```

2026-10-18 187 → 2026-10-25 188（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d9ef0eb7cadf` · [字段定义](../../DATASET.md)*
