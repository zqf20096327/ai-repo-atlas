# ritwik12/Celestial-bodies-detection

⭐ 84 · Python · GPL-3.0 · 推送 2026-02-26 · [GitHub](https://github.com/ritwik12/Celestial-bodies-detection) · [官网](https://celestial-bodies-detection.herokuapp.com) · 个人维护

**天体图像分类器：识别行星、星系、卫星、彗星等并给出百科信息**

基于 TensorFlow 1.x 的图像分类项目：对上传或 URL 图片输出天体类别（行星、椭圆/旋涡/不规则星系、卫星、小行星等）及各类别匹配百分比，附 Wikipedia 信息抓取、Google 反向图片搜索跳转。提供 Flask Web 应用（4 个端点）与命令行评估脚本，训练基于 Inception 迁移学习（retrain.py），仓库内含已训练模型文件，可不训练直接评估。限制：依赖 TensorFlow 1.14 旧版本，CUDA GPU 支持为可选配置（示例针对 GTX 1080）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 天体多类别分类并输出各类别匹配百分比
- Flask Web 应用：上传/URL 图片 → 结果页附 Wikipedia 信息
- 基于 Inception 迁移学习，提供 retrain.py 训练与 label_image.py 评估脚本
- 仓库内含已训练模型，可跳过训练直接推理

## 适用场景

- 上传天文图片识别行星或星系类型
- 用自己的训练数据重新训练天体分类模型
- 在本地部署 Flask 网页进行天体图像分类

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L101: `python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps=500 --model_dir=inception --summaries_di
> L107: `python label_image.py test_data/uranus/000.jpg`

## 星数曲线

```mermaid
xychart-beta
    title "ritwik12/Celestial-bodies-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-30 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `41e933ca3dc5` · [字段定义](../../DATASET.md)*
