# stepfun-ai/Step-Audio2

⭐ 1,527 · Python · Apache-2.0 · 推送 2026-03-16 · [GitHub](https://github.com/stepfun-ai/Step-Audio2) · 组织维护 · 中文 README

**端到端多模态语音大模型：音频理解与语音对话**

阶跃星辰开源的音频多模态大语言模型系列（Step-Audio 2 mini / mini Base / mini Think，Apache 2.0），支持 ASR、副语言信息理解（性别/年龄/情绪/音色）、语音翻译、工具调用与多模态 RAG，可按检索语音切换音色。安装需 Python 3.10+、PyTorch 2.3-cu121 与 CUDA Toolkit，提供 vLLM 后端（含 Docker 镜像）支持流式推理与多卡部署，另提供 Gradio 网页演示；模型权重托管于 HuggingFace 与 ModelScope。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ASR、副语言信息理解、语音翻译、语音对话端到端能力
- 支持工具调用与多模态 RAG，可按检索语音切换音色
- 提供 vLLM 后端 Docker 镜像，支持流式推理与多 GPU 部署
- Step-Audio 2 mini 系列以 Apache 2.0 开源

## 适用场景

- 本地部署中英语音识别与语音对话系统
- 构建带语音工具调用的实时语音助手
- 做语音翻译与方言/口音识别任务
- 通过 Gradio 演示快速试用模型能力

## 场景标签

`语音 Agent` `语音识别` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L27: Step-Audio 2 is an end-to-end multi-modal large language model designed for industry-strength audio understanding a
> L29: - **Advanced Speech and Audio Understanding**: Promising performance in ASR and audio understanding by comprehendin
> L31: - **Intelligent Speech Conversation**: Achieving natural and intelligent interactions that are contextually appropr

## 星数曲线

```mermaid
xychart-beta
    title "stepfun-ai/Step-Audio2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 1525 --> 1528
    line [1526, 1527]
```

2026-10-18 1,526 → 2026-10-27 1,527（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e81b189c420a` · [字段定义](../../DATASET.md)*
