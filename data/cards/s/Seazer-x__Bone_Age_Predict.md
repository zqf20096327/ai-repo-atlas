# Seazer-x/Bone_Age_Predict

⭐ 15 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/Seazer-x/Bone_Age_Predict) · 个人维护 · 中文 README

**从手部 X 光片估计骨龄的开源 YOLOv5 + RUS-CHN 工具**

面向科研、教学与可复现实验的骨龄估计项目：用 YOLOv5 检测手骨区域，选取 13 个 RUS-CHN 评分区，9 个 YOLOv5 分类模型估计成熟度分期，换算 CHN 总分与估计骨龄。提供本地 Streamlit 界面（可调置信度与 IoU 阈值）和托管在 Hugging Face 的 Gradio + ZeroGPU 演示。附带针对标注数据集的评测脚本，输出 MAE/RMSE/命中率与 bootstrap 置信区间。明确声明仅供研究与教育用途，非医疗器械且未做临床验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv5 检测 + 9 个分类模型的 RUS-CHN 骨龄估计流水线
- 本地 Streamlit 应用，可调置信度与 IoU 阈值
- 评测脚本输出 MAE/RMSE/±0.5 与 ±1.0 年命中率及 bootstrap 95% CI
- Hugging Face Space 托管 Gradio + ZeroGPU 演示，权重来自 v1.0.0 release

## 适用场景

- 科研或教学中从手部 X 光片复现骨龄估计流程
- 在标注数据集上批量评测骨龄预测误差
- 本地部署处理敏感医学影像数据

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L11: Open-source **YOLOv5 + RUS-CHN bone age estimation** from hand X-ray images, with a local Streamlit app and a hoste
> L26: - Uses 9 YOLOv5 classification models to estimate maturation stages.
> L27: - Converts stage scores into a CHN total score and estimated bone age.

## 星数曲线

```mermaid
xychart-beta
    title "Seazer-x/Bone_Age_Predict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `7e600244027a` · [字段定义](../../DATASET.md)*
