# UCAS-GYX/YouTube-GDD

⭐ 42 · Python · Apache-2.0 · 推送 2025-12-12 · [GitHub](https://github.com/UCAS-GYX/YouTube-GDD) · 组织维护

**枪支检测数据集 YouTube-GDD：5000 图、16064 枪支标注**

从 343 个高清 YouTube 视频中构建的枪支检测数据集，含 5000 张图像、16064 个枪支实例和 9046 个人物实例标注，标注为 YOLO 格式，类别为 person 与 gun。数据集按文件名划分为 10 个不重叠 fold，用尺度分布的 JS 散度选定 fold7 为测试集、fold6 为验证集。README 提供从源视频重建数据集的三个脚本（下载、抽帧、选图），需先安装 ffmpeg 并 pip 安装依赖；同时给出 YOLOv5 基线评测结果（迁移学习与人物标注的影响分析）。注意多条 YouTube 链接已失效，作者建议改用 Google Drive 下载预处理图像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5000 图像 / 16064 枪支 / 9046 人物实例的 YOLO 格式标注
- 按尺度分布 JS 散度划分 10 折，选定测试与验证集
- 提供从源视频构建数据集的三步脚本（download/extract/select）
- YOLOv5s 基线：附加人物标注使枪支 AP50 从 67.9 升至 77.3

## 适用场景

- 训练与评测枪支检测模型
- 研究人物上下文信息对枪支检测的影响
- 安防场景目标检测研究的数据来源

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: # YouTube-GDD: A challenging gun detection dataset with rich contextual information [[arXiv]](https://arxiv.org/pdf/
> L6: To promote the development of security, this work presents a new challenging dataset called YouTube Gun Detection Da

## 星数曲线

```mermaid
xychart-beta
    title "UCAS-GYX/YouTube-GDD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-31 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6254d4e2c0fe` · [字段定义](../../DATASET.md)*
