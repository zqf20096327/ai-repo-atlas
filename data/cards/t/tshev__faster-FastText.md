# tshev/faster-FastText

⭐ 16 · HTML · MIT · 推送 2026-09-08 · [GitHub](https://github.com/tshev/faster-FastText) · 个人维护

**fastText 性能调优分叉：词向量学习与文本分类库**

facebookresearch/fastText 的分叉仓库，README 内容为上游 fastText 文档：提供词表示学习（skipgram/cbow，含子词 n-gram）与监督文本分类两类功能，通过 CLI 与 Python 绑定使用；支持模型量化压缩（.ftz）以降低内存占用，可输出 P@k/R@k 评估与标签预测。需从源码编译（make 或 cmake，C++11 编译器），构建产物为 fasttext 二进制与共享/静态库。仓库描述声称训练与推理速度最高提升 2 倍，但 README 正文未含相关改动说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- skipgram/cbow 词向量训练，默认 3-6 字符 n-gram 子词支持
- 监督文本分类：predict/predict-prob 与 P@k、R@k 评估
- 模型量化生成 .ftz 文件以减小内存占用
- 提供 make 与 cmake 两种构建方式及 Python 绑定（pybind11）

## 适用场景

- 在自有语料上训练词向量并查询词/句子向量表示
- 训练轻量文本分类器（如情感分析）并做评估
- 量化已训练模型以在低内存环境部署

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L105: This library has two main use cases: word representation learning and text classification.
> L149: This library can also be used to train supervised text classifiers, for instance for sentiment analysis.

## 星数曲线

```mermaid
xychart-beta
    title "tshev/faster-FastText 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e362f801e141` · [字段定义](../../DATASET.md)*
