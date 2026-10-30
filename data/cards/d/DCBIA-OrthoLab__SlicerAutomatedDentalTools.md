# DCBIA-OrthoLab/SlicerAutomatedDentalTools

⭐ 182 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools) · 组织维护

**3D Slicer 牙科/颅面自动分析扩展：分割、定位点、定向**

面向 3D Slicer 的医学影像扩展，通过图形界面让无编程背景的正畸/牙科用户在 CBCT 与口内扫描（IOS）上执行机器学习驱动的自动分割（AMASSS）、 landmark 识别（ALI-CBCT/ALI-IOS）、自动定向（ASO）、配准（AReg）等任务，另有批量处理、医学文档匿名化、面部不对称分类等约 17 个 GUI 模块与对应 CLI 模块，并包含用本地 LLM 通过自然语言调度各模块的 Agent 助手。训练模型需手动下载；建议 12GB 内存；兼容 3D Slicer 5.6.1 稳定版与 5.7.0 nightly。

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

- CBCT/IOS 上的自动分割与 landmark 识别（模型可由模块内按钮下载）
- 单文件或整文件夹批量处理，支持输出分组与自定义输出路径
- 自然语言驱动的 Agent 模块（本地 LLM 路由请求到各工具）
- GUI 模块配套提供 CLI 版本（Advanced 类别）

## 适用场景

- 对 CBCT 做多解剖结构自动分割并生成表面模型
- 在 CBCT 或口内扫描上自动识别解剖标志点
- 批量定向、配准与裁剪整批患者扫描数据

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: Slicer automated dental tools is an extension that allows users to perform automatic **segmentation**, **landmark i
> L25: |AMASSS|Perform automatic segmentation of CBCT scan. AMASSS is an acronym for Automatic Multi-Anatomical Skull Stru
> L39: |Agent|AI assistant that runs the other modules from a natural-language request, using a local LLM.|

## 星数曲线

```mermaid
xychart-beta
    title "DCBIA-OrthoLab/SlicerAutomatedDentalTools 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 180 --> 183
    line [181, 182, 182]
```

2026-10-18 181 → 2026-10-30 182（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ec7ad4fe23ab` · [字段定义](../../DATASET.md)*
