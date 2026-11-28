# timmyy123/LLM-Hub

⭐ 669 · Swift · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/timmyy123/LLM-Hub) · [官网](https://llm-hub.app) · 个人维护

**手机与桌面上本地运行 LLM 聊天及图像/视频/音乐生成的应用**

跨 Android、iOS、Windows、macOS、Linux 的开源本地 AI 应用，全部推理在设备端完成，不依赖云与账号。功能覆盖多轮聊天（RAG 记忆、网页搜索、TTS）、自主 Agent（函数调用、MCP 工具、Termux 命令生成）、Stable Diffusion 图像生成、LTX-Video/Stable Video Diffusion 视频生成、Stable Audio 3/Magenta Realtime 2 音乐生成、离线转录与翻译、语音克隆、图像放大与物体擦除等。通过 LiteRT-LM、llama.cpp（含自维护补丁分支）、ONNX Runtime 等引擎支持 GGUF 等多种模型格式，并可对外提供 OpenAI/Anthropic 兼容 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 设备端推理，零数据收集，无需账号与云端
- AI Agent 支持设备函数调用、MCP 工具与 Termux 命令生成及错误自纠正循环
- Flash streaming 可在内存受限设备上运行大于 RAM 的 MoE 模型
- GPU/NPU 加速（Hexagon NPU、OpenCL、Vulkan）并自动 CPU 回退

## 适用场景

- 在无网络或注重隐私的环境下本地聊天与生成图像/视频/音乐
- 在 Android 上通过 Termux 运行 Codex 或 Claude Code 搭配本地模型写代码
- 离线转录语音、翻译文本/图片/音频、克隆自定义语音
- 为其他应用提供 OpenAI/Anthropic 兼容的本地 API 服务

## 场景标签

`编码 Agent` `图像生成` `视频生成` `语音合成` · 领域:编码与开发

## 证据(README 行号)

> L5: **LLM Hub** is an open-source app for on-device LLM chat, image generation, video generation, and music generation, 
> L51: |**Chat**|Multi-turn conversations with RAG memory, web search, TTS auto-readout, and multimodal input|
> L114: - **100% on-device processing** - no internet required for inference

## 星数曲线

```mermaid
xychart-beta
    title "timmyy123/LLM-Hub 星数(近 22 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-28"]
    y-axis "stars" 618 --> 673
    line [623, 624, 627, 628, 629, 622, 638, 641, 643, 646, 647, 651, 654, 656, 658, 659, 661, 663, 665, 667, 669, 669]
```

2026-10-26 623 → 2026-11-28 669（+46）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `5fc18048fc29` · [字段定义](../../DATASET.md)*
