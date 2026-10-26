# developers-cosmos/Meme-Generator

⭐ 94 · JavaScript · Apache-2.0 · 推送 2026-02-11 · [GitHub](https://github.com/developers-cosmos/Meme-Generator) · 组织维护

**上传人像照片自动生成表情梗图的 Web 应用**

Web 应用：用户上传人脸照片，应用通过基于 CNN 的表情识别模型分析图中人物表情，并据此自动生成梗图（meme），可在页面下载生成结果。模型部分使用 3 个不同人脸数据集（日本人脸、印度演员、名人面孔）经 GCP AutoML 训练，按各类别精度为模型分配权重组合输出；训练涉及欠采样/过采样与图像增广。技术栈为 Flask、Chef 与 Google Cloud Platform。README 提供在线演示链接，未给出本地安装运行步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN 表情识别驱动的自动梗图生成
- 3 个数据集训练的模型按类别精度加权组合
- GCP AutoML 自动训练模型
- Flask 提供 Web 服务，附在线演示链接

## 适用场景

- 上传人像照片一键生成表情梗图
- 下载生成的梗图用于社交分享

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: MemeGen is a web application which generates memes automatically according to the given image. All the user has to d
> L50: > *CNN is a type of Artificial Neural Network, the other types being MLP, RNN, Shallow neural networks, sequence-to

## 星数曲线

```mermaid
xychart-beta
    title "developers-cosmos/Meme-Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-26 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b6550d105408` · [字段定义](../../DATASET.md)*
