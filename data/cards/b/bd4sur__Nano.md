# bd4sur/Nano

⭐ 297 · C · 推送 2026-10-30 · [GitHub](https://github.com/bd4sur/Nano) · [官网](https://bd4sur.com/Nano/infer/web) · 个人维护 · 中文 README

**从零实现的 Transformer 语言模型训练与多端推理项目，供个人研究赏玩**

个人维护的 Transformer 语言模型全流程实践项目：覆盖预训练、全参数 SFT、LoRA 微调、模型量化导出，以及从 PC、树莓派、路由器、STM32/ESP32 单片机、浏览器 WASM 到自研 Scheme 解释器的多种推理形态。自研 Nano 系列（230k 至 168M 参数）及 Psycho 试验模型，纯 C 推理引擎基于 llama2.c 实现，支持 W32A32/W8A32/W4A32 量化，并适配 Qwen2/Qwen3 端侧转换。当前不支持多轮对话 SFT，DeepSpeed 分布式训练已标记废弃。

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

- Transformer 预训练、SFT、LoRA 微调与模型量化导出的完整训练链路
- 纯 C 推理引擎可部署于树莓派、路由器、STM32/ESP32 单片机等设备
- 浏览器 WASM 推理开箱即用，含 ASR/TTS 且全程本地
- 支持将 Qwen2/Qwen3 HuggingFace 模型转换为端侧二进制格式

## 适用场景

- 在各类低资源硬件上实践 LLM 推理部署
- 完整跑通语言模型预训练与监督微调流程
- 在浏览器本地体验语言模型推理与指令问答

## 场景标签

`模型训练` `微调` `推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L11: **Nano**是Transformer结构的语言模型，供个人赏玩、研究、炼丹炉煲机。期望：
> L13: - **训练实践**：实现Transformer语言模型的预训练和监督微调，训练出若干可用的模型。
> L14: - **推理实践**：在单板机、单片机、浏览器、PC、服务器等各类环境上，高效推理语言模型。

## 星数曲线

```mermaid
xychart-beta
    title "bd4sur/Nano 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 296 --> 298
    line [297, 297]
```

2026-10-18 297 → 2026-10-31 297（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `05efeabc8781` · [字段定义](../../DATASET.md)*
