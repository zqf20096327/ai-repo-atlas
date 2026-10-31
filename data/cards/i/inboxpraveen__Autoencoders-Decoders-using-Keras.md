# inboxpraveen/Autoencoders-Decoders-using-Keras

⭐ 20 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/inboxpraveen/Autoencoders-Decoders-using-Keras) · [官网](https://inboxpraveen.github.io/projects/project-11.html) · 个人维护

**Keras 自编码器工具箱：图像压缩、去噪、检索与变形**

用 TensorFlow/Keras 实现的三种图像自编码器（线性 PCA 式、卷积、去噪），共享统一 encoder/decoder 接口，并提供基于训练编码器的两个应用：编码空间最近邻图像检索和两图 code 插值变形。单一 CLI（main.py，五种模式）可在 LFW 数据集或自有图像文件夹上训练与运行，保存的模型带 model_config.json 自动重建。面向学习自编码器原理、做压缩/去噪基线实验或图像嵌入起步的开发者；普通自编码器的 code 空间不保证平滑，变形中间帧效果受限，VAE 在路线图中。

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

- 三种自编码器（线性/卷积/去噪）共享统一接口
- 编码空间最近邻检索与两图 code 插值变形
- 单 CLI 支持 LFW 或 --data-dir 自有图像训练
- 保存模型自动记录 code size 等配置，测试套件 CPU 下一分钟内完成

## 适用场景

- 学习自编码器原理并跑通图像压缩与去噪基线
- 在自己的图片集上训练并做相似图像检索
- 生成两幅图像之间的 latent 空间变形序列

## 场景标签

`图像视频处理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: Three image autoencoders in TensorFlow and Keras (a linear PCA-style model, a deep convolutional model and a denois
> L24: - **Image retrieval**: encodes a set of images once and finds the nearest neighbours of any query in code space wit


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b466783928b3` · [字段定义](../../DATASET.md)*
