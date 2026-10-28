# linkcraftstudio/feedlog

⭐ 191 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/linkcraftstudio/feedlog) · [官网](https://feedlog.ai) · 组织维护 · 中文 README

**面向 SaaS 团队的开源 AI 客服平台：AI 客服+帮助中心+反馈板**

自托管或托管运行的开源 AI 客服平台：内嵌 Widget 供用户提问与提交反馈，基于帮助中心知识库的 AI Agent 回答重复性问题，AI 与人工共用统一收件箱并可按规则触发人工接管；反馈板、路线图与更新日志形成反馈到发布的闭环，相似反馈可检测合并。自托管需 PostgreSQL 17+（vector 扩展）与配置 OpenAI 兼容模型服务（含 OpenAI/Azure/LiteLLM/Ollama）；支持 Docker、Cloudflare Workers、Vercel 部署，并提供 MCP 与 Skills 接入 coding agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库驱动的 AI Agent 回答产品问题并随对话改进
- AI–人工统一收件箱与人工接管规则（账单/账号/隐私等转人工）
- 反馈板+路线图+AI 起草更新日志的闭环，含相似反馈检测合并
- 提供 MCP 与 Skills 供 Claude/Cursor 等 coding agent 接入

## 适用场景

- 把重复性客户咨询交给 AI 回答，团队只处理需人工判断的问题
- 在产品内嵌 Widget 收集问题与功能反馈并公开发布路线图
- 自托管一套客服+帮助中心+反馈管理平台

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: AI-driven customer support with a Widget, a self-improving knowledge base, and a feedback board — cut manual support
> L63: Give your AI Agent the latest product knowledge and context to answer repetitive questions reliably — reducing manu
> L229: |AI|OpenAI-compatible API, including OpenAI, Azure OpenAI, LiteLLM, and Ollama|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `221c9f97e0c4` · [字段定义](../../DATASET.md)*
