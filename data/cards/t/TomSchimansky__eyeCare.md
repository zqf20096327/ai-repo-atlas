# TomSchimansky/eyeCare

⭐ 17 · Python · 推送 2026-02-08 · [GitHub](https://github.com/TomSchimansky/eyeCare) · 个人维护

**用摄像头检测眨眼并提醒休息的护眼概念程序**

作者 2018-2019 年开发的概念程序，针对长时间盯屏幕导致眨眼减少引发的干眼、眼痒问题：程序读取摄像头画面，用 Dlib 68 点人脸关键点定位并裁剪眼部区域，再由基于 mrlEyes_2018_01 数据集训练的 CNN 分类器实时判定睁眼/闭眼，超过设定时间未检测到眨眼即播放提示音。README 提供数据集构建、模型训练（约 50 epoch，RTX3070 约 15 分钟）与实时测试脚本，验证集准确率 98.3%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Dlib 人脸关键点裁剪眼部区域 + CNN 实时睁闭眼分类
- 长时间无眨眼时播放声音提示
- 提供 mrlEyes 数据集预处理、训练与评估脚本
- 验证集 Accuracy 98.3% / Recall 98.7%

## 适用场景

- 长时间用屏幕工作时提醒自己规律眨眼、缓解眼干
- 复现并训练自己的睁闭眼分类模型
- 作为基于 Dlib 关键点的实时眨眼检测参考实现

## 场景标签

 · 领域:计算机视觉/健康工具

## 证据(README 行号)

> L5: which this program tries to fix by giving a subtle sound signal when no blinking is detected for a
> L7: a classifier on the eye regions detecting an open or closed eye in real time.

## 星数曲线

```mermaid
xychart-beta
    title "TomSchimansky/eyeCare 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `d5323f24c135` · [字段定义](../../DATASET.md)*
