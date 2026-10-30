# devmount/GermanWordEmbeddings

⭐ 245 · Jupyter Notebook · MIT · 推送 2026-10-07 · [GitHub](https://github.com/devmount/GermanWordEmbeddings) · [官网](https://devmount.github.io/GermanWordEmbeddings/) · 个人维护

**德语词向量训练工具：语料获取、预处理、训练与评估**

基于 gensim word2vec 的德语词向量工具包，覆盖完整流程：下载德语维基百科与新闻语料、用 WikiExtractor 与 preprocessing.py 做预处理（去 XML/标点/停用词、双元音替换、bigram 短语检测）、用 training.py 训练 Skip-Gram/CBOW 模型（支持断点续训与全模型存储）、用 evaluation.py 生成句法与语义类比测试集（共约 11k 问题）并评估，另有 PCA 二维可视化脚本。项目始于 2015 年，README 声明仍在维护、历史模型仍可加载。需 Python 3.12/3.13 与 NLTK 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- corpus→preprocess→train→evaluate→visualize 全流程脚本
- 自带德语句法/语义测试集（约 10k 类比 + 950 语义问题）
- 支持训练参数定制（维度/窗口/负采样/Skip-Gram vs CBOW）与全模型断点续训
- word2vec_german.sh 一键下载语料并完成训练评估

## 适用场景

- 我想在德语语料上训练自己的 word2vec 词向量
- 评估已训练词向量的句法与语义类比表现
- 可视化词向量的二维 PCA 投影

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: There has been a lot of research about the training of word embeddings on English corpora. This toolkit applies gens
> L30: Now you can download `word2vec_german.sh` and execute it in your shell to automatically download this toolkit and t

## 星数曲线

```mermaid
xychart-beta
    title "devmount/GermanWordEmbeddings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 244 --> 246
    line [245, 245]
```

2026-10-18 245 → 2026-10-30 245（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `47244658fa8b` · [字段定义](../../DATASET.md)*
