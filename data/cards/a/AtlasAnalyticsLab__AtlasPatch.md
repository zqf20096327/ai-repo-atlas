# AtlasAnalyticsLab/AtlasPatch

⭐ 65 · Python · NOASSERTION · 推送 2026-05-27 · [GitHub](https://github.com/AtlasAnalyticsLab/AtlasPatch) · [官网](https://atlasanalyticslab.github.io/AtlasPatch/) · 组织维护

**病理全切片图像预处理工具：组织分割与高通量切块特征提取**

面向计算病理学的全切片图像（WSI）预处理 Python 库与 CLI：使用 SAM2 进行组织分割，提取切块坐标与特征，并支持切片级（TITAN/PRISM）与患者级（MOOZY）嵌入生成。提供 4 个可独立使用的检查点命令（detect-tissue/segment-and-get-coords/process/encode-slide/encode-patient），内置数十种视觉与病理专用特征编码器，并支持自定义编码器插件。运行前需安装 OpenSlide 系统库，SAM2 为必需依赖；部分编码器需 Hugging Face 访问审批与 HF_TOKEN。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SAM2 组织分割输出掩码、叠加与轮廓可视化
- 单条命令产出每切片 H5（坐标+特征）并支持切片级/患者级嵌入
- 内置自然图像与病理专用视觉/CLIP 编码器数十种（UNI/Virchow/GigaPath/DINOv3 等）
- --feature-plugin 机制支持接入自定义编码器

## 适用场景

- 对病理 WSI 批量做组织检测与切块提取
- 为下游病理模型生成切片级或患者级嵌入
- 对比测试自研编码器与内置编码器的特征输出

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: # AtlasPatch: Efficient Tissue Detection and High-throughput Patch Extraction for Computational Pathology at Scale

## 星数曲线

```mermaid
xychart-beta
    title "AtlasAnalyticsLab/AtlasPatch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-29 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `10287d66a04d` · [字段定义](../../DATASET.md)*
