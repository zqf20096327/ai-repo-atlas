# ModelTC/ComfyUI-Lightx2vWrapper

⭐ 95 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ModelTC/ComfyUI-Lightx2vWrapper) · 组织维护 · 中文 README

**ComfyUI 自定义节点：封装 LightX2V 做视频生成**

将 LightX2V 视频推理封装为 ComfyUI 自定义节点的封装层：提供 8 类节点，包括推理配置（T2V/I2V）、TeaCache 加速（阈值越低加速越多）、int8/fp8 量化（后端 vllm/sgl/q8f 自动检测）、显存优化（CPU offload 等）、轻量 VAE、LoRA 链式加载，以及配置合并与模块化推理节点。支持 wan2.1、hunyuan 架构，模型从 Hugging Face lightx2v 组织下载后放入 ComfyUI/models/lightx2v/ 目录。以 git clone 源码方式安装到 custom_nodes，附带示例工作流 JSON。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生视频（T2V）与图生视频（I2V）双模式
- TeaCache 加速、int8/fp8 量化与 CPU offload 显存优化
- LoRA 链式加载，支持 wan2.1、hunyuan 架构
- 模块化节点系统，8 类节点可组合配置

## 适用场景

- 在 ComfyUI 工作流中用 LightX2V 生成视频
- 低显存环境下通过量化与 offload 运行大模型视频生成
- 通过链式 LoRA 定制视频风格

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: A ComfyUI custom node wrapper for LightX2V, enabling modular video generation with advanced optimization features.
> L12: - **Text-to-Video (T2V) and Image-to-Video (I2V)**: Support for both generation modes

## 星数曲线

```mermaid
xychart-beta
    title "ModelTC/ComfyUI-Lightx2vWrapper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-24 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1ddeeeff23d6` · [字段定义](../../DATASET.md)*
