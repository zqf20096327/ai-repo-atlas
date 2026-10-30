# antas-marcin/weaviate-multi-vector-example

⭐ 15 · Jupyter Notebook · 推送 2026-10-03 · [GitHub](https://github.com/antas-marcin/weaviate-multi-vector-example) · 个人维护

**Weaviate + ColQwen2 多向量嵌入与 MUVERA 量化的 PDF 相似检索示例**

由个人维护的演示项目，展示如何用 Weaviate 向量数据库与 ColPali（ColQwen2）视觉语言模型对 PDF 文件做多向量嵌入并执行相似度搜索，涉及 MUVERA 量化方案。运行需 Docker 与 Python3，通过 venv 或 uv 安装 requirements.txt 依赖，提供一个 ColQwen2 的 Jupyter Notebook 示例。README 附 Weaviate 多向量嵌入与 ColPali 文档检索的参考链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ColPali（ColQwen2）视觉模型生成多向量嵌入
- 基于 Weaviate 对 PDF 执行相似度搜索
- 涉及 MUVERA 量化方案
- 提供 ColQwen2 的 Jupyter Notebook 示例

## 适用场景

- 学习多向量嵌入在 PDF 检索中的用法
- 参考 Weaviate 多向量与 MUVERA 量化的接入方式

## 场景标签

`语义搜索` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L5: This is a simple demo of how one can use Weaviate and ColPali (ColQwen2) models and perform similarity search over P
> L32: 1. ColQwen2 example: (colqwen2.ipynb)

## 星数曲线

```mermaid
xychart-beta
    title "antas-marcin/weaviate-multi-vector-example 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `0401b2700770` · [字段定义](../../DATASET.md)*
