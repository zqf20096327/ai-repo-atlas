# junforge-dev/voxplane

⭐ 307 · Python · 推送 2026-11-23 · [GitHub](https://github.com/junforge-dev/voxplane) · [官网](https://junforge-dev.github.io/voxplane/) · 组织维护 · 中文 README

**跨平台 DICOM 阅片工作台：为 CT/MR/PET 提供重建、融合与本地 AI 分割**

面向 CT、MR 与 PET 的桌面 DICOM 工作台，功能覆盖本地与压缩包影像导入、PACS（DICOMweb 与 DIMSE）查询回传、2D 阅片与多序列对比、MPR/CPR/3D/4D 重建、PET/CT 融合、测量标注、阈值分割与 VOI、CT 水模 QA/MTF/FWHM 分析，以及 SEG/SR/NRRD/PDF 等导出。AI 部分为本地调用 TotalSegmentator 做 CT 多器官自动分割，结果可叠加、精修与保存；需另行安装 TotalSegmentator 环境并按 CUDA/Apple MPS/CPU 选择推理后端。提供 macOS（含 Apple Silicon）与 Windows 安装版/便携版，源码可用 uv 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地调用 TotalSegmentator 做 CT 多器官自动分割，结果可叠加与精修
- 支持 DICOMweb（QIDO-RS/WADO-RS）与传统 DIMSE（C-ECHO/C-FIND/C-MOVE）PACS 接入
- MPR/CPR、体绘制 3D、CT 多时相 4D 与 PET/CT 融合
- 测量与分割可导出 DICOM SEG/SR、NRRD、CSV/PDF

## 适用场景

- 在本地桌面完成 CT/MR/PET 的阅片与三维重建
- 连接院内 PACS 查询并下载序列进行阅片与测量
- 用 TotalSegmentator 自动分割 CT 器官后手动精修并导出 SEG/NRRD
- 做 CT 水模 QA、点源 MTF 与层厚分析并生成 PDF 报告

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: 面向 CT、MR 与 PET 的跨平台 DICOM 工作台，集阅片、三维重建、影像融合与测量分割于一体。支持 **基于 TotalSegmentator 的本地 AI 自动分割**，结果可直接查看、精修和保存。
> L40: |本地 AI|TotalSegmentator CT 多器官快速分割；器官搜索与选择、结果叠加、精修、撤销与保存。|
> L66: - **本机推理**：连接已有 TotalSegmentator 环境，计算当前时相的完整 CT；支持按环境选择 CUDA、Apple MPS 或 CPU。

## 星数曲线

```mermaid
xychart-beta
    title "junforge-dev/voxplane 星数(近 4 点)"
    x-axis ["2026-11-11", "2026-11-16", "2026-11-20", "2026-11-27"]
    y-axis "stars" 305 --> 309
    line [306, 307, 308, 307]
```

2026-11-11 306 → 2026-11-27 307（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `f86f8e4fb1c6` · [字段定义](../../DATASET.md)*
