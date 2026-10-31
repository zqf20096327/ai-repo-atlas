# Nambekai/dangerous-person-detection-yolo11

⭐ 27 · Python · AGPL-3.0 · 推送 2026-08-25 · [GitHub](https://github.com/Nambekai/dangerous-person-detection-yolo11) · [官网](https://drive.google.com/drive/folders/1m-BzFvQwwWzvTCXApwJftQU3tRt0CmCC?usp=drive_link) · 个人维护

**YOLO11 毕业论文原型：检测公共区域中与潜在危险物同行的人**

基于 YOLO11 的学术研究原型（VNUHCM-University of Science 本科毕业论文），在公共区域图像中定位与潜在危险物体同现的人员，使用 normal_person 与 potentially_dangerous_person 两个上下文类别。比较五种 YOLO11 变体后选定 YOLO11s（mAP50 0.80），数据集含 3,140 张图像、10,595 个标注实例。提供推理与训练脚本、模型权重下载，并声明保留原始 notebook 与随机种子缺失，不保证精确数值复现；附越南语论文 PDF 与负责任使用指引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个上下文类别定位人而非仅物体
- 五种 YOLO11 变体的测试集对比与训练记录
- 3,140 图像 / 10,595 实例的 YOLO 格式数据集（CC BY 4.0）
- 提供推理、训练重建脚本与复现性说明、伦理指引

## 适用场景

- 在公共区域图像/视频中定位疑似携带危险物品的人员供人工复核
- 复现或审阅论文的模型对比与训练配置
- 作为公共安全领域目标检测研究的参考资料

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: This graduation-thesis repository studies YOLO11-based detection of people who appear with a potentially dangerous 
> L13: The study compared YOLO11n, YOLO11s, YOLO11s with a recorded preprocessing configuration, YOLO11m, and YOLO11l. YOL

## 星数曲线

```mermaid
xychart-beta
    title "Nambekai/dangerous-person-detection-yolo11 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fa539fd16e83` · [字段定义](../../DATASET.md)*
