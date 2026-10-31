# nghorbani/homogenus

⭐ 133 · Python · NOASSERTION · 推送 2026-09-17 · [GitHub](https://github.com/nghorbani/homogenus) · [官网](https://smpl-x.is.tue.mpg.de/) · 组织维护

**基于全身图像与 OpenPose 关键点的人像性别分类器**

CVPR 2019 论文 Expressive Body Capture 的官方推理代码：输入全身人像与 OpenPose 2D 关键点，输出性别预测，并生成标注性别的关键点与叠加图像。其输出用于 SMPLify-X 中选择男性/女性/中性 3D 人体模型。限制：仅含推理代码；需 Python 3.7、TensorFlow 1.13/1.15，不支持 TF2；预训练权重需从需登录的项目下载页获取，可得性未验证；仓库声明不再积极开发，仅限非商业与科研用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 输入全身图像与 OpenPose 2D 关键点，输出性别预测
- 生成性别标注的 OpenPose 关键点与叠加图像
- 供 SMPLify-X 按性别选择 3D 人体模型（男/女/中性）
- 仅含推理代码，需从项目网站下载预训练权重

## 适用场景

- 为 SMPLify-X 流水线提供性别判定以选择对应人体模型
- 对全身人像数据集批量生成性别标注的关键点与图像

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: Numerous methods have classified human gender using face images. In full-body images of a person, the face may be s
> L49: usage: homogenus_infer.py [-h] [-tm TRAINED_MODEL_DIR] -ii IMAGES_INDIR -oi

## 星数曲线

```mermaid
xychart-beta
    title "nghorbani/homogenus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 132 --> 134
    line [133, 133]
```

2026-10-18 133 → 2026-10-31 133（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7568d8496142` · [字段定义](../../DATASET.md)*
