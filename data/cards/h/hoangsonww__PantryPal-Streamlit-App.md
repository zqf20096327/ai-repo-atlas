# hoangsonww/PantryPal-Streamlit-App

⭐ 15 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/PantryPal-Streamlit-App) · [官网](https://pantrypal-app.streamlit.app) · 个人维护

**输入现有食材与饮食限制，AI 生成菜谱的 Streamlit 网页应用**

基于 Streamlit 构建的网页应用，面向家庭烹饪用户：输入手头食材、选择饮食限制（素食/纯素/无麸质等）与份数（1-12），调用 Google Gemini API 生成含步骤、营养分解、购物清单与配图的菜谱，也提供 Surprise Me 随机菜谱模式。营养数据以 Altair 柱状图与环图可视化，菜谱历史经本地存储跨会话保存，可导出 JSON/Markdown/TXT。运行需自备 Gemini API key 与 Unsplash key，支持 Docker 部署，另提供成分频率与营养汇总的分析脚本。

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

- 按现有食材+饮食限制+份数调用 Gemini 生成菜谱
- 营养柱状/环图可视化与难度估算
- 菜谱历史本地持久化，可导出 JSON/Markdown/TXT
- 提供 Docker Compose 部署与数据分析脚本

## 适用场景

- 根据冰箱里的食材快速决定晚餐做什么
- 有饮食限制（素食/无麸质等）时获取合适菜谱
- 生成菜谱后直接下载购物清单去采购

## 场景标签

 · 领域:生活/饮食应用

## 证据(README 行号)

> L7: Built from the frustration of “what’s for dinner?”, PantryPal combines the power of Google Gemini AI with a sleek, i
> L147:  - Click **Generate Recipe** to fetch from Gemini AI.

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/PantryPal-Streamlit-App 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `7c94c66aa441` · [字段定义](../../DATASET.md)*
