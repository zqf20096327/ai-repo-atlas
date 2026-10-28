# kasmya/Cosmetic-Recomendation-System

⭐ 25 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kasmya/Cosmetic-Recomendation-System) · [官网](https://colour-atelier.pages.dev/) · 个人维护

**基于机器学习与计算机视觉的护肤/彩妆推荐 REST API 系统**

单一 FastAPI 服务提供两个功能：一是护肤品推荐，用 8,649 条评论训练的梯度提升分类器预测用户偏好概率，结合 TF-IDF+SVD 成分相似度混合排序，附硬过滤与解释；二是粉底色号匹配，OpenCV 检测人脸并测量肤色，Lab 色彩空间 k-NN 匹配 36 品牌 621 个色号。另有护肤流程规划、虚拟试妆、肤质评估问卷等功能。README 明确列出数据量小导致排序能力有限（AUC 约 0.6）等限制，照片仅在内存中处理不存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 梯度提升+校准模型预测用户 4 星以上评分概率，附成分相似度混合排序
- OpenCV 人脸检测与 CIELAB 肤色测量，k-NN 匹配 621 个真实粉底色号
- 模型注册-门控晋升的 MLOps 流程与 Prometheus/Grafana 监控
- 自曝并修复了原数据集的数据泄漏问题（标签即特征）

## 适用场景

- 上传自拍照片匹配相近的粉底色号
- 按肤质、预算、忌用成分获取带解释的护肤品推荐
- 生成符合预算与成分冲突规则的早晚护肤流程

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L5: 1. **Skincare recommender (machine learning).** Ranks 315 skincare products using a model trained on 8,649 real revi
> L6: 2. **Makeup shade matcher (computer vision).** Upload a face photo; OpenCV measures your skin colour and a k-NN sear
> L30: - **Gradient boosting classifier** (`HistGradientBoostingClassifier`) predicts P(user rates a product 4+ stars) fro

## 星数曲线

```mermaid
xychart-beta
    title "kasmya/Cosmetic-Recomendation-System 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-22 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bf43d4f06529` · [字段定义](../../DATASET.md)*
