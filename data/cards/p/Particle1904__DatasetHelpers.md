# Particle1904/DatasetHelpers

⭐ 229 · C# · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Particle1904/DatasetHelpers) · 个人维护

**图像-文本数据集预处理桌面工具：选图、裁剪、打标一体化**

面向机器学习训练数据准备的 C# 桌面工具集：提供图库浏览与批量筛选、低分辨率图剔除、保持宽高比的缩放（可条件锐化）、拖框手动裁剪与基于 YoloV4 检测人物的内容感知自动裁剪（输出 512/640/768 方图），以及使用 WD 1.4 SwinV2 Tagger V2 等四种模型生成 booru 风格标签写入 .txt/.caption 文件。另有 .txt 批量文本处理、子集抽取、提示词生成与元数据查看。可从 releases 下载或用 .NET 8 自行构建，需另行下载模型文件；部分功能（元数据查看）仅限 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 AI 模型自动打标，可多模型追加写入 .txt
- YoloV4 人物检测驱动的内容感知自动裁剪，输出三种方图尺寸
- 批量图库管理：选图、剔除低分辨率、备份
- 批量文本处理：标签增删替换、去冗余、合并相似标签

## 适用场景

- 给 Stable Diffusion 类训练准备图像与标签数据集
- 批量整理既有 .txt/.caption 标注文件
- 从大数据集按关键词抽取训练子集

## 场景标签

 · 领域:机器学习/数据集工具

## 证据(README 行号)

> L1: # Dataset Processor - All-in-one Tools
> L5: Dataset Processor Tools is a versatile toolkit designed to streamline the processing of image-text datasets for mach
> L11: The toolkit also offers advanced content-aware smart cropping. Leveraging the YoloV4 model for object detection, it

## 星数曲线

```mermaid
xychart-beta
    title "Particle1904/DatasetHelpers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 228 --> 230
    line [229, 229]
```

2026-10-18 229 → 2026-10-30 229（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8cf93e8c6dcb` · [字段定义](../../DATASET.md)*
