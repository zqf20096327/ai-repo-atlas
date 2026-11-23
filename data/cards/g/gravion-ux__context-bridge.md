# gravion-ux/context-bridge

⭐ 4 · JavaScript · MIT · 推送 2026-11-01 · [GitHub](https://github.com/gravion-ux/context-bridge) · 组织维护

**为 AI 辅助编码会话生成含密钥脱敏的 Markdown 交接文档**

VS Code 扩展，用于在聊天结束、换模型或换 agent 时把工作上下文写成结构化 Markdown 交接文档。用户回答一组固定问题（目标、现状、决策、下一步、阻塞），扩展收集有界的项目文件列表、可选的只读 git status/log、可选的编辑器摘录，经尽力而为的密钥模式替换后保存到 .gravion/handoffs/。自由文本被转义以防提示注入，文件名带毫秒时间戳且独占创建。本地优先：无遥测、不调用任何模型提供商、不上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 问答式生成交接文档，含目标/决策/下一步/阻塞等结构化章节
- 有界工作区文件列表与只读 Git 上下文，跳过 node_modules、.env、密钥文件等敏感路径
- 尽力而为的常见密钥模式替换与防注入的 Markdown 渲染（转义+围栏）
- 本地优先：无遥测、无模型调用、自动加入 .gitignore

## 适用场景

- 切换 AI 模型或 agent 时把会话上下文带入新会话
- 团队协作中向接手者传递项目决策与未完成工作
- 分享 AI 会话上下文前自动脱敏凭据

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Create privacy-conscious Markdown handoffs that carry an AI-assisted coding session forward.
> L32: - **Local-first** — no telemetry, no model-provider calls, no automatic upload.
> L124: - No AI provider is contacted. The extension never sends your code anywhere.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `a8227a4dd650` · [字段定义](../../DATASET.md)*
