# mikeknapp/candy-machine

⭐ 55 · TypeScript · NOASSERTION · 推送 2026-04-06 · [GitHub](https://github.com/mikeknapp/candy-machine) · 个人维护

**给 Stable Diffusion/Lora 训练者手动标注小图像数据集的 Web 工具**

本地运行的 Web 界面图像标注工具，面向为训练 Stable Diffusion LoRA / DreamBooth 模型准备小型数据集（<1k 张）的用户：生成 .txt caption 文件，支持可自定义标签布局、占位符模板、内置裁剪/旋转/翻转编辑、自动转换图片格式为 .png。创建项目时可用 wd-v1-4-convnext-tagger.v3 提供标签建议（GPU 路径需 CUDA 12.2 与 cuDNN 8.x）。全部数据留在本机不外传；个人非商业使用免费，商业使用需联系作者购买付费许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 生成 .txt caption 文件，支持占位符标签模板与自定义布局
- 内置图片编辑（裁剪、旋转、水平翻转）与格式自动转换
- 基于 wd-v1-4-convnext-tagger.v3 的标签建议
- 完全本地运行，不向第三方传输信息

## 适用场景

- 为训练 LoRA / DreamBooth 模型手动标注小数据集
- 在标注的同时裁剪、旋转和转换训练图片
- 保持数据集标签的一致性以提升训练效果

## 场景标签

 · 领域:图像/生成式模型数据工具

## 证据(README 行号)

> L3: _Web-Based Manual Image Tagger for Training Custom Stable Diffusion LORAs & DreamBooth Models_
> L7: Candy Machine is a nascent image tagger for _manually tagging_ small datasets (< 1k images) with `.txt` caption file
> L15: - **Tag suggestions** using `wd-v1-4-convnext-tagger.v3` when creating a new project

## 星数曲线

```mermaid
xychart-beta
    title "mikeknapp/candy-machine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-24 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9f8481e8a59d` · [字段定义](../../DATASET.md)*
