# spawner1145/comfyui-kaloscope

⭐ 109 · Python · GPL-3.0 · 推送 2026-10-06 · [GitHub](https://github.com/spawner1145/comfyui-kaloscope) · 个人维护 · 中文 README

**画风分类与聚类工具：识别图片风格并输出特征与关系图**

基于 LSNet 与 DINOv3 模型的画风分析工具，支持 ComfyUI 插件、WebUI 插件和独立启动三种运行方式。功能包括单图画风分类（画师标签匹配）、多图风格聚类、多层特征提取（patch tokens、空间特征图、中间层特征等）以及关系网络、距离热图、聚类散点等 19 种分析图表。提供 Gradio 界面、命令行推理与 /kaloscope/v1/ HTTP API。模型权重需从 Hugging Face 或 ModelScope 单独下载放置到 models/kaloscope 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LSNet 与 DINOv3 模型的画风分类与相似标签匹配
- KMeans/DBSCAN/层次聚类与 PCA/t-SNE 等多种关系制图
- 19 种特征输出类型（含中间层、patch tokens、空间特征图）
- ComfyUI 节点 + WebUI 界面 + 命令行 + HTTP API 四种使用方式

## 适用场景

- 识别一幅作品的画风并匹配相似画师标签
- 批量整理图库，按风格特征聚类分组
- 提取图片特征供下游分析节点或脚本使用

## 场景标签

 · 领域:图像分析/AIGC 工具

## 证据(README 行号)

> L15: 支持 *LSNet* 和 *DINOv3* 模型，本工具聚焦以下场景：
> L17: 1. **画风分类**：识别单幅作品的风格属性，完成风格相似的标签匹配

## 星数曲线

```mermaid
xychart-beta
    title "spawner1145/comfyui-kaloscope 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 107 --> 110
    line [109, 108, 109, 109]
```

2026-10-18 109 → 2026-10-23 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3953e5218b09` · [字段定义](../../DATASET.md)*
