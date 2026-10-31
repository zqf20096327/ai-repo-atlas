# Genius-Society/svhn

⭐ 34 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/Genius-Society/svhn) · [官网](https://genius-society-svhn.hf.space) · 个人维护

**PyTorch 深度 CNN 识别 SVHN 街景门牌多数字（准确率 89%）**

基于 PyTorch 的深度卷积神经网络实现，读取 Google 街景门牌号（SVHN）数据集，对每张图片中 0-9 的多数字序列进行识别，模型测试准确率为 89%。训练代码位于 main 分支，当前仓库提供带 WebUI 的实现（项目标题为 SVHN WebUI）。README 引用了多数字识别论文作为参考。面向计算机视觉与深度学习开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 实现的深度 CNN 多数字识别
- 使用 SVHN 街景门牌数据集，每图含 0-9 多位数字
- 模型测试准确率 89%

## 适用场景

- 在 SVHN 数据集上训练/测试多数字识别模型
- 通过 WebUI 运行门牌号识别

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: This project is a _PyTorch_ implementation that uses deep CNN to recognize multi-digit numbers using the Street View

## 星数曲线

```mermaid
xychart-beta
    title "Genius-Society/svhn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4e240e9117a0` · [字段定义](../../DATASET.md)*
