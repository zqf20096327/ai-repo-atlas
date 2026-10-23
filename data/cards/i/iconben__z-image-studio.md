# iconben/z-image-studio

⭐ 128 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/iconben/z-image-studio) · 个人维护 · 中文 README

**Z-Image-Turbo 文生图模型的本地 CLI/WebUI/MCP 工具**

围绕通义 Tongyi-MAI/Z-Image-Turbo 文生图模型（含量化变体，经 diffusers 加载）的三合一本地工具：zimg CLI 直接在终端生图、FastAPI Web UI 提供交互式生成（多语言、历史浏览、LoRA 管理、按硬件推荐模型精度）、并可作为 MCP Server 被 AI agent 调用（stdio/SSE/Streamable HTTP 三种传输）。支持 CUDA/ROCm/Intel XPU/Apple MPS，无 GPU 时回退 CPU，自动显存管理防止 OOM。单次生成可叠加至多 4 个 LoRA。提供 pip/uv、Windows 安装包与 Docker 镜像；Windows 安装包要求 8GB+ 内存（全精度建议 16GB+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI/WebUI/MCP Server 三种使用方式，MCP 支持 stdio/SSE/Streamable HTTP
- CUDA/ROCm(AMD Linux)/Intel XPU/Apple Silicon(MPS) 加速，无 GPU 回退 CPU
- Web UI 按 RAM/VRAM 动态推荐模型精度，含注意力切片自动管理
- 单次生成可叠加至多 4 个 LoRA 并分别设强度

## 适用场景

- 在本地终端或网页上用 Z-Image-Turbo 模型生成图片
- 让 Claude Desktop 等 AI agent 通过 MCP 调用生图能力
- 显存有限的机器上用量化模型与自动降载生图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L17: A Cli, a webUI, and a MCP server for the **Z-Image-Turbo** text-to-image generation model (`Tongyi-MAI/Z-Image-Turb
> L25:  * **CLI**: Fast, direct image generation from the terminal.
> L49: * **MCP Server (stdio + SSE + Streamable HTTP)**: Expose tools for image generation, listing models, and viewing hi

## 星数曲线

```mermaid
xychart-beta
    title "iconben/z-image-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 127 --> 129
    line [128, 128]
```

2026-10-18 128 → 2026-10-23 128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `697e9d7a8294` · [字段定义](../../DATASET.md)*
