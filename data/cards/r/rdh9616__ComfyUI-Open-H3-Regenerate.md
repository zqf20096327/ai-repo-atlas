# rdh9616/ComfyUI-Open-H3-Regenerate

⭐ 17 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/rdh9616/ComfyUI-Open-H3-Regenerate) · 个人维护

**ComfyUI 节点包：把低分辨率视频草稿三步重生成至 768P–4K**

为 NVIDIA Open-H3-Regenerate-2K 提供的 ComfyUI 节点与工作流：输入 H3 768P 草稿或 LTX/Wan/SANA-Video 低分辨率片段，经 H3 VAE 编码、LBH 3D 潜空间上采样、三步 Euler 再噪声化（σ 0.909375 起，CFG 1），以 ComfyUI 原生 MiniMax H3 模型在 768P–4K 原生分辨率重生成视频；并含快速 H3 VAE 解码器（StreamRender-H3 24 层蒸馏版）与用自有 OpenAI 兼容服务器上视觉模型为片段写 H3 提示词的节点。需 ComfyUI 0.42.0（含原生 MiniMax H3 支持）与多项下载权重（LoRA 12.4 GB、VAE 6.5 GB 等），README 注明高 σ 下重生成会明显改绘画面，可用 start_sigma 0.8 贴近草稿。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三步扩散将草稿原生重生成至 768P/1080P/2K/4K
- 快速 H3 VAE 解码器（36 层剪枝到 24 层并蒸馏，VRAM 约 6.5 GB + 每潜 token 26 KB）
- Video to H3 Prompt 节点：经 OpenAI 兼容服务器（vLLM/SGLang/llama.cpp/LM Studio）生成 H3 文生视频提示词，API key 仅从环境变量读取
- 细化潜变量先落盘再解码，解码失败无需重跑细化

## 适用场景

- 把我用 LTX/Wan/SANA-Video 生成的低分辨率片段重生成到 2K/4K
- 给 H3 草稿快速提升分辨率并保持布局与运动
- 自动为视频片段生成带镜头切分与声景描述的 H3 提示词

## 场景标签

`视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: ComfyUI nodes and workflows for NVIDIA's **Open-H3-Regenerate-2K**,
> L5: a 384P–576P clip from LTX, Wan, SANA-Video…) and regenerates it **natively at 768P, 1080P, 2K or 4K in three diffusi


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2f53c936bdfe` · [字段定义](../../DATASET.md)*
