# ahmedfgad/KivyAndroidClassification

⭐ 26 · Python · 推送 2026-10-17 · [GitHub](https://github.com/ahmedfgad/KivyAndroidClassification) · 个人维护

**在 Android 上用 NumPy ANN 做图像分类的 Kivy 应用示例项目**

演示项目：用纯 NumPy 从零构建人工神经网络，在桌面端以遗传算法优化权重（4 类 Fruits360 水果数据），权重存为 weights.npy；再通过 Kivy 桌面应用读取图片并预测类别标签，最终用 Buildozer 与 python-4-android 打包为 Android APK，在手机上加载预训练权重对测试图片分类。给想在 Android 上运行 NumPy 模型的开发者参考；README 未给出具体安装命令，细节依赖作者此前的系列教程与关联仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 NumPy 实现 ANN，权重经遗传算法优化
- Kivy 桌面应用加载 weights.npy 预测图片类别
- 通过 Buildozer/python-4-android 导出为 Android 应用

## 适用场景

- 学习如何在 Android 端运行纯 NumPy 构建的神经网络
- 参考 Kivy 打包含 NumPy 依赖的 APK 的流程
- 复现 Fruits360 4 类水果图片的分类示例

## 场景标签

`教程课程` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L4: This project runs a pre-trained artificial neural network (ANN) in Android for image classification. The ANN is buil
> L6: The ANN created using NumPy is trained in a desktop computer using 4 classes from the Fruits360 dataset which are ap

## 星数曲线

```mermaid
xychart-beta
    title "ahmedfgad/KivyAndroidClassification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `64d247e77fb7` · [字段定义](../../DATASET.md)*
