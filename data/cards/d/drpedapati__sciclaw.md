# drpedapati/sciclaw

⭐ 89 · Go · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/drpedapati/sciclaw) · [官网](https://sciclaw.dev) · 个人维护

**面向科研人员的配对科学家 AI 助手，可复现研究工作流**

基于 PicoClaw 运行时（Go 单二进制）的科研 agent：通过 Telegram/Discord 或终端与应用对话，连接多家 LLM 提供商，执行文献检索（PubMed、bioRxiv）、手稿撰写（Quarto/pandoc/docx）、文档处理、实验溯源等内置技能，并在本地工作区保留可审计的证据链。默认本地运行、不开放端口、无遥测，API key 存于本地配置。支持 OpenAI/Anthropic/Gemini/OpenRouter/DeepSeek/Groq/智谱等提供商，提供 Homebrew、预编译二进制与源码安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram/Discord 对话式交互，支持后台任务队列与文件附件回传
- 12+ 内置科研技能：PubMed 检索、手稿撰写、docx 审阅、PDF/表格处理、实验溯源
- 本地运行、无遥测、单工作区数据隔离（channel→workspace 路由）
- 跨平台预编译二进制（macOS/Linux/Windows）与 Homebrew 安装

## 适用场景

- 通过 Telegram/Discord 让 AI 助手检索文献并生成引用列表
- 让 agent 起草、润色与审阅科研手稿（docx/PDF/PPT/表格）
- 为每个研究项目分配独立聊天频道与工作区，保留可审计证据链

## 场景标签

`AI 助手` `科研工具` · 领域:对话与助手

## 证据(README 行号)

> L20: sciClaw is a paired-scientist agent for rigorous research work. It connects to major LLM providers, proposes and ex
> L22: Built on the PicoClaw runtime (a Go rewrite of nanobot), sciClaw keeps a single-binary footprint while adding a pai

## 星数曲线

```mermaid
xychart-beta
    title "drpedapati/sciclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 88 --> 91
    line [89, 90, 89]
```

2026-10-18 89 → 2026-10-24 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `8fcdfd835f0e` · [字段定义](../../DATASET.md)*
