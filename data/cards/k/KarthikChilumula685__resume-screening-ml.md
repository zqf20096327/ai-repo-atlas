# KarthikChilumula685/resume-screening-ml

⭐ 19 · Python · 推送 2026-03-08 · [GitHub](https://github.com/KarthikChilumula685/resume-screening-ml) · [官网](https://resume-screening-ml-rkwj.onrender.com) · 个人维护

**上传简历 PDF 预测最适配岗位的 ML 网页应用**

基于 Streamlit 的网页应用：用户上传 PDF 简历，系统用 pdfplumber 提取文本，经清洗与 TF-IDF 向量化后，由 Logistic Regression 分类模型预测最适配的岗位类别，并展示预测置信度与各岗位概率图表。流程为克隆仓库、pip 安装依赖、运行 train_model.py 训练并生成 pkl 模型文件、streamlit run 启动。作者为 B.Tech CSE 学生，项目部署于 Render，提供在线 Demo。BERT 等深度学习为未来计划，当前未实现。

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

- PDF 简历文本提取（pdfplumber）与清洗预处理
- TF-IDF + Logistic Regression 的岗位分类预测
- 展示预测置信度与概率分布图表
- 提供 Render 在线 Demo 与部署步骤

## 适用场景

- 上传简历快速得到适配岗位类别的预测
- 查看候选岗位的概率分布辅助求职方向判断
- 作为 Streamlit + scikit-learn 分类项目的学习参考

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: An intelligent **Machine Learning web application** that analyzes uploaded resumes and predicts the most suitable jo
> L20: * 🧠 Uses **Machine Learning model** for job role prediction

## 星数曲线

```mermaid
xychart-beta
    title "KarthikChilumula685/resume-screening-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6b747a10cf53` · [字段定义](../../DATASET.md)*
