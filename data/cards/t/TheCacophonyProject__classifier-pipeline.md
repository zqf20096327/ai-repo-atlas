# TheCacophonyProject/classifier-pipeline

⭐ 23 · Python · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/TheCacophonyProject/classifier-pipeline) · 组织维护

**热成像视频动物追踪与分类的 CNN 训练/推理管线**

Cacophony Project 的热成像动物识别管线：提供从 CPTV 热视频构建训练/验证/测试数据集（build.py）、训练 TensorFlow CNN（train.py）、模型评估、TF Lite 与 OpenVINO 转换，以及对 CPTV 文件执行追踪与动物分类（classify.py）的完整脚本。树莓派上支持实时追踪与两级模型分类（FP 模型过滤误检，全量模型经 localhost:8123 服务预测），并可通过 pip 安装 pi_classify 可执行文件连接热像相机。限制：环境为 Ubuntu 18.04/Python 3.6.9，需配置 yaml 与系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 CPTV 热视频构建数据集并训练 TensorFlow CNN 分类器
- 树莓派实时追踪与两级分类（FP 模型 + 网络服务预测）
- TF Lite 与 OpenVINO Neural Compute 模型转换脚本
- 按相机/地点切分数据集以减少偏差，支持缩略图自动选取

## 适用场景

- 在树莓派上对热成像视频做动物实时追踪与分类
- 用自己的热视频片段训练动物分类模型
- 对 CPTV 文件批量离线识别动物并生成 JSON/MPEG 输出

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L3: These scripts handle the data pre-processing, training, and execution of a Convolutional Neural Network based classi
> L6: The output is a TensorFlow model that can identify thermal video clips of animals
> L51: Uses a pre-trained model to identifying and classifying any animals in supplied CPTV file, CPTV file must have asso

## 星数曲线

```mermaid
xychart-beta
    title "TheCacophonyProject/classifier-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `730fbe700b71` · [字段定义](../../DATASET.md)*
