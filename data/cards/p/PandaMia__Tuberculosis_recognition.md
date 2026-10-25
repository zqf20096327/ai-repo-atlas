# PandaMia/Tuberculosis_recognition

⭐ 66 · Python · MIT · 推送 2026-04-28 · [GitHub](https://github.com/PandaMia/Tuberculosis_recognition) · [官网](https://tuberculosis-recognition.pandamia.org/) · 个人维护

**PyTorch 结核病胸片 X 光分类模型，含 Streamlit 演示**

基于 PyTorch 的 CNN 二分类模型（四个卷积块+四层全连接），使用 Kaggle 的结核病胸片数据集训练，判别胸片是否患有结核。数据准备阶段将图像统一为单通道以避免模型利用颜色差异 shortcut；针对类别不平衡（3500 正常/700 结核）采用数据增强与加权 BCEWithLogitsLoss，并以 F1 为主要指标。提供训练/评估脚本、可下载的模型权重与 Streamlit 交互应用，作者同时审计了数据集伪影（白矩形、L/R 标注）对结果可信度的影响。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四卷积块 CNN 二分类，测试集 F1 97.87%
- 图像统一单通道处理以消除颜色 spectrum 差异导致的 shortcut
- 针对类别不平衡使用增强与加权损失，弃用 accuracy 改用 F1
- README 审计数据集伪影（白矩形、L/R 标注、来源差异）并提示域外泛化风险

## 适用场景

- 上传胸片获得结核阳性/阴性分类结果
- 复现训练与评估流程并自行训练模型
- 作为数据集伪影审计的参考案例学习 responsible AI 实践

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: The PyTorch neural network model for tuberculosis classification.
> L65: Accuracy on the test dataset is ```99.29%```, f1-score is ```97.87%```.

## 星数曲线

```mermaid
xychart-beta
    title "PandaMia/Tuberculosis_recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-25 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b01fbed16f65` · [字段定义](../../DATASET.md)*
