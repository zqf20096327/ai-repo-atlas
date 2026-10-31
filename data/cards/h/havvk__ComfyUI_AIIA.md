# havvk/ComfyUI_AIIA

⭐ 13 · Python · 推送 2026-02-24 · [GitHub](https://github.com/havvk/ComfyUI_AIIA) · 个人维护 · 中文 README

**ComfyUI 节点套件：媒体浏览器与长视频生成、数字人节点**

为 ComfyUI 提供的自定义节点集合，包含两大方向：一是 AIIA 媒体浏览器，集成在 ComfyUI 内的媒体文件管理中心，支持即时预览、元数据工具提示、虚拟滚动等，基于异步后端用 ffmpeg 与 Pillow 生成缩略图；二是面向大规模生成的节点，通过分批处理、逐帧释放、磁盘流式等策略解决长视频生成时的 OOM 问题，并封装 FLOAT、PersonaLive、EchoMimic V3、Ditto 等 Talking Head 模型为 ComfyUI 节点。安装方式为 git clone 到 custom_nodes 目录，视频功能强依赖 ffmpeg，部分节点需 SoX 与 NeMo 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AIIA 媒体浏览器：ComfyUI 内置文件中心，支持数千至数万文件的即时预览与排序筛选
- OOM 安全处理：分批 50 帧、逐帧释放、torch.cuda.empty_cache，支持 1500+ 帧视频
- 集成 FLOAT / PersonaLive / EchoMimic V3 / Ditto 等 Talking Head 模型节点
- JSON 预设系统自定义 FFmpeg 编码参数

## 适用场景

- 在 ComfyUI 内直接浏览管理 output 目录的生成结果并加载工作流
- 生成长音频口型同步视频而不出现内存溢出
- 用参考图与音频驱动数字人 Talking Head 视频生成

## 场景标签

`视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L5: 欢迎来到 AIIA Nodes for ComfyUI 仓库！这是一个旨在为 ComfyUI 提供一系列强大、直观且高度可定制的节点的集合。这些节点专注于简化复杂的工作流，并为创意工作者提供最大的灵活性。
> L157: 这组节点封装了先进的 **FLOAT** 模型，能够根据参考图像和音频生成高质量的口型同步影片。我们提供了两种模式，以应对不同长度的生成需求。

## 星数曲线

```mermaid
xychart-beta
    title "havvk/ComfyUI_AIIA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `05a3b2dfcb3c` · [字段定义](../../DATASET.md)*
