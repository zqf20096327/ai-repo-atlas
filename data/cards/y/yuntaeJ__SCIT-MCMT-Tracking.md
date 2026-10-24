# yuntaeJ/SCIT-MCMT-Tracking

⭐ 56 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/yuntaeJ/SCIT-MCMT-Tracking) · 个人维护

**CVPRW2023 多摄像头行人跟踪系统，利用未来轨迹预测**

NVIDIA AI City Challenge 第 7 届 Track1（多摄像头行人跟踪）的官方论文代码实现。流水线包含三个部分：基于 mmdetection YOLOX-X 的行人检测、yolov7-pose 的关键点检测、基于 Social-Implicit 的轨迹预测，并在单摄像头跟踪后做多摄像头关联。提供在 NVIDIA Omniverse 数据集上的预训练权重。运行环境为 2 块 NVIDIA A6000 GPU，通过 conda 环境文件与 setup.sh 脚本安装，以 shell 脚本运行单摄像头与多摄像头跟踪演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 行人检测（YOLOX-X）+ 关键点检测（yolov7-pose）+ 轨迹预测（Social-Implicit）三段流水线
- 提供 Track1 数据集上的预训练检测与轨迹预测权重
- 多摄像头关联使用 homography_list.pkl 单应矩阵

## 适用场景

- 复现 CVPRW2023 多摄像头行人跟踪论文结果
- 在 AI City Challenge Track1 数据集上训练或微调跟踪模型
- 参考轨迹预测辅助多摄像头关联的实现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Track1: Multi-Camera People Tracking
> L64:  We use Social-Implicit model.

## 星数曲线

```mermaid
xychart-beta
    title "yuntaeJ/SCIT-MCMT-Tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-24 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8d64af6fcf5e` · [字段定义](../../DATASET.md)*
