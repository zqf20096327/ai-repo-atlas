# ali-faraz-py/DiabetesDetector

⭐ 26 · JavaScript · 推送 2026-09-07 · [GitHub](https://github.com/ali-faraz-py/DiabetesDetector) · [官网](https://diabetes-detector.vercel.app/) · 个人维护

**面向大众的糖尿病风险预测 Web 应用（随机森林+FastAPI+Next.js）**

基于 Pima Indians Diabetes 数据集训练的随机森林分类器（scikit-learn，自述约 80.5% 准确率），从 8 项临床指标估算糖尿病风险的 Web 应用。后端 FastAPI 暴露 /predict 接口并附带预训练 model.pkl，前端 Next.js 提供输入表单、人群均值对比、会话历史、纯文本报告下载，以及高风险结果下按浏览器定位推荐附近内分泌科医生（巴基斯坦用 Oladoc，其他地区用 Google Maps）。本地部署需分别启动后端 venv/pip/uvicorn 与前端 npm install/run dev，并配置 NEXT_PUBLIC_API_URL。模型训练过程在 Notebook 中提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 随机森林分类器基于 8 项临床指标预测风险，自述约 80.5% 准确率
- 人群均值对比、会话历史与可下载纯文本报告
- 高风险结果下基于浏览器定位推荐附近内分泌科医生
- FastAPI 后端暴露 /predict，附预训练 model.pkl

## 适用场景

- 输入临床指标快速估算糖尿病风险并获得对比参考
- 高风险结果时查找附近内分泌科医生
- 作为 FastAPI+Next.js 的机器学习部署示例学习

## 场景标签

 · 领域:医疗健康/预测分析

## 证据(README 行号)

> L9: * **AI-powered predictions** — a **Random Forest Classifier** (scikit-learn) trained on the Pima Indians Diabetes Da
> L19: * **Model:** Random Forest Classifier, ~80.5% accuracy, trained on the Pima Indians Diabetes Database

## 星数曲线

```mermaid
xychart-beta
    title "ali-faraz-py/DiabetesDetector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ec057ab590e7` · [字段定义](../../DATASET.md)*
