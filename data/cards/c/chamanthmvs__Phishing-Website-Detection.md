# chamanthmvs/Phishing-Website-Detection

⭐ 209 · Jupyter Notebook · 推送 2026-09-05 · [GitHub](https://github.com/chamanthmvs/Phishing-Website-Detection) · [官网](https://chamanthmvs.github.io/Phishing-Website-Detection/) · 个人维护

**用随机森林对 URL 做钓鱼网站分类的 Streamlit 应用**

面向实验与教育用途的机器学习项目：提取 URL 长度、重定向、IP 地址、子域名数量、短链服务、HTTPS token、DNS 与域名注册信息等特征，输入已训练的随机森林分类器，在 Streamlit 界面中输出 Legitimate 或 Phishing 判定并展示所用特征值。仓库包含应用代码、特征提取逻辑、已保存模型、训练 notebook 与原始 URL 数据集，可本地以 venv + requirements.txt 安装并用 streamlit run 启动。README 明确声明其预测不应视为网站安全性的保证。

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

- 基于 URL 特征的随机森林二分类（Legitimate/Phishing）
- 提取 URL 长度、重定向、IP、子域名、短链、DNS/注册信息等信号
- Streamlit 界面展示预测结果与所提取的特征值
- 包含可复现的训练 notebook 与原始数据集

## 适用场景

- 输入 URL 快速查看钓鱼分类判定与依据特征
- 学习 URL 特征提取与随机森林分类的完整流程
- 复现模型训练并开展自己的实验

## 场景标签

 · 领域:网络安全/机器学习

## 证据(README 行号)

> L3: Phishing Website Detection is a machine learning project that classifies URLs as legitimate or potentially phishing.
> L27: These features are passed to a trained Random Forest classifier. The application then displays the resulting classi

## 星数曲线

```mermaid
xychart-beta
    title "chamanthmvs/Phishing-Website-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 208 --> 210
    line [209, 209]
```

2026-10-18 209 → 2026-10-22 209（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fccc03b684ac` · [字段定义](../../DATASET.md)*
