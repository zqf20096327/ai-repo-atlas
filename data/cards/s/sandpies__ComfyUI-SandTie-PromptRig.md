# sandpies/ComfyUI-SandTie-PromptRig

⭐ 4 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/sandpies/ComfyUI-SandTie-PromptRig) · [官网](https://huggingface.co/sandpies/ComfyUI-SandTie-PromptRig) · 个人维护

**ComfyUI 节点：为 MiniMax H3 视频工作流组装六字段提示词**

一个 ComfyUI V3 自定义节点，将 ComfyUI-Hand-Tie-Clips 的 H3 提示词编写引擎封装为单节点，插入标准 MiniMax H3 工作流（Ref2VA/T2VA/I2VA/FL2VA/L2VA/p-h3-image）。支持两种接线模式：输出 prompt 字符串（零 VRAM）或直出 positive+latent conditioning。提供三种编写方式：确定性 CPU 组装（无需 LLM）、调用本地 OpenAI 兼容服务器（LM Studio/nInfer/llama.cpp/vLLM）的两段式生成、以及基于 OpenCV 的视频节拍提取。附带 19 组导演拨盘、168 内置组合与示例工作流，需 ComfyUI v0.38.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零 VRAM CPU 模式：确定性 Shot-Tree 组装提示词，无需 LLM
- 动态 Autowgrow 插座扩展至 ref_image_1..9 / ref_video / ref_audio
- 双模式输出：prompt 字符串或原生 positive+latent conditioning
- 19 组导演拨盘、168 内置组合与 6 种 H3 输出格式

## 适用场景

- 在 ComfyUI 中为 MiniMax H3 视频生成快速编写六字段提示词
- 通过本地 LLM 服务器两段式生成并校验镜头连续性
- 从参考视频提取节拍与镜头轨迹转为分镜 beat

## 场景标签

`提示工程` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L1: # ComfyUI SandTie PromptRig (H3)
> L7: > **Stop hand-typing 6-field MiniMax H3 walls of text.** Drop **SandTie PromptRig (H3)** into any stock MiniMax H3 w
> L18: **SandTie PromptRig (H3)** wraps the entire H3 authoring engine from ComfyUI-Hand-Tie-Clips into **one plug-and-pla


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a2262b7a4194` · [字段定义](../../DATASET.md)*
