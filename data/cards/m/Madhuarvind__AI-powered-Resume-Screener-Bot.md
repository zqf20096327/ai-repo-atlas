# Madhuarvind/AI-powered-Resume-Screener-Bot

⭐ 29 · JavaScript · MIT · 推送 2026-01-05 · [GitHub](https://github.com/Madhuarvind/AI-powered-Resume-Screener-Bot) · 个人维护

**招聘方使用的 AI 简历筛选系统：分析评分并检测偏见**

Flask 后端加 React 前端的简历筛选 Web 应用：上传 PDF/DOCX 简历后调用 OpenAI ChatGPT 或 Google Gemini 进行技能提取、经验评估、相关性评分与三档分类；内置性别/年龄/地区/学历偏见分析与盲简历模式（去除姓名等个人标识），并提供 HR 问答聊天机器人与候选人单独对话。数据存 SQLite，需自备 OpenAI 或 Gemini API key。仓库描述提及 IBM Watsonx，但 README 正文仅写 OpenAI 与 Gemini。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Gemini 双模型简历分析与三档评分
- 四类偏见分析、盲简历模式与偏见缓解建议
- HR 问答助手与候选人单独对话功能
- REST API 覆盖上传、偏见分析、聊天与统计端点

## 适用场景

- 招聘方批量评估候选人简历并获得评分分类
- 启用盲简历模式降低筛选中的个人信息偏见
- 通过对话向 AI 助手查询候选人与统计数据

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L11: - **AI-Powered Analysis**: OpenAI ChatGPT and Google Gemini integration for intelligent candidate evaluation
> L14: - **HR Query Assistant**: AI chatbot for asking questions about candidates and getting insights

## 星数曲线

```mermaid
xychart-beta
    title "Madhuarvind/AI-powered-Resume-Screener-Bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `783c185efcd5` · [字段定义](../../DATASET.md)*
