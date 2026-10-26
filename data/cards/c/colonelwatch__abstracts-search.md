# colonelwatch/abstracts-search

⭐ 105 · C · Apache-2.0 · 推送 2026-06-19 · [GitHub](https://github.com/colonelwatch/abstracts-search) · [官网](https://huggingface.co/spaces/colonelwatch/abstracts-index) · 个人维护

**索引 2 亿+学术文献摘要的语义搜索引擎**

将 OpenAlex 数据集公开摘要用 stella_en_1.5B_v5 模型生成嵌入，训练 faiss 索引，构成覆盖 2 亿+学术出版物的语义搜索系统。项目拆为四个仓库：编排 Makefile、嵌入数据集、Hugging Face Space 搜索界面与训练好的索引。运行搜索界面仅需克隆 abstracts-index；完整重建曾用四块 L4 GPU 一周完成，后续构建最低需 16 GB 内存、RTX 3060 12GB 与 2 TB 磁盘，可通过下载已发布的嵌入数据集绕过初始构建，并支持与 OpenAlex 季度快照同步。

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

- 索引 200+ 百万 OpenAlex 学术出版物摘要
- stella_en_1.5B_v5 生成嵌入 + faiss 训练索引
- 嵌入与索引以 CC0 发布在 Hugging Face Dataset/Space
- 可与 OpenAlex 季度快照重复构建保持同步

## 适用场景

- 按语义相似度检索学术文献摘要并获得 OpenAlex ID
- 在自有硬件上重建或同步学术文献搜索索引
- 复用 CC0 嵌入数据集构建下游检索应用

## 场景标签

`语义搜索` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: `abstracts-search` is a project about indexing 200+ million academic publications into a single semantic search engi
> L16: An Internet connection is always needed. All data associated with the publications (titles, abstracts, authors, etc

## 星数曲线

```mermaid
xychart-beta
    title "colonelwatch/abstracts-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-26 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2290c15b6fd0` · [字段定义](../../DATASET.md)*
