# julienkay/tools.doji.transformers

⭐ 25 · C# · MIT · 推送 2026-11-25 · [GitHub](https://github.com/julienkay/tools.doji.transformers) · 个人维护

**让 Unity 开发者在游戏/应用内运行预训练 transformer 模型**

Hugging Face transformers 库的 C# 移植，以 Unity 包形式发布，基于 Unity Inference Engine（Sentis）运行预训练模型。两大用途：为 tools.doji.diffusers 提供文本生成（Stable Diffusion 流水线的 CLIPTokenizer/T5Tokenizer），以及在 Unity 中运行小型 LLM（SmolLM2、Phi-3、Qwen3 等）。模型经 AI Model Hub 下载，支持 optimum 命名的 ONNX 导出，并可加载 llama.cpp 的 GGUF 文件（Q8_0/Q4_K 等量化权重驻留 GPU）。通过 OpenUPM 分发，附文本生成示例场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AutoTokenizer/AutoModelForCausalLM 的 FromPretrainedAsync 加载与 Generate 生成接口
- AutoModelForCausalLM.FromGguf 直接加载 llama.cpp GGUF 文件及其中 chat template
- GPU 上 token 采样与 PreTrainedModel.Pacing 每帧主线程时间预算控制
- README 给出 D3D12/D3D11 下多模型的 tokens/s、VRAM/RAM 实测数据

## 适用场景

- 在 Unity 应用中接入小型 LLM 做文本生成
- 为 Stable Diffusion 的 Unity 流水线提供分词器
- 在游戏内加载 GGUF 量化模型并控制每帧生成耗时

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: A Unity package to run pretrained transformer models with Unity Inference Engine
> L12: This is essentially a C# port of Hugging Face’s [transformers] library.
> L16: - To run small LLMs like SmolLM2 in Unity

## 星数曲线

```mermaid
xychart-beta
    title "julienkay/tools.doji.transformers 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-11-26 25 → 2026-11-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `24f596524511` · [字段定义](../../DATASET.md)*
