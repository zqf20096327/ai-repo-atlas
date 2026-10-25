# elastic/eland

⭐ 693 · Python · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/elastic/eland) · [官网](https://eland.readthedocs.io) · 组织维护

**用 Pandas 兼容 API 操作 Elasticsearch 数据的 Python 客户端与工具包**

Elastic 官方维护的 Python 客户端：以 Pandas 兼容的 DataFrame API 包装 Elasticsearch 索引，数据处理与过滤均在 Elasticsearch 端执行而非本地内存，从而可操作存储在 Elasticsearch 中的大数据集；并支持将 scikit-learn、XGBoost、LightGBM 训练的回归/分类模型序列化为 Elasticsearch 推理模型，以及从 Hugging Face hub 导入 PyTorch/BERT NLP 模型。提供 PyPI、Conda Forge 与 Docker 镜像安装方式，NLP 功能需额外安装 pytorch extras。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pandas 兼容 DataFrame API，计算下推到 Elasticsearch 执行
- 上传 scikit-learn/XGBoost/LightGBM 训练模型到 Elasticsearch 做推理
- eland_import_hub_model 命令导入 Hugging Face PyTorch NLP 模型
- 提供 PyPI、Conda Forge 与官方 Docker 镜像三种分发途径

## 适用场景

- 在 Jupyter 中分析超出本地内存的 Elasticsearch 大数据集
- 把已训练的回归/分类模型部署到 Elasticsearch 集群做推理
- 将 Hugging Face 上的 BERT 类模型导入 Elasticsearch 执行 NLP 任务

## 场景标签

 · 领域:数据分析/Elasticsearch 工具链

## 证据(README 行号)

> L27: Eland also provides tools to upload trained machine learning models from common libraries like
> L134: Eland allows transforming trained regression and classification models from scikit-learn, XGBoost, and LightGBM

## 星数曲线

```mermaid
xychart-beta
    title "elastic/eland 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 692 --> 694
    line [693, 693]
```

2026-10-18 693 → 2026-10-25 693（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b40bc8cc20ac` · [字段定义](../../DATASET.md)*
