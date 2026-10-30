# LevelPixel/ComfyUI-LevelPixel-Advanced

⭐ 22 · Python · GPL-3.0 · 推送 2026-03-21 · [GitHub](https://github.com/LevelPixel/ComfyUI-LevelPixel-Advanced) · [官网](https://www.patreon.com/c/LevelPixel) · 组织维护

**ComfyUI 高级节点包：运行 GGUF 格式 LLM/VLM 模型**

Level Pixel 维护的 ComfyUI 节点包，收集在 ComfyUI 工作流中运行 GGUF 格式 LLM 与 VLM 模型的节点：Multimodal Generator（基于 GGUF 多模态模型，支持 Qwen2.5-VL）、LLaVa/LLM 文本生成节点（生成后卸载模型）、WD/RAM 自动打标器、三种图像背景移除节点（RMBG/BiRefNet/rembg）。核心依赖 llama-cpp-python，需预装 CUDA 12.9、Visual Studio 2022 与 CMake 以编译，通过 ComfyUI Manager 或 git clone 到 custom_nodes 安装。部分核心功能取自 ComfyUI_VLM_nodes 等项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Multimodal Generator 节点支持 GGUF 格式 Qwen2.5-VL 多模态模型
- LLM/LLaVa 文本生成节点在生成后自动从显存卸载模型
- WD tagger 与 RAM++ 图像自动打标节点
- 三种背景移除节点（RMBG-2.0、BiRefNet、rembg）

## 适用场景

- 在 ComfyUI 工作流中直接运行 GGUF 格式的本地 LLM/VLM
- 为图像自动生成标签用于数据集或提示词
- 在显存有限的工作流中切换使用 LLM 与图像模型

## 场景标签

`推理引擎` `多模态` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: The purpose of this package is to collect the most necessary and atomic nodes for working with LLM and VLM models wi
> L35: Before running ComfyUI with this node package, you should make sure that you have the following programs and librar

## 星数曲线

```mermaid
xychart-beta
    title "LevelPixel/ComfyUI-LevelPixel-Advanced 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d5aca3fb3f72` · [字段定义](../../DATASET.md)*
