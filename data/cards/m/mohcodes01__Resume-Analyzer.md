# mohcodes01/Resume-Analyzer

⭐ 13 · TypeScript · Apache-2.0 · 推送 2026-07-10 · [GitHub](https://github.com/mohcodes01/Resume-Analyzer) · 个人维护 · 中文 README

**面向求职者的 AI 简历定制工具：按职位描述生成匹配简历**

Resume Matcher 是一个自托管 Web 应用：上传主简历（PDF/DOCX）、粘贴目标职位描述后，由 LLM 生成针对该职位的定制简历内容、求职信与面试准备材料，并提供简历与职位的匹配评分、关键词高亮与改进建议；支持拖拽调整段落、多套模板选择与 PDF 导出。后端为 FastAPI + LiteLLM，支持 Ollama 本地模型及 OpenAI、Anthropic、Gemini、OpenRouter、DeepSeek 等云端服务商，提供官方 Docker 镜像，界面含简体中文等多语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按职位描述生成定制简历、求职信与面试准备
- 简历匹配评分、关键词高亮与改进建议
- 支持 Ollama 本地模型及多家云端 LLM 服务商
- 官方 Docker 镜像（linux/amd64、linux/arm64）与多语言界面（含简体中文）

## 适用场景

- 求职者为不同岗位快速定制简历与求职信
- 检查简历与目标职位描述的关键词匹配情况
- 本地 Ollama 环境下离线生成简历内容

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: The AI harness to build tailored resumes for each job application with Claude, ChatGPT, DeepSeek, Kimi, GLM, Gemma, 
> L38: 3. **Review** AI-generated improvements and tailored content
> L113: Paste in a job description and get AI-powered resume tailored for that specific role.

## 星数曲线

```mermaid
xychart-beta
    title "mohcodes01/Resume-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c9c6ad667cc6` · [字段定义](../../DATASET.md)*
