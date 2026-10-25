# Okohedeki/scroll-studio

⭐ 49 · Python · AGPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/Okohedeki/scroll-studio) · [官网](https://okohedeki.github.io/scroll-studio-showcase/) · 个人维护

**从单个 YAML 文件生成交互式滚动叙事网站的开源设计工具**

面向建站与内容创作的开源设计工具：输入一个 YAML 配置，在本地生成包含电影式镜头、实时 3D、图表、地图的滚动驱动网站，输出为纯 HTML/CSS/JS 静态文件可任意托管。图像与视频全部由本地开源模型生成（Z-Image、Qwen-Image-Edit、LTX-2.3、Wan 2.2 等），无需 API key。提供 CLI 工作流（storyboard/build/inspect/publish）与 Studio UI；生成影片等功能需 ComfyUI 与 24GB GPU，纯 3D 场景仅需 Python。附带 MCP server，可由 Claude 等 agent 驱动完整流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 YAML 文件生成交互式滚动网站，输出静态 HTML/CSS/JS
- 图像与视频用本地开源模型生成，无需 API key
- 32 种页面风格、六种美术方向、storyboard 先行的工作流
- 提供 MCP server 供 Claude 等编码 agent 驱动

## 适用场景

- 为自己的产品或品牌制作滚动驱动的落地页
- 在本地 GPU 上生成电影式视觉内容并发布为静态网站
- 让 Claude 通过 MCP 代为执行建站流程

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L28: Every image and video is made with open models on your machine (Z-Image, Qwen-Image-Edit, LTX-2.3, Wan 2.2, SeedVR2
> L68: |Photo parallax, product sequences, inside the product|Runs on the CPU; Blender and a GPU make it fast|
> L75: Open the repo in Claude Code and ask for a site. The `scroll-studio` MCP server (`.mcp.json`) gives Claude every

## 星数曲线

```mermaid
xychart-beta
    title "Okohedeki/scroll-studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-25 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `29ac8d3bd7a3` · [字段定义](../../DATASET.md)*
