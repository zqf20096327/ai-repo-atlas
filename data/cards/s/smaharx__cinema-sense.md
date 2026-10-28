# smaharx/cinema-sense

⭐ 19 · Python · NOASSERTION · 推送 2026-06-16 · [GitHub](https://github.com/smaharx/cinema-sense) · 个人维护

**语义电影搜索引擎：按含义而非关键词检索影片**

基于深度学习与向量相似度检索的电影推荐引擎：将影片元数据经 HuggingFace all-MiniLM-L6-v2 模型编码为 384 维向量，用户查询经同一模型转向量后由 FAISS（CPU）做近邻检索，再经 Pandas 过滤年份/评分，异步调用 TMDb API 获取海报，通过 Streamlit 暗色 UI 交互。需先本地生成 .faiss 向量索引与 .pkl 数据（GitHub 不含大文件），并配置免费 TMDb API key；数据池预取策略用于避免严格过滤条件下结果枯竭。面向个人开发者与影片爱好者，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- all-MiniLM-L6-v2 句向量编码 + FAISS 近邻检索
- 过取（over-fetching）架构避免严格过滤条件下的结果枯竭
- @st.cache_resource 将 5000+ 向量索引常驻内存
- 线程池并行调用 TMDb API 渲染海报

## 适用场景

- 用自然语言描述（如太空银行劫案）查找相关电影
- 按含义而非关键词匹配浏览影片库
- 结合年份/评分过滤获取语义相关的推荐结果

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L15: The system passes movie metadata through a HuggingFace Transformer model to compress contextual meaning into a 384-
> L19: * **Semantic Context Search:** True NLP understanding via HuggingFace's `all-MiniLM-L6-v2` transformer model.

## 星数曲线

```mermaid
xychart-beta
    title "smaharx/cinema-sense 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `98dd9d0a8710` · [字段定义](../../DATASET.md)*
