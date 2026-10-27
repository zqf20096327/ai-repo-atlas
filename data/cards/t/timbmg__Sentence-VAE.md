# timbmg/Sentence-VAE

⭐ 593 · Python · 推送 2026-06-10 · [GitHub](https://github.com/timbmg/Sentence-VAE) · 个人维护

**Bowman 等 2015 句子 VAE 论文的 PyTorch 复现实现**

用 PyTorch 重新实现论文《Generating Sentences from a Continuous Space》（Bowman et al. 2015）的句子变分自编码器：在 Penn Tree Bank 语料上训练 RNN/GRU 编码器-解码器 VAE（不支持 LSTM），支持 KL 退火（logistic/linear）、词级与嵌入 dropout、TensorBoard 记录等训练参数；README 报告了 4 个 epoch 的 NLL/KL 指标，并可用 inference.py 从隐空间采样与插值生成句子。面向需要复现或研究该模型的研究者与开发者。

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

- RNN/GRU 编码器-解码器的句子 VAE 实现（不支持 LSTM）
- KL 退火函数支持 logistic 与 linear 两种
- inference.py 支持从隐空间采样与句子插值
- 提供 dowloaddata.sh 脚本下载 PTB 数据

## 适用场景

- 复现 Bowman et al. 2015 的句子 VAE 实验
- 研究生成式文本模型与隐空间句子插值
- 在此基础上调整训练参数做变体实验

## 场景标签

 · 领域:NLP/生成模型

## 证据(README 行号)

> L3: PyTorch re-implementation of _Generating Sentences from a Continuous Space_ by Bowman et al. 2015.
> L86: For obtaining samples and interpolating between senteces, inference.py can be used.

## 星数曲线

```mermaid
xychart-beta
    title "timbmg/Sentence-VAE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 592 --> 594
    line [593, 593]
```

2026-10-18 593 → 2026-10-27 593（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `30197400e980` · [字段定义](../../DATASET.md)*
