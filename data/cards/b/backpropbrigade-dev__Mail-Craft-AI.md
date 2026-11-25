# backpropbrigade-dev/Mail-Craft-AI

⭐ 3 · TypeScript · 推送 2026-10-23 · [GitHub](https://github.com/backpropbrigade-dev/Mail-Craft-AI) · [官网](https://ai-email-generator-wine.vercel.app/) · 组织维护

**面向邮件撰写者的 AI 邮件生成器，输入信息生成邮件并可导出**

React + TypeScript 前端与 FastAPI + Groq 后端组成的全栈应用：用户填写目的、收件人、语气、长度、要点等表单项，后端调用 Groq 大语言模型生成带主题的完整邮件。前端提供一键复制、jsPDF 导出 PDF、加载动画与错误提示，界面为响应式设计。安装需克隆仓库、npm 启动前端、Python 虚拟环境运行 uvicorn 后端，并在 .env 中配置 GROQ_API_KEY。README 另附学习总结与未来改进清单（模板、历史记录、认证等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Groq LLM 的邮件生成，支持目的/收件人/语气/长度/要点定制
- 生成结果一键复制与导出为 PDF
- 响应式界面，适配桌面/平板/移动端
- 生成失败时的用户友好错误提示

## 适用场景

- 快速生成求职、客服等场景的专业邮件
- 按语气和长度定制邮件内容
- 将生成的邮件导出 PDF 存档

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: MailCraft AI is a modern AI-powered email generation platform that helps users create professional, personalized em
> L18: The application combines a premium React frontend with a FastAPI backend powered by Groq AI to deliver fast, intell

## 星数曲线

```mermaid
xychart-beta
    title "backpropbrigade-dev/Mail-Craft-AI 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-25 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c5ad9979c2b6` · [字段定义](../../DATASET.md)*
