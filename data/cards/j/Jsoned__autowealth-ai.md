# Jsoned/autowealth-ai

⭐ 26 · Python · MIT · 推送 2026-06-08 · [GitHub](https://github.com/Jsoned/autowealth-ai) · [官网](https://github.com/Jsoned/autowealth-ai) · 个人维护 · 中文 README

**多智能体个人投资分析引擎：技术/基本面/情绪综合决策**

面向个人投资者的多智能体投资分析引擎：技术分析、基本面分析、情绪分析三个智能体按 35/35/30 权重交叉验证，输出 BUY/HOLD/SELL 信号与置信度。支持 OpenAI API 或本地 LLM（Ollama 地址 localhost:11434）部署，涵盖 12+ 技术指标、马科维茨组合优化、回测、随机森林+MLP 价格预测、5 种实时预警。提供 Python API、CLI、Streamlit 界面、FastAPI Web 服务与 Flutter 移动 App；数据源覆盖 Yahoo Finance、akshare/东方财富与币安。项目声明仅供教育研究，不构成投资建议。

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

- 3 个分析智能体按权重交叉验证并输出带置信度的买卖信号
- 支持本地 LLM 部署（如 llama2）保护数据隐私
- 组合优化、回测系统与随机森林+MLP 机器学习预测
- 多形态交付：CLI / Streamlit / FastAPI / Flutter App

## 适用场景

- 分析股票/加密货币并获取买卖信号参考
- 批量筛选投资标的
- 对策略做回测与组合优化
- 接收价格突破等规则的实时预警通知

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L15: AutoWealth AI 是一款基于**多智能体技术**的智能投资分析引擎。它通过整合技术分析、基本面分析和市场情绪分析，为个人投资者提供专业的投资决策支持。
> L19: - 🤖 **多智能体协作** — 3个专业AI智能体协同工作，交叉验证投资决策

## 星数曲线

```mermaid
xychart-beta
    title "Jsoned/autowealth-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3ba508549eaa` · [字段定义](../../DATASET.md)*
