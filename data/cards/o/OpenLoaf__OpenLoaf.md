# OpenLoaf/OpenLoaf

⭐ 110 · TypeScript · AGPL-3.0 · 推送 2026-05-14 · [GitHub](https://github.com/OpenLoaf/OpenLoaf) · [官网](https://openloaf-website.hexems.com/) · 组织维护 · 中文 README

**本地优先的项目式 AI 生产力桌面应用，多代理+文档+邮件日历**

OpenLoaf 是以项目为独立工作区的本地优先 AI 桌面应用（Electron 40 / Next.js 16）。每个项目有专属 AI 代理、三级记忆（用户/项目/链接项目注入）、SKILL.md 技能加载与 MCP 工具接入；主窗口的 Secretary Agent 负责跨项目编排与路由。内置多模型对话（OpenAI/Claude/Gemini/DeepSeek/Qwen/Grok/Ollama 本地模型）、无限画布（AI 生图/生视频）、终端、IMAP 邮件、日历同步、看板与块编辑器。数据全存本地 ~/.openloaf/，自带 API key（BYOK），无遥测；README 声明处于活跃开发期。采用双许可，源码安装需 Node.js 20+ 与 pnpm 10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Secretary/Project/Worker 三层代理架构，自研代理栈而非 Claude Code 封装
- 三级记忆体系与项目链接（记忆与技能跨项目注入）
- 支持 MCP 服务器接入，可导入 Claude Desktop/Cursor/VS Code/Cline/Windsurf 的 JSON 配置
- 多模型对话 + 本地 Ollama 全离线方案，数据 100% 本地存储

## 适用场景

- 每个代码仓库建一个项目，链接共享的编码规范项目保持 AI 行为一致
- 科研写作时把参考文献项目作为知识库链接到论文项目
- 在无限画布上头脑风暴并用 AI 生成图片/视频，配合任务看板跟踪产出
- 个人知识库积累笔记，与工作项目链接让 AI 关联信息

## 场景标签

`AI 助手` `图像生成` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L22: OpenLoaf is a local-first AI productivity desktop app built around **projects as independent workspaces**. Each pro
> L94: Multi-model AI chat supporting **OpenAI**, **Anthropic Claude**, **Google Gemini**, **DeepSeek**, **Qwen**, **xAI G

## 星数曲线

```mermaid
xychart-beta
    title "OpenLoaf/OpenLoaf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-24 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `cc9c5365747c` · [字段定义](../../DATASET.md)*
