# Nuked88/ComfyUI-N-Nodes

⭐ 240 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/Nuked88/ComfyUI-N-Nodes) · 个人维护

**ComfyUI 自定义节点套件：视频处理与图像描述生成**

面向 ComfyUI 用户的自定义节点集合，共 14 类节点：视频加载/保存/帧插值（RIFE）、文件夹帧加载、整数/浮点/字符串变量节点、基于 Moondream 与 JoyTag 模型的图像描述与打标、外绘扩图增强和动态提示词等。1.2.0 版移除了 llama-cpp-python 集成及 GGUF 文本生成与 LLaVA 节点。模型（Moondream 约 3.72GB、JoyTag 约 0.37GB）在首次使用时自动从 Hugging Face 下载。支持 Windows/Linux 的 ComfyUI Python 环境，可经 ComfyUI Manager 或手动 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频帧提取、保存与 RIFE 帧插值节点
- 基于 Moondream/JoyTag 的图像描述与打标（模型自动下载）
- GPT Loader Simple 支持 CPU/GPU 层选择（gpu_layers）
- 提供旧工作流自动迁移脚本（migrate.bat / migrate.py）

## 适用场景

- 在 ComfyUI 工作流中加载、处理和保存视频
- 用视觉模型为图像生成描述或标签
- 通过帧插值提高视频帧率

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L4: A suite of custom nodes for ComfyUI that includes integer, string and float variable nodes, image-captioning nodes a
> L10: 1. Install **ComfyUI-N-Nodes** through ComfyUI Manager (recommended). For a manual install, clone `https://github.c

## 星数曲线

```mermaid
xychart-beta
    title "Nuked88/ComfyUI-N-Nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 239 --> 241
    line [240, 240]
```

2026-10-18 240 → 2026-10-28 240（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3bbdc4ea8ea3` · [字段定义](../../DATASET.md)*
