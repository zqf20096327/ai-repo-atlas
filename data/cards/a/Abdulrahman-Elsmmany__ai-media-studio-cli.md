# Abdulrahman-Elsmmany/ai-media-studio-cli

⭐ 19 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/Abdulrahman-Elsmmany/ai-media-studio-cli) · 个人维护

**命令行多模态 AI 媒体生成工具：调用 Google 模型生成视频等**

Python 编写的 CLI 工具，通过 Google Veo 2.0/3.0 模型按文本提示词生成 5-8 秒视频，支持视频续接、多种画面比例与并发下载；Imagen 图像生成与 MusicLM 音乐生成分别标记为 coming soon 与 planned，尚未可用。提供交互式终端界面与自动按媒体类型归档的下载管理（videos/images/audios 目录）。运行需配置 Google Cloud 项目、API key 及一个 GCS 存储桶（视频生成中转用），通过 git clone 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 集成 Google Veo 2.0/3.0，支持视频续接与图生视频
- 交互式终端界面：模型选择、参数配置、提示词指南
- 生成内容自动按类型归档，支持 20+ 媒体格式与并发下载
- Imagen 与 MusicLM 集成尚未发布（coming soon/planned）

## 适用场景

- 用一条命令按提示词生成短视频素材
- 批量生成并自动归档媒体文件
- 通过交互模式浏览模型能力并配置生成参数

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L8: *Generate videos, images, and music with Google's AI models using simple text prompts*
> L94: - **Google Veo 2.0 & 3.0** models
> L125: ai-studio generate video -p "a majestic eagle soaring over mountains"

## 星数曲线

```mermaid
xychart-beta
    title "Abdulrahman-Elsmmany/ai-media-studio-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `799f30873766` · [字段定义](../../DATASET.md)*
