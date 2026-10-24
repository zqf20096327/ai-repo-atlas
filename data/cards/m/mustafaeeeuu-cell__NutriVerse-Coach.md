# mustafaeeeuu-cell/NutriVerse-Coach

⭐ 55 · HTML · 推送 2026-10-21 · [GitHub](https://github.com/mustafaeeeuu-cell/NutriVerse-Coach) · 个人维护

**面向个人的 AI 餐饮陪伴应用：按心情与节律推荐食谱**

名为 CogniPlate 的营养/餐饮应用：通过每日打卡记录饥饿感与情绪，结合时间感知与心情自适应逻辑生成食谱与分量建议；提供可拖拽的周餐画布、对话式饮食日志、多语言界面、家庭共享空间与合并购物清单，内置 800+ 食谱库。技术栈为 React/Flutter 前端、Node.js/Express/PostgreSQL 后端、Python+scikit-learn+LSTM 的 ML 微服务（/predict 端点）。仓库为 monorepo，需自行配置 .env 并应用 schema.sql 后运行；声明为决策支持工具而非医疗设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 时间感知与心情自适应的食谱建议（如压力大时推荐富含镁的零食）
- 对话式饮食日志：解析情绪并记录餐食与能量变化
- Python + scikit-learn + 自定义 LSTM 的餐序预测微服务
- 800+ 食谱库与按过道分组的合并购物清单

## 适用场景

- 我想让应用根据心情和时间推荐合适的食谱
- 我想和家人共享一个空间并自动合并购物清单
- 我想用自然语言记录饮食和餐后感受

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L53: |AI Engine|Python, scikit‑learn, custom LSTM for meal‑sequence prediction|
> L71: For the database schema, a `schema.sql` file is provided in `services/db/`. Apply it to your local Postgres instanc

## 星数曲线

```mermaid
xychart-beta
    title "mustafaeeeuu-cell/NutriVerse-Coach 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-24 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `866845947d5c` · [字段定义](../../DATASET.md)*
