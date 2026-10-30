# frankluise5220/ComfyUI-Lorahelper

⭐ 15 · Python · NOASSERTION · 推送 2026-03-17 · [GitHub](https://github.com/frankluise5220/ComfyUI-Lorahelper) · 个人维护 · 中文 README

**ComfyUI 插件：用本地 GGUF/Ollama 模型生成 Prompt 并整理 LoRA 训练数据**

面向 ComfyUI 用户的多节点插件：LH_AIChat 节点用本地 GGUF 模型或本地/远程 Ollama 实例做图像反推（JoyCaption 风格内置指令）与文本扩写，输出 Prompt 与 Danbooru tags；LH_AllInOne_Saver 一键打包图片、tags、日志与工作流元数据用于 LoRA 训练。另含 GGUF 加载器（支持 Qwen2.5-VL/Qwen3.5-VL、Llama 3.2 Vision、Yi-VL、Llava 等）、关键词触发的 LoRA 加载器、动态 Prompt 引擎等 9 个节点。安装方式为克隆到 custom_nodes 目录并 pip 安装依赖，依赖 llama-cpp-python，视觉功能需 CLIP/MMProj 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个 ComfyUI 节点：AI 对话、GGUF/Ollama 加载、训练集保存、动态 Prompt 等
- 图像反推与文本扩写生成 Flux/SD 可用 Prompt 及 Danbooru tags
- 支持 Qwen2.5-VL/Qwen3.5-VL 并提供 enable_thinking 思维链开关
- 一键保存图片、tags、日志与嵌入工作流元数据的 PNG

## 适用场景

- 批量反推图片生成 LoRA 训练用 tags 与 Prompt
- 一键打包 LoRA 训练数据集（图片+标签+工作流）
- 用本地 GGUF 或 Ollama 模型扩写简单描述为详细 Prompt

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L50: #### 1. LH_AIChat (DeepBlue Architecture)
> L116: #### 5. UniversalOllamaLoader (Local/Remote Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "frankluise5220/ComfyUI-Lorahelper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4e78c23216fa` · [字段定义](../../DATASET.md)*
