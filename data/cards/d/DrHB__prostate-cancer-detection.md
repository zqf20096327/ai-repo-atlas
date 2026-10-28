# DrHB/prostate-cancer-detection

⭐ 20 · Python · MIT · 推送 2026-01-28 · [GitHub](https://github.com/DrHB/prostate-cancer-detection) · 个人维护

**PANDA 挑战亚军方案：CNN 集成做前列腺癌 Gleason 分级**

Kaggle PANDA 挑战（10,616 张数字化前列腺穿刺切片）第二名解决方案的代码仓库：将全切片图像按多分辨率网格切 tile，用 EfficientNet-B0/B1 与 SE-ResNeXt50 作为骨干，经注意力池化聚合 tile 级特征得到切片级分级预测，采用两阶段训练并集成 4 名队员的模型，二次加权 kappa >0.9。面向希望复现竞赛结果或研究病理图像分类的科研开发者，代码按作者分四个训练目录组织，通过 make_pred.sh 脚本生成预测。

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

- EfficientNet / SE-ResNeXt 骨干 + tile 级注意力池化的整体架构
- 两阶段训练：初始训练后用困难样本微调
- 集成 4 名队员模型，二次加权 kappa >0.9
- 工作成果发表于 Nature Medicine 的 PANDA 挑战论文

## 适用场景

- 复现 PANDA 挑战第二名的训练与预测流程
- 参考全切片病理图像的 tile 化与注意力池化建模方法
- 开展前列腺癌 Gleason 分级相关研究

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L8: **CNN ensemble for automated Gleason grading of prostate cancer from whole-slide biopsy images**
> L14: This 2nd place solution uses an ensemble of CNNs (EfficientNet, SE-ResNeXt) with tile-based attention pooling, achi
> L20: - **Attention Pooling**: Learnable aggregation of tile-level features to slide-level prediction

## 星数曲线

```mermaid
xychart-beta
    title "DrHB/prostate-cancer-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `600f9b6108bf` · [字段定义](../../DATASET.md)*
