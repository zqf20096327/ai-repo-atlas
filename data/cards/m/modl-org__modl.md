# modl-org/modl

⭐ 27 · Rust · AGPL-3.0 · 推送 2026-07-25 · [GitHub](https://github.com/modl-org/modl) · [官网](https://modl.run) · 个人维护

**本地优先的 AI 图像生成与 LoRA 训练一体化 CLI/Web 工具**

单一 Rust 二进制提供模型下载、依赖解析、图像生成、LoRA 训练与输出管理：内置托管 Python 运行时负责 GPU 计算，无需另装外部依赖。支持 6 个模型家族共 16 个模型（Flux 2/1、Chroma、Z-Image、Qwen Image、SDXL/SD1.5）及 70+ 辅助模型，提供文生图、指令编辑、ControlNet、视觉语言（描述/打标/检测/分割）等命令；无本地 GPU 时可经用户自有 Vast.ai API key 租用远程 pod 训练与生成。CLI 与 Web UI（localhost:3939）共用同一引擎，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令完成 LoRA 训练（自动打标、数据集准备）
- 内容寻址模型仓库，ComfyUI/A1111 通过符号链接复用模型
- 按显存自动选择模型精度变体（fp16/fp8/量化），8GB 显卡可用
- 支持租用 Vast.ai pod 远程训练与生成，结果经 SSH 同步回本地

## 适用场景

- 用本地 GPU 从一组照片训练 LoRA 并生成图像
- 在本地运行 Flux/Qwen Image 等扩散模型做文生图与编辑
- 无本地 GPU 时租远程显卡完成训练和批量生成
- 统一管理 ComfyUI/A1111 已有模型避免重复存储

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L3: **Train LoRAs and generate images on your own GPU.** Web UI + CLI. Managed runtime. It just works.
> L10: modl generate "a cat on mars"
> L135: modl generate "prompt" --base flux-dev          # text to image

## 星数曲线

```mermaid
xychart-beta
    title "modl-org/modl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c84e52a7f21d` · [字段定义](../../DATASET.md)*
