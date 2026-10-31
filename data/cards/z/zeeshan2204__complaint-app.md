# zeeshan2204/complaint-app

⭐ 16 · Jupyter Notebook · MIT · 推送 2026-04-21 · [GitHub](https://github.com/zeeshan2204/complaint-app) · [官网](https://complaint-app-y95q.onrender.com/) · 个人维护

**市政投诉分类门户：TF-IDF+逻辑回归自动归类投诉**

Flask 编写的市政投诉 Web 应用，用户提交投诉文本后经 TF-IDF（bigrams）与 Logistic Regression 管道自动分类为 Road、Water、Garbage、Electricity 四类，支持英语与 Hinglish 双语，训练集 120 条样本，自述准确率约 95%。提供公共提交门户与含实时统计、图表的 Admin Dashboard，数据存于内存列表，部署于 Render 并附 render.yaml 配置，本地运行通过 git clone 源码进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TF-IDF + Logistic Regression 四分类投诉管道
- 英语 + Hinglish 双语支持
- Admin Dashboard 含实时统计与图表
- 提供 REST API（/submit-complaint、/complaints、/model-stats）

## 适用场景

- 市民在线提交道路/供水/垃圾/电力类投诉并自动归类
- 管理员通过仪表盘查看投诉统计与分布
- 作为文本分类教学/课程项目参考

## 场景标签

 · 领域:市政科技/NLP 文本分类

## 证据(README 行号)

> L23: - 🤖 **AI Classification** — Automatically detects complaint category
> L50: User Input → TF-IDF Vectorizer → Logistic Regression → Category

## 星数曲线

```mermaid
xychart-beta
    title "zeeshan2204/complaint-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4def287f44ca` · [字段定义](../../DATASET.md)*
