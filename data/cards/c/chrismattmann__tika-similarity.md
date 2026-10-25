# chrismattmann/tika-similarity

⭐ 108 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/chrismattmann/tika-similarity) · 组织维护

**基于文件元数据特征计算文件相似度的 Python 工具集**

使用 Tika-Python（Apache Tika 的 Python 移植）解析文件元数据，计算文件间相似度：以特征集合的交集与并集之比得出 Jaccard 相似度分数，另提供基于元数据值的 Edit Distance 与 Cosine Distance 两两比较脚本，可用 --accept 按 IANA MIME 类型过滤。分数排序后可生成 Cluster、Circlepacking、Composite、Sunburst 等 D3 可视化。脚本含 Tika server 失败检测与重启逻辑，附单元测试。面向需要批量比对文档相似度并做聚类可视化的开发者与科研用户。

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

- 元数据特征集合的 Jaccard 相似度计算（键比较与值比较两种模式）
- Edit Distance 与 Cosine Distance 两两相似度脚本
- 按 IANA MIME 类型（--accept）过滤参与计算的文件
- 多种 D3 可视化输出：Cluster/Circlepacking/Composite/Sunburst

## 适用场景

- 批量比对目录内文档的元数据相似度并排序
- 将相似文件聚类并生成 D3 可视化页面
- 对爬取或归档的大批文件做相似度分组

## 场景标签

 · 领域:信息检索/文档处理

## 证据(README 行号)

> L3: This project demonstrates the usage of the Tika-Python package (Python port of Apache Tika) to compute file similari
> L5: The script can iterate over all files in the current directory, or specific files by command line, derive their meta
> L7: Scores are sorted in reverse (descending) order which can be shown in three different Data-Driven document visualiza

## 星数曲线

```mermaid
xychart-beta
    title "chrismattmann/tika-similarity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-25 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f1d6b8fc1e82` · [字段定义](../../DATASET.md)*
