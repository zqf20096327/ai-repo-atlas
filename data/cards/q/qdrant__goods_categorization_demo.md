# qdrant/goods_categorization_demo

⭐ 32 · Jupyter Notebook · 推送 2026-09-07 · [GitHub](https://github.com/qdrant/goods_categorization_demo) · 组织维护

**电商商品名称分类演示：文本编码+向量检索归类**

Qdrant 官方演示项目：用神经文本编码器对真实电商商品名称编码，向量存入 Qdrant 相似度搜索引擎；提交新商品名时用同一网络编码并与已存向量比对完成归类。类别以向量集合形式存在，可扩展/精简类别而无需重训模型；界面上的类别点图为 Umap 降维到 2D 的示意，距离不保证准确。运行需 Poetry 装依赖、Docker 起 Qdrant、uvicorn 起后端、npm 起前端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 商品名经神经编码器编码后存入 Qdrant 做相似度比对
- 类别即向量集合，可无重训扩展与精简
- 前端类别点图用 Umap 降到 2D 展示（注明损失信息）
- 提供 VITE_MOCK 模式让前端独立于后端运行

## 适用场景

- 演示向量检索如何做电商商品归类
- 了解类别向量化的免重训扩展方式
- 参考 Qdrant 文本编码+检索的完整前后端示例

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L4: Each product name is encoded using a **neural text encoder model** and indexed into the Qdrant vector similarity sea
> L5: Once you submit a new product name, it will be encoded using the same neural network and compare against stored refe

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/goods_categorization_demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ee77cd07680a` · [字段定义](../../DATASET.md)*
