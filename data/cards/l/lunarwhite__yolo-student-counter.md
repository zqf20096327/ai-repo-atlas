# lunarwhite/yolo-student-counter

⭐ 47 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/lunarwhite/yolo-student-counter) · 个人维护 · 中文 README

**基于 YOLOv5 的教室人数检测：支持图片/视频/直播流输入**

在 YOLOv5 预训练模型基础上，使用 Kaggle Classroom Monitoring Dataset（partA 2000 张 + partB 2405 张，XML 标注）进行训练，实现教室场景的人员目标检测与计数；测试输入覆盖图片、视频与直播流。提供 detect.sh / train.sh 脚本执行训练与预测，环境为 PyTorch 1.7.1+cu110 与 Python 3.8.5。可视化图形界面与目录结构优化仍标记为 TODO。以源码仓库形式提供，需自行下载预训练权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持图片、视频、直播流多种输入格式的人数检测
- 基于 Kaggle 教室监控数据集（4405 张图片）微调 YOLOv5
- 提供 train.sh / detect.sh 训练与预测脚本
- 含 XML 转 TXT 数据预处理流程，丢弃缺失标签样本

## 适用场景

- 我想统计教室或监控画面中的人员数量
- 用 YOLOv5 在自定义教室数据集上训练检测模型
- 学习目标检测从数据预处理到训练测试的完整流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: Monitor in classroom headcount, support image/video/live streaming as input. 基于YOLOv5的教室人数检测统计，支持图片、视频和直播流等多种媒体输入格式
> L20: - 目标检测 (Object Detection) 在教室人数统计上的应用尝试
> L21: - 先借助 YOLOv5 预训练模型对图片数据集进行训练，再测试多种输入流

## 星数曲线

```mermaid
xychart-beta
    title "lunarwhite/yolo-student-counter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-31 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a0299dd0e873` · [字段定义](../../DATASET.md)*
