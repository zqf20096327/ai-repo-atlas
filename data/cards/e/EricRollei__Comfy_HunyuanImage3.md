# EricRollei/Comfy_HunyuanImage3

⭐ 67 · Python · NOASSERTION · 推送 2026-04-30 · [GitHub](https://github.com/EricRollei/Comfy_HunyuanImage3) · 个人维护

**在 ComfyUI 中本地运行腾讯混元 Image 3.0 的自定义节点集**

面向 ComfyUI 用户的自定义节点集，用于在本地加载与运行腾讯混元 HunyuanImage-3.0（80B 参数多模态图像生成模型）。提供 BF16/INT8/NF4 三种量化加载节点、块交换、显存预算管理与 CPU 卸载，最低 24GB 显存可运行 NF4 量化版（配合系统内存卸载）。Instruct 变体支持内置 CoT 提示增强、自然语言图像编辑与 2–5 图融合，可选接入任意 OpenAI 兼容 LLM API 做提示重写。本集成代码以 CC BY-NC 4.0 非商业许可发布，需 NVIDIA GPU 与 CUDA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BF16/INT8/NF4 多档量化加载节点，含低显存（24GB 起）工作流
- Instruct 模型支持内置 CoT 提示增强、图像编辑与多图融合
- 统一 Generate V2 节点自动检测量化格式并管理块交换与显存
- Hugging Face 提供预量化 v2 权重（NF4/INT8）下载

## 适用场景

- 在 ComfyUI 中用 24GB 消费级显卡跑 NF4 量化的混元 Image 3
- 用自然语言指令做图像编辑与多张参考图融合
- 在高显存卡上做 3MP–4K+ 高分辨率生成

## 场景标签

`图像生成` `模型量化` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L7: Professional ComfyUI custom nodes for Tencent HunyuanImage-3.0, the powerful 80B parameter native multimodal image g
> L39: - **Multiple Loading Modes**: Full BF16, INT8/NF4 Quantized, Single GPU, Multi-GPU

## 星数曲线

```mermaid
xychart-beta
    title "EricRollei/Comfy_HunyuanImage3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `342781754743` · [字段定义](../../DATASET.md)*
