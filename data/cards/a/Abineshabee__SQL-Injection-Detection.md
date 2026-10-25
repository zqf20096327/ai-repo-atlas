# Abineshabee/SQL-Injection-Detection

⭐ 41 · CSS · 推送 2026-04-02 · [GitHub](https://github.com/Abineshabee/SQL-Injection-Detection) · 个人维护

**机器学习检测 SQL 注入查询的 Web 与 REST API 系统**

基于 Python、Flask 与 Scikit-learn 的 SQL 注入检测系统：预训练分类模型（my_model.pkl）配合 TF-IDF/NLP 向量化管道（vectorizer.pkl），将输入的 SQL 查询分类为安全或注入，并输出两类概率分数。提供用户注册登录的 Web 界面与 POST /api/check_query 的 REST API，附 api_client.py 客户端脚本，可接入 Web 应用、漏洞扫描器与 DevSecOps 流水线。面向开发者与安全研究人员，安装方式为 git clone 后 pip 安装依赖并运行 app.py。

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

- 预训练 ML 模型 + TF-IDF/NLP 向量化管道分类 SQL 查询
- Flask Web 界面（注册/登录/提交查询/结果展示）
- REST API 返回预测类别与安全/注入概率分数
- 附 api_client.py 演示 API 调用

## 适用场景

- 在执行前检测 SQL 查询是否含注入攻击
- 将检测能力通过 REST API 集成到安全测试工具或 DevSecOps 流水线
- 网络安全研究中的 AI 检测演示与实验

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A **Machine Learning based SQL Injection Detection System** built using **Python, Flask, and Scikit-learn** that det
> L27: * Machine Learning based SQL Injection detection

## 星数曲线

```mermaid
xychart-beta
    title "Abineshabee/SQL-Injection-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d6fe48601504` · [字段定义](../../DATASET.md)*
