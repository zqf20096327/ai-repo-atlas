# MagnumVD/RotoForge-AI

⭐ 115 · Python · NOASSERTION · 推送 2026-09-30 · [GitHub](https://github.com/MagnumVD/RotoForge-AI) · [官网](https://ko-fi.com/s/5025cf0a06) · 个人维护

**Blender 机器学习辅助动态遮罩（roto）生成扩展**

基于 SAM-HQ 实现的 Blender 扩展，通过用户在图像编辑器中绘制的遮罩样条（闭合区域或正/负提示点）作为提示，为图像和视频生成灰度位掩码，并提供手动跟踪、逐帧绘制修正等调整手段。依赖约 8GB 数据，通过扩展内置按钮自动下载安装；支持 NVIDIA CUDA、AMD ROCm（仅 Linux）及 CPU。需 Blender 4.2+，以 GPL-3.0 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SAM-HQ 驱动的图像/视频位掩码生成
- 以样条（闭合区域/正负提示点）作为提示方式
- 依赖约 8GB，扩展内一键自动安装
- 提供 light/base/large/huge 四档模型与显存占用参考数据

## 适用场景

- 在 Blender 中为视频快速生成动态遮罩（rotoscoping）
- 逐帧或用绘制模式修正不准确的遮罩
- 无 GPU 时用 CPU 模式运行遮罩生成

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7:  RotoForge is an implementation of SAM-HQ + some other custom stuff to make rotoscoping fast af
> L26: Rotoforge generates bitmasks (grayscale images which show how much a pixel is part of a mask) based on prompts whic

## 星数曲线

```mermaid
xychart-beta
    title "MagnumVD/RotoForge-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-30 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fe7ad8751de0` · [字段定义](../../DATASET.md)*
