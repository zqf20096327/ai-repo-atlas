# maemreyo/omnivoice-server

⭐ 93 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/maemreyo/omnivoice-server) · 个人维护

**OmniVoice TTS 模型的 OpenAI 兼容 HTTP 服务封装**

将 OmniVoice 文本转语音模型包装为 OpenAI 兼容 HTTP API 的 Python 服务端，提供语音设计（性别/年龄/音高/口音）、参考音频语音克隆、实时分块流式输出与克隆语音的持久化存储，可作为 OpenAI TTS 端点的直接替代。基于 FastAPI 构建，通过 pip 安装，需先装 PyTorch。当前处于早期开发阶段，CPU 与 CUDA 可用，MPS（Apple Silicon）存在已知问题，性能 RTF 约 CPU 4.92 / GPU 0.2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容 API，可直接替换 OpenAI TTS 端点
- 语音设计（性别/年龄/音高/口音/方言）与参考音频克隆
- 实时音频分块流式输出与语音档案持久化
- CPU 与 CUDA 已验证可用，MPS 存在已知问题

## 适用场景

- 为已有 OpenAI TTS 客户端切换到自托管 OmniVoice 服务
- 搭建支持语音克隆与流式输出的 TTS API 服务
- 在 CPU 或 CUDA 环境本地运行文本转语音推理

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L9: OpenAI-compatible HTTP server for OmniVoice text-to-speech.
> L43: **omnivoice-server** wraps the OmniVoice TTS model with an OpenAI-compatible HTTP API:
> L49: - **OpenAI-Compatible**: Drop-in replacement for OpenAI TTS endpoints

## 星数曲线

```mermaid
xychart-beta
    title "maemreyo/omnivoice-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 91 --> 94
    line [92, 93, 93]
```

2026-10-18 92 → 2026-10-28 93（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a420f6eb4019` · [字段定义](../../DATASET.md)*
