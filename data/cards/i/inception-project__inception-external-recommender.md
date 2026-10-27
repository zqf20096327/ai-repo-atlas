# inception-project/inception-external-recommender

⭐ 48 · Python · Apache-2.0 · 推送 2026-06-20 · [GitHub](https://github.com/inception-project/inception-external-recommender) · 组织维护

**为 INCEpTION 标注平台实现外部推荐器的 Python 库**

提供 ariadne 库，用于以 Python 实现并运行 INCEpTION 文本标注平台的外部推荐器（recommender），以 Web 服务形式与 INCEpTION 的 external recommender API 通信。内置多个可直接使用的推荐器：spaCy 的 NER 与词性标注、Jieba 中文分词、sklearn-crfsuite 提及检测、S-BERT+LightGBM 句子分类、NLTK 词干提取等，部分支持在标注过程中增量训练。可基于 gunicorn 部署多 worker 服务，并提供不依赖 INCEpTION 的请求测试脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 INCEpTION external recommender API 的 Web 服务框架
- 内置 10 个可用推荐器（spaCy/Jieba/sklearn/S-BERT/Flair/Adapters 等）
- 部分推荐器可训练（trainable），通过 INCEpTION 界面触发训练
- gunicorn 多 worker 部署示例与脱离 INCEpTION 的 tester 脚本

## 适用场景

- 为 INCEpTION 标注项目接入命名实体或词性自动推荐
- 用自有模型实现自定义外部推荐器
- 多人同时使用时以 gunicorn 部署推荐服务

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository provides **ariadne**, a library
> L6: to run and implement external recommenders for INCEpTION using Python.

## 星数曲线

```mermaid
xychart-beta
    title "inception-project/inception-external-recommender 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-27 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5b20592c051c` · [字段定义](../../DATASET.md)*
