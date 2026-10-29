# naomifridman/BreastDCEDL

⭐ 36 · Jupyter Notebook · NOASSERTION · 推送 2026-07-01 · [GitHub](https://github.com/naomifridman/BreastDCEDL) · [官网](https://zenodo.org/records/15627233) · 个人维护

**2,072 例乳腺癌 DCE-MRI 深度学习数据集（含基准任务）**

由 I-SPY1、I-SPY2 与 Duke 三个临床队列整合的乳腺癌治疗前 3D DCE-MRI 数据集，共 2,072 名患者。提供两个版本：MinCrop 版含每例 3 个肿瘤中心时相（裁剪至 256×256），全版本保留原始时空信息（约 202GB）。数据为保留原始 DICOM 强度值的 3D NIfTI 体积，附肿瘤分割与统一 CSV 临床元数据，并给出 pCR/HER2/HR 三个分层抽样的基准分类任务及数据划分。示例代码基于 Python/PyTorch，数据可从 Zenodo 与 TCIA 获取，许可需参照原始数据源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,072 例患者，覆盖 I-SPY1/I-SPY2/Duke 三个临床队列
- 保留原始 DICOM 强度值的 3D NIfTI 体积与肿瘤分割标注
- pCR/HER2/HR 三个基准分类任务与训练/验证/测试划分
- 提供 Colab demo 与 ViT pCR 预测示例 notebook

## 适用场景

- 下载乳腺癌 DCE-MRI 数据训练 pCR/HER2 预测模型
- 在统一基准划分上对比影像分类方法
- 研究造影增强动力学与预处理方法（Full 版本）

## 场景标签

 · 领域:医学影像/肿瘤研究

## 证据(README 行号)

> L3: Deep learning-ready dataset of pretreatment 3D dynamic contrast-enhanced MRI (DCE-MRI) scans from **2,072 breast can
> L19: The MinCrop version provides three methodicaly selected DCE-MRI time points (pre-contrast, early post-contrast, lat

## 星数曲线

```mermaid
xychart-beta
    title "naomifridman/BreastDCEDL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4e85c3e74fc5` · [字段定义](../../DATASET.md)*
