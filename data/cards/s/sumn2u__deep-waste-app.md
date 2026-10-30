# sumn2u/deep-waste-app

⭐ 66 · HTML · BSD-3-Clause · 推送 2026-05-30 · [GitHub](https://github.com/sumn2u/deep-waste-app) · [官网](https://www.dwaste.live/) · 个人维护

**用手机拍照识别垃圾分类并给予奖励的 Flutter 应用**

开源 AI 移动应用：用户拍摄或上传垃圾图片，设备端 TensorFlow Lite 模型实时分类为金属、玻璃、纸张、塑料等 10 类，并给出处理指导；正确管理垃圾可获得积分奖励，应用还提供回收教育内容与进度跟踪，无需注册。基于自有 Kaggle 数据集训练模型，已上架 Google Play 与 App Store。已知限制：部分图片准确率低于 45%，部分设备运行模型会崩溃；可提交错误预测修正。源码基于 Flutter，需 Flutter 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手机拍照/上传即时的 10 类垃圾分类（TensorFlow Lite 设备端推理）
- 正确处理垃圾可获得积分奖励，无需注册
- 用户可提交错误预测以改进模型
- 配套自建 Kaggle 垃圾图像数据集（10 类，人工核验）

## 适用场景

- 不确定垃圾类别时拍照查询分类与处理方式
- 通过积分奖励激励自己坚持正确分类回收
- 学习各类垃圾的回收知识并跟踪自己的回收数量

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: D.Waste is as an open source AI-powered app that enables users to identify the type of waste they are trying to disp
> L14: In this app, we have prepared a substantial collection of waste images and trained a machine learning model. The tr
> L36: After training the AI model, we export it to TensorFlow Lite for mobile device compatibility. Using the app, users 

## 星数曲线

```mermaid
xychart-beta
    title "sumn2u/deep-waste-app 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-30 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f9c8c5123a5b` · [字段定义](../../DATASET.md)*
