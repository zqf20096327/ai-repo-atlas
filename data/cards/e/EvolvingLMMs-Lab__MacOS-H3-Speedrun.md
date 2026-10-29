# EvolvingLMMs-Lab/MacOS-H3-Speedrun

⭐ 25 · Python · 推送 2026-08-21 · [GitHub](https://github.com/EvolvingLMMs-Lab/MacOS-H3-Speedrun) · 组织维护 · 中文 README

**Apple Silicon 上运行 MiniMax-H3 音画同步视频生成的 ComfyUI 工作流套装**

面向 Apple Silicon Mac 用户的 MiniMax-H3 视频生成方案：提供 bootstrap.py 安装器，按统一内存档位（24–192 GB）自动选择模型与工作流（MLX 快档或 ComfyUI BF16 标准图），支持 Turbo4/Turbo8/Full20 三种生成模式及 SolAttn、FBC、strict-staged 等机制，从 Prompt 直接生成含原生音频的 MP4。附带内存峰值与 M3 Ultra 实测生成时间数据、社区 LoRA 转换路径说明与 Prompt 指南。需自备 ComfyUI 环境，24 GB 档需约 110–120 GB 临时磁盘空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按统一内存（24–192 GB）自动选择模型与工作流的 bootstrap.py 安装器
- Turbo4/Turbo8/Full20 三种生成模式，输出含原生音频的 MP4
- MLX 与 ComfyUI BF16 两条执行路径，各档位给出峰值内存与实测时间
- 社区 LoRA/Checkpoint 的兼容性说明与转换路径

## 适用场景

- 在我的 Mac 上本地生成音画同步短片
- 按内存档位选择合适的视频生成工作流
- 用 480p 快速草稿确定主体与镜头后提高分辨率出成品

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L38: /path/to/ComfyUI/.venv/bin/python bootstrap.py --comfyui /path/to/ComfyUI --memory-tier auto
> L41: 1. 安装器按统一内存下载所需节点、模型和工作流。
> L42: 2. PyTorch工作流使用 `python main.py --use-pytorch-cross-attention` 重启ComfyUI。

## 星数曲线

```mermaid
xychart-beta
    title "EvolvingLMMs-Lab/MacOS-H3-Speedrun 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f0198604e4de` · [字段定义](../../DATASET.md)*
