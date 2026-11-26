# petarzarkov/gemini-code-review-action

⭐ 10 · TypeScript · MIT · 推送 2025-12-06 · [GitHub](https://github.com/petarzarkov/gemini-code-review-action) · 个人维护

**用 Gemini 自动评审 GitHub PR 的 Action**

一个 GitHub Action，在 pull request 事件触发时读取代码 diff，连同之前的评审对话历史一起发送给 Google Gemini，生成评审评论并发布到对应代码行。支持会话连续性（跨多次 PR 评审记住此前讨论）、触发限流时自动降级到更快的模型、可配置文件排除规则、模型、响应语言及是否跳过草稿 PR。配置需在仓库 workflow YAML 中引入，并设置 GEMINI_API_KEY 与 GITHUB_TOKEN 两个 secrets。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PR 事件触发自动评审，评论直接发布到相关代码行
- 会话连续性：跨多次评审保留上下文、避免重复反馈
- 限流时自动降级到更快的 Gemini 模型
- 输入项可配置排除文件、模型、评审响应语言

## 适用场景

- 在 GitHub 仓库 PR 上自动获得 AI 代码评审评论
- 配合草稿 PR 工作流，在标记 ready for review 时触发评审
- 让评审回复使用指定语言

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: This GitHub Action uses Google's powerful Gemini family of models to perform an automated, AI-powered code review on
> L34: 3. **AI Review**: Sends code to Gemini AI with specialized prompts that include conversation context
> L55: |`model`|The Gemini model to use for code review. See available models.|`gemini-3-pro-preview`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `140c7946c5ec` · [字段定义](../../DATASET.md)*
