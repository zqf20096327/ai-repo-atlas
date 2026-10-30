# hoangsonww/Spot-the-Scam-AI-Job-Fraud

⭐ 16 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/Spot-the-Scam-AI-Job-Fraud) · [官网](https://hoangsonww.github.io/Spot-the-Scam-AI-Job-Fraud/) · 个人维护

**面向招聘欺诈检测的全栈 ML 系统：校准风险评分与审查队列**

端到端招聘欺诈检测系统：离线训练管线在 TF-IDF 文本特征与 25 个表格特征上训练逻辑回归、SVM、LightGBM、XGBoost 及可选 DistilBERT 微调，经 Platt/Isotonic 校准后按阈值与灰区策略输出 legit/fraud/review 决策；在线部分由 FastAPI 服务加载 artifacts 提供预测、洞察、审查队列与 SSE 流式聊天端点，Next.js 仪表盘提供评分、triage 与 AI 分析页面。当前胜出模型为 ensemble_top3（校准误差 ECE 0.0066）。提供 Docker Compose 与本地 pip/npm 两条安装路径，训练数据来自两个 Kaggle 数据集（约 1.79 万行，欺诈率 4.84%）。

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

- 校准概率 + 灰区路由的 legit/fraud/review 三态决策
- FastAPI 服务含预测、洞察、审查队列与流式聊天端点
- 训练管线覆盖多模型族 + Optuna 调参 + ONNX/MLflow 导出
- 人工反馈可回流重训（make retrain-with-feedback）

## 适用场景

- 对招聘帖做欺诈风险打分并查看可解释依据
- 模糊案例进入人工审查队列做 triage 与反馈回流
- 在仪表盘中通过 AI 聊天助手分析可疑职位帖

## 场景标签

`网络安全` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L38: Spot the Scam is a full-stack, uncertainty-aware fraud detector for job postings. It combines calibrated classical 
> L50: - A FastAPI service exposes predictions, insights, review queues, and chat.
> L415: - A calibrated probability

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/Spot-the-Scam-AI-Job-Fraud 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7655b1443754` · [字段定义](../../DATASET.md)*
