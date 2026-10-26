# JeevansSP/resume-optimizer

⭐ 38 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/JeevansSP/resume-optimizer) · 个人维护

**求职者上传 PDF 并粘贴职位描述，AI 生成 ATS 优化简历并编译为 PDF**

开源 AI 简历定制服务：用户上传 PDF 简历，pdfplumber 抽取文本后由 Gemini Flash 结构化为个人档案，粘贴职位描述后由 Gemini Pro 生成关键词优化的定制简历，再经 LaTeX（pdflatex + 自定义 resume.cls）编译为 PDF。附带免费简历吐槽（Resume Roast，含 8 项 ATS 检查清单与分享链接）、基于 Google ADK 的对话式简历编辑 Agent、积分与支付系统、多租户与管理后台。后端 FastAPI + PostgreSQL，前端 Vue 3，需 Python 3.12+、TeX Live 与 Gemini API key。

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

- Gemini Pro 按职位描述生成 ATS 优化的定制简历
- LaTeX（pdflatex + 自定义 resume.cls）编译 PDF
- Google ADK 驱动的对话式简历编辑 Agent（JSON Patch 编辑、编辑后自动重编译）
- 免费 Resume Roast：AI 吐槽 + 8 项 ATS 就绪检查清单 + 公开分享链接
- 积分系统（每日免费额度 + Razorpay 购买）与多租户管理后台

## 适用场景

- 针对具体职位 JD 快速定制简历并生成 ATS 友好的 PDF
- 免费获取简历的 ATS 就绪度分析与可分享的吐槽报告
- 通过对话让 AI 修改简历内容并自动重新编译 PDF

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Open-source AI-powered resume tailoring service. Upload your PDF resume, paste a job description, and get an ATS-opt
> L18: **Phase 1 — AI Generation:** Your structured profile + the job description go to Gemini Pro, which produces a tailo
> L34: - **AI Resume Tailoring** — Gemini Pro tailors your resume for each specific job description

## 星数曲线

```mermaid
xychart-beta
    title "JeevansSP/resume-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6dd639beb2ec` · [字段定义](../../DATASET.md)*
