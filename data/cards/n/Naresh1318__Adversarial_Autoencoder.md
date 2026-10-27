# Naresh1318/Adversarial_Autoencoder

⭐ 435 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/Naresh1318/Adversarial_Autoencoder) · 个人维护

**TensorFlow 对抗自编码器实现：自编码器训练与隐空间探索**

基于 TensorFlow 实现对抗自编码器（AAE）及其监督、半监督变体的研究代码库，配套四篇 Medium 系列教程。提供基础自编码器训练与图像生成、对抗训练约束隐空间分布、风格与内容解耦、以及用 1000 个标注样本做 MNIST 半监督分类的脚本；MNIST 数据集自动下载到 ./Data，训练产生 TensorBoard 日志。通过 pip 安装依赖于 virtualenv 环境运行，作者建议训练时使用 GPU，Windows 下存在文件夹命名报错问题需修改代码或改用 Linux。

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

- 四种脚本：自编码器/对抗/监督/半监督对抗自编码器训练与加载
- 半监督路径下 1000 个标注样本做 MNIST 分类
- MNIST 数据集自动下载，训练生成 TensorBoard 日志
- 配套四篇 Medium 教程文章

## 适用场景

- 学习对抗自编码器的实现与隐空间分析方法
- 复现风格与内容解耦实验
- 做半监督 MNIST 分类实验对比

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: This repository contains code to implement adversarial autoencoder using Tensorflow.
> L58:  python3 adversarial_autoencoder.py --train True
> L96:  python3 semi_supervised_adversarial_autoencoder.py --train True

## 星数曲线

```mermaid
xychart-beta
    title "Naresh1318/Adversarial_Autoencoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 434 --> 436
    line [435, 435]
```

2026-10-18 435 → 2026-10-27 435（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3529df733698` · [字段定义](../../DATASET.md)*
