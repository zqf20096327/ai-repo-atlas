# serhaturtis/TOOL-FastBatchImageCrop

⭐ 34 · Python · MIT · 推送 2026-01-28 · [GitHub](https://github.com/serhaturtis/TOOL-FastBatchImageCrop) · 个人维护

**给数据集制作者的批量图像裁剪 GUI 工具**

基于 Python 的桌面 UI 工具，用于从图片文件夹和视频中批量裁剪图像以制作训练数据集：支持自定义宽高比裁剪、自动缩放、视频抽帧、播放中裁剪；裁剪时可输入类别名（输出到不同类别目录）和图像描述（生成同名 txt 标签文件），面向 stable-diffusion 等图像分类/生成模型的数据准备场景。运行方式为 pip 安装依赖（pillow、opencv、pyyaml）后执行 python main.py，仅支持源码运行，无打包安装包。

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

- 从视频与图片文件夹批量裁剪，支持自定义宽高比与自动缩放
- 按类别名分目录保存，裁剪同时生成 txt 标签文件
- 视频抽帧与播放中实时裁剪
- 快捷键旋转图像与切换下一张

## 适用场景

- 为图像分类或 stable-diffusion 训练准备裁剪好的图片数据集
- 从视频中抽帧并批量裁剪出目标区域
- 裁剪同时打类别标签与图像描述

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # TOOL-FastBatchImageCrop
> L11: - Save cropped images to different class folders

## 星数曲线

```mermaid
xychart-beta
    title "serhaturtis/TOOL-FastBatchImageCrop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bbec7857b837` · [字段定义](../../DATASET.md)*
