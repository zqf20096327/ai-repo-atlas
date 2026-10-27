# VAST-AI-Research/SeqTex

⭐ 50 · Python · NOASSERTION · 推送 2025-12-12 · [GitHub](https://github.com/VAST-AI-Research/SeqTex) · [官网](https://yuanze1024.github.io/SeqTex/) · 组织维护 · 中文 README

**基于视频扩散先验的端到端 3D 网格纹理生成方法**

SIGGRAPH Asia 2025 会议论文的官方实现：SeqTex 利用视频扩散先验（Wan2.1）将网格纹理生成表述为视频序列生成任务，支持图像条件（img2tex）与文本条件（经 SDXL/FLUX 转图像）两种输入，输出 UV 纹理贴图。训练支持 3D 数据集与图像数据集两种格式，默认使用 FSDP。推理在 1×A100 80GB 上测试，训练需至少 8×80GB GPU（论文结果为 4 节点训练 1 周），并提供 Hugging Face 在线 Demo 与模型权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以视频序列方式为网格生成 UV 纹理贴图
- 支持图像条件与 SDXL/FLUX 文本转图像条件两种输入
- 提供模型权重与 Hugging Face 在线 Demo
- 已被集成进 ComfyUI

## 适用场景

- 为 3D 网格模型生成纹理贴图
- 复现论文中的 img2tex/geo2mv 任务结果
- 在 ComfyUI 工作流中使用该纹理生成方法

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: SeqTex: Generate Mesh Textures in Video Sequence
> L62:     system.seqtex_transformer_name_or_path=VAST-AI/SeqTex-Transformer
> L122: - Wan2.1 for the 3D prior from video sequences

## 星数曲线

```mermaid
xychart-beta
    title "VAST-AI-Research/SeqTex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-27 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cad11d7f1cdf` · [字段定义](../../DATASET.md)*
