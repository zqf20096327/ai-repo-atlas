# Saganaki22/ComfyUI-VDN-H3

⭐ 241 · Python · Apache-2.0 · 推送 2026-09-12 · [GitHub](https://github.com/Saganaki22/ComfyUI-VDN-H3) · [官网](https://huggingface.co/drbaph/vdn-minimax-h3-int8-convrot-comfyui) · 个人维护 · 中文 README

**把 MiniMax-H3 的 Video Delta Net 混合注意力移植为 ComfyUI 原生节点**

面向 ComfyUI 用户的模型运行补丁：将 OpenVDN/vdn-minimax-h3 的混合注意力（近邻帧精确 softmax + 远程时序走线性 Delta Attention 分支）以运行时 patch 形式移植到 ComfyUI 原生 MiniMax-H3 上，不改核心文件。官方实现依赖 8×B200、FA4 与 Triton 内核，此移植用可移植 PyTorch 等价实现替代，无新增 Python 依赖；提供 merge/bypass 适配器模式、stream/cache_gpu 显存策略、INT8 分支等选项。README 明确声明这是实验性移植，计算与显存开销高于 int8 融合注意力路线，不推荐显存受限用户使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 窗口 softmax + Video Delta Attention 线性分支，注意力开销随片长线性增长
- 相对官方数据中心栈（8×B200/FA4/FP8/Triton）的可移植 PyTorch 移植，无新增依赖
- 对官方实现做过单元测试校验（46-51 项回归测试通过）
- 提供 merge/bypass 适配器模式与 stream/cache_gpu 显存策略

## 适用场景

- 在 ComfyUI 中用自己的 GPU 运行 VDN-H3 架构做文本生视频
- 长片/高分辨率视频生成时降低注意力开销的二次增长
- 对窗口参数、锚点帧等做消融实验

## 场景标签

`视频生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L7: Video Delta Net hybrid attention for MiniMax-H3 as a native ComfyUI node. Nearby
> L17: This package is a **port, not a fork**: it reproduces the official hybrid-attention
> L18: math on ComfyUI's native MiniMax-H3 model as runtime model patches. No ComfyUI core

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-VDN-H3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 240 --> 242
    line [241, 241]
```

2026-10-18 241 → 2026-10-22 241（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fbd870af7949` · [字段定义](../../DATASET.md)*
