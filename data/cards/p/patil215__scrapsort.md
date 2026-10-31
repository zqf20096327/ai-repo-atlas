# patil215/scrapsort

⭐ 31 · JavaScript · GPL-3.0 · 推送 2026-02-02 · [GitHub](https://github.com/patil215/scrapsort) · 个人维护

**树莓派垃圾自动分类装置：卷积网络识别可回收物**

Hackathon 项目（Greylock Hackfest 2017）：用相机拍摄托盘上的垃圾，基于重训最后一层的 Inception-v3 卷积网络判定其是否属于金属、纸张、纸板、玻璃、塑料等可回收类别，树莓派 3 根据分类结果驱动舵机翻转托盘，将垃圾倒入对应垃圾桶。分类结果与照片发送到 Firebase 数据库，配套仪表盘展示垃圾统计。最初尝试 Google Cloud Vision API 做标签匹配，后改为自训模型。README 未给出安装或复现步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Inception-v3 重训最终层，识别 5 类可回收材料
- 树莓派 3 + 相机模块 + 舵机托盘的硬件分拣装置
- 相机运动检测触发分类流程
- 分类结果与照片上传 Firebase，配套统计仪表盘

## 适用场景

- 家庭场景下自动把垃圾分入可回收/不可回收桶
- 通过仪表盘查看自己产生的垃圾统计
- 了解如何用卷积网络加树莓派搭建嵌入式分类设备

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: I built a classifier that uses computer vision to determine if a piece of trash is recyclable or not. This classifie
> L15: The classification algorithm I settled on was a modified convolutional neural network that we trained on our own cu

## 星数曲线

```mermaid
xychart-beta
    title "patil215/scrapsort 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `15dd0f754324` · [字段定义](../../DATASET.md)*
