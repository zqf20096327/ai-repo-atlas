# haranrk/DigiPathAI

⭐ 76 · JavaScript · MIT · 推送 2026-02-20 · [GitHub](https://github.com/haranrk/DigiPathAI) · 个人维护

**病理全切片图像查看与癌症区域 AI 分割工具**

基于 openslide 构建的软件应用：提供全切片病理图像（WSI）的 Web 浏览器查看界面，并内置 AI 管道对癌变组织区域进行分割并以叠加层展示。仅运行 UI 只需 openslide 与 flask；完整 AI 管道需 GPU 及 pytorch、tensorflow-gpu（>=1.14,<2）等深度学习依赖。支持 pip 安装、CLI 启动本地服务器，并提供 Python API 调用分割功能。有 arXiv 论文（2001.00258）可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WSI 全切片图像浏览器查看
- AI 管道分割并叠加展示癌变组织区域
- pip 安装两种依赖模式（仅 UI / 完整 GPU 管道）
- 提供 Python API 调用分割功能

## 适用场景

- 查看和浏览超大病理全切片图像
- 在病理图像上运行癌症组织分割并以叠加层展示结果
- 在 Python 程序中调用分割 API 做病理分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: A software application built on top of openslide for viewing whole slide images (WSI) and performing pathological an
> L20: - State of the art cancer AI pipeline to segment and display the cancerous tissue regions
> L72: prediction = getSegmentation(img_path,

## 星数曲线

```mermaid
xychart-beta
    title "haranrk/DigiPathAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-25 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `950bd99442f3` · [字段定义](../../DATASET.md)*
