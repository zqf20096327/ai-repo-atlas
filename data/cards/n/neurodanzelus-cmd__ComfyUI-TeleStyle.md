# neurodanzelus-cmd/ComfyUI-TeleStyle

⭐ 45 · Python · Apache-2.0 · 推送 2026-02-03 · [GitHub](https://github.com/neurodanzelus-cmd/ComfyUI-TeleStyle) · 个人维护

**ComfyUI 节点：基于 Wan2.1-T2V 的视频风格迁移**

TeleStyle 的非官方 ComfyUI 节点实现，聚焦视频风格迁移：使用 Wan2.1-T2V 架构与 TeleStyle 自定义权重，去除了原仓库的图像编辑组件（Qwen 权重），改用预计算风格嵌入（prompt_embeds.pth）以省去外部文本编码节点。支持 Flash Attention 2 与 SageAttention 加速，提供 fast_mode 内存管理与低显存 offloading 选项。要求 6GB 显存与约 6GB 磁盘空间，权重首次运行时自动下载，或从 Hugging Face 获取。以 git clone 方式安装到 custom_nodes 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Wan2.1-T2V 架构的视频风格迁移节点
- 使用预计算风格嵌入（prompt_embeds.pth），无需外部文本编码节点
- 支持 Flash Attention 2 与 SageAttention 加速
- fast_mode 内存管理与低显存 offloading 选项

## 适用场景

- 在 ComfyUI 工作流中用参考图对输入视频做风格迁移
- 显存有限（6GB 起）的环境下运行视频风格迁移
- 需要加速推理的视频生成任务

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: An unofficial, streamlined, and highly optimized ComfyUI implementation of TeleStyle.
> L9: This node is specifically designed for **Video Style Transfer** using the **Wan2.1-T2V** architecture and TeleStyle 

## 星数曲线

```mermaid
xychart-beta
    title "neurodanzelus-cmd/ComfyUI-TeleStyle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `92b89cc4132f` · [字段定义](../../DATASET.md)*
