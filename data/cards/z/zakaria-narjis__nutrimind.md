# zakaria-narjis/nutrimind

⭐ 258 · TypeScript · Apache-2.0 · 推送 2026-03-21 · [GitHub](https://github.com/zakaria-narjis/nutrimind) · [官网](https://diet-recommendation-system.streamlit.app/) · 个人维护

**基于营养向量相似度的个性化饮食推荐 Web 应用**

全栈饮食推荐系统：从年龄、体重、身高、活动水平等健康数据计算 BMI/BMR/TDEE 与目标热量，将每餐营养需求表示为 9 维向量，用 scikit-learn 的 NearestNeighbors 余弦相似度从 50 万+ Food.com 食谱中匹配最近邻，生成个性化每日餐单；也支持自定义营养向量搜索与食材过滤。后端 FastAPI，前端 Streamlit，通过 Docker Compose 部署，另有 Streamlit Cloud 托管版本。冷启动无需用户历史数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BMI/BMR/TDEE 计算 + 热量按餐次分配后做最近邻食谱匹配
- 9 维营养向量 + 余弦相似度的内容推荐引擎
- 50 万+ Food.com 食谱数据集，启动时预解析食材为 frozenset 加速过滤
- 提供 /generate-meal-plan/ 与 /predict/ 两个 API 及交互式文档

## 适用场景

- 根据我的身体数据自动生成一日三餐
- 按自定义热量和营养目标搜索匹配食谱
- 排除/指定食材并按营养值筛选食谱

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L13: A full-stack diet recommendation system that generates personalized meal plans based on user health data (age, weig
> L29: Recipes are embedded as 9-dimensional nutritional vectors (Calories, Fat, Saturated Fat, Cholesterol, Sodium, Carbo

## 星数曲线

```mermaid
xychart-beta
    title "zakaria-narjis/nutrimind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 256 --> 259
    line [257, 258, 258]
```

2026-10-18 257 → 2026-10-30 258（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ccf17dd19049` · [字段定义](../../DATASET.md)*
