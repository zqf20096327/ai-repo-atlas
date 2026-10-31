# aadium/wheat-disease-detection

⭐ 14 · 推送 2026-08-30 · [GitHub](https://github.com/aadium/wheat-disease-detection) · 个人维护

**用 CNN 从小麦图像识别 4 类健康/病害状态的 Python 脚本**

Python 脚本实现基于 Keras Sequential 模型的卷积神经网络，对小麦图像做 4 分类（健康、叶锈病、冠腐根腐病、散黑穗病）。流程包括：加载数据集并转为 numpy 数组归一化、划分训练/测试集、用 ImageDataGenerator 做数据增强、训练并输出准确率与损失、对新图像预处理并预测标签，最终以 H5 格式保存模型。面向使用 large-wheat-disease-classification-dataset 数据集的开发者/科研用户，README 未给出安装命令或依赖清单。

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

- Keras Sequential CNN 实现 4 分类（健康/叶锈/冠根腐/散黑穗）
- ImageDataGenerator 数据增强训练
- 训练后可对新图像预测标签并输出
- 模型以 H5 格式保存

## 适用场景

- 对小麦照片做病害分类预测
- 基于公开数据集训练小麦病害 CNN 模型
- 复用 H5 模型做后续预测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: This is a Python script that implements a Convolutional Neural Network (CNN) model for detecting wheat diseases. It 
> L9: The model is then used to classify new images by preprocessing them and predicting their labels. The predicted label

## 星数曲线

```mermaid
xychart-beta
    title "aadium/wheat-disease-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `ecb39cc9b7fa` · [字段定义](../../DATASET.md)*
