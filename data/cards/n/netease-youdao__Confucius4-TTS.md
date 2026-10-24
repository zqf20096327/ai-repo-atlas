# netease-youdao/Confucius4-TTS

⭐ 846 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/netease-youdao/Confucius4-TTS) · 组织维护 · 中文 README

**多语言跨语言零样本语音克隆 TTS 引擎**

网易有道开源的基于语音编码器 + LLM 架构的文本转语音系统，支持 14 种语言的跨语言零样本语音克隆：无需参考文本即可克隆音色，并支持情感迁移，切换语言时保持说话人身份。提供 example.py 脚本、Python API、Gradio Web 界面与 FastAPI 服务端（含流式端点）；训练管线覆盖 T2S 与 S2A（flow-matching）两模块，训练时冻结 T2S 主干。T2S 阶段默认用 HuggingFace Transformers，可切换 vLLM 0.16.0 后端加速。要求 Python 3.10 与 CUDA 12.6。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 种语言的零样本/跨语言语音克隆，无需参考文本
- T2S + S2A（flow-matching）架构，可切换 vLLM 0.16.0 后端加速
- 提供 Gradio Web 界面与 FastAPI 流式服务端
- 提供 T2S/S2A 微调训练管线

## 适用场景

- 用一段参考音频跨语言合成保持原音色的语音
- 为其他服务提供可编程调用的 TTS API
- 在自己的多语言语音数据上微调模型

## 场景标签

`语音合成` `微调` · 领域:内容生成

## 证据(README 行号)

> L19: Confucius4-TTS is an advanced LLM-based text-to-speech (TTS) system designed for multilingual and cross-lingual spe
> L26: - **Zero-Shot Voice Transfer**: Clone voices without additional training

## 星数曲线

```mermaid
xychart-beta
    title "netease-youdao/Confucius4-TTS 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 841 --> 847
    line [842, 843, 845, 846]
```

2026-10-18 842 → 2026-10-24 846（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `8a79e20ba2e1` · [字段定义](../../DATASET.md)*
