# inboxpraveen/Movie-Recommendation-System

⭐ 246 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/inboxpraveen/Movie-Recommendation-System) · [官网](https://inboxpraveen.github.io/projects/project-3.html) · 个人维护

**给开发者的内容型电影推荐系统：训练管线加 Django 服务**

基于内容相似度的电影推荐器：训练管线读取 TMDB 格式 CSV，拼接类型、关键词、剧情等文本，经 TF-IDF 与 SVD 降维后计算余弦相似度，每部影片保存 top-50 近邻；Django 应用提供搜索、自动补全与 JSON API，无用户历史收集，首次查询即可工作。仓库自带 6,248 部影片的演示模型，克隆即用；服务时仅读取 parquet/JSON/NumPy，不加载 pickle。支持 Render、Heroku 与 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TF-IDF + SVD + top-K 余弦近邻训练管线，支持自有 TMDB 格式数据
- 每片仅存 50 近邻（约 20 MB@5 万片），服务时内存映射单行读取，查询中位数约 1.1 ms
- 自带 6,248 部影片演示模型，克隆后开箱即用
- 提供搜索自动补全、JSON API 与健康检查端点，推理类可脱离 Django 使用

## 适用场景

- 部署一个可按片名查询相似影片的网站或 JSON API
- 在自己的影片目录上训练内容型推荐模型并交付
- 在自有代码中调用推理类做带年份/类型/评分过滤的推荐

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L5: **A content-based movie recommender you can run, train and deploy.**
> L24: - **A training pipeline** (`training/train.py`) that turns any TMDB-shaped CSV into a small, fast model directory.
> L54: 4. Fit TF-IDF over one and two word grams, then reduce with truncated SVD to 500 dimensions.

## 星数曲线

```mermaid
xychart-beta
    title "inboxpraveen/Movie-Recommendation-System 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 245 --> 247
    line [246, 246]
```

2026-10-29 246 → 2026-10-31 246（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5cbd7fb253e2` · [字段定义](../../DATASET.md)*
