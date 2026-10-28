# jonathanrao99/Inventory-Management-System

⭐ 31 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/jonathanrao99/Inventory-Management-System) · [官网](https://ai-inventory-dashboard.vercel.app) · 个人维护

**Flask 库存管理 Web 应用：CSV 上传、分析与补货预测**

基于 Flask 的库存管理系统：拖拽上传 CSV 后提供 KPI 总览、低库存补货提醒、过期预警、按行收入与头尾动销分析（Chart.js 可视化），并可用 scikit-learn 基于近期库存水平生成预测。预测功能的 ML 依赖为可选安装（requirements-ml.txt）。支持本地运行或设置 VERCEL 环境变量部署到 Vercel，需 Python 虚拟环境与 pip 安装依赖，附示例数据文件。面向需要轻量库存分析的小型用户，无登录与企业功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽上传 CSV，生成 KPI、补货提醒与过期预警
- scikit-learn 训练的库存水平预测（可选 ML 依赖）
- Chart.js 基于真实数据的收入与动销可视化
- 本地运行或 Vercel 部署，VERCEL 变量自动切换路径

## 适用场景

- 上传销售 CSV 查看低库存与临期商品
- 基于近期库存水平获取补货预测
- 在本地或 Vercel 上快速搭建库存看板

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: IMS is a Flask app that turns a boring CSV into something you can actually use: who's low on stock, what's about to 
> L18: |🔮 **Forecast**|Three recent stock levels in, one estimate out (scikit-learn)|
> L35: > **Want forecasting?** Pull in the ML extras:

## 星数曲线

```mermaid
xychart-beta
    title "jonathanrao99/Inventory-Management-System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8b4b025ccbe3` · [字段定义](../../DATASET.md)*
