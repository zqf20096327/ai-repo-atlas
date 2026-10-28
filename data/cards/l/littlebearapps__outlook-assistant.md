# littlebearapps/outlook-assistant

⭐ 39 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/littlebearapps/outlook-assistant) · [官网](https://littlebearapps.com/builds/outlook-assistant) · 个人维护

**让 AI 助手经 MCP 直接管理 Outlook 邮件/日历/联系人的服务器**

通过 Model Context Protocol 将 AI 客户端连接到 Microsoft Outlook（个人 Outlook.com 与工作/学校 Microsoft 365 账户），提供 22 个工具覆盖邮件搜索与阅读、带干跑预览与安全控制的发信、草稿、日历、联系人、文件夹、收件箱规则、邮箱设置、共享邮箱读取、增量 delta 同步与批量导出（EML/MBOX/Markdown/JSON/CSV/HTML）。安全机制包括 MCP 工具注解、只读模式、收件人白名单与发送前 mail tips。限制：个人账户全文搜索有限（采用多级回退），共享邮箱不支持发送，会议室搜索需管理员同意。以 npm 包形式安装运行。

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

- 22 个工具覆盖邮件/日历/联系人/规则/设置/共享邮箱
- 发信安全控制：dry-run 预览、收件人白名单、会话限速、发送前 mail tips
- delta sync 增量收件箱监控，适合 agent 轮询场景
- OUTLOOK_READ_ONLY 只读模式与逐工具 MCP 安全注解

## 适用场景

- 在对话中让 AI 助手搜索、阅读、起草并发送 Outlook 邮件
- 用 AI 管理日历会议、联系人与收件箱规则
- 分析邮件原始头（DKIM/SPF/DMARC）排查钓鱼与投递问题
- 批量导出邮件或会话线程归档

## 场景标签

 · 领域:AI 助手集成/邮件自动化

## 证据(README 行号)

> L5:  MCP server for Outlook email, calendar, and contacts — let your AI assistant manage your inbox directly from the co
> L14: Outlook Assistant connects AI assistants to your Microsoft Outlook account through the Model Context Protocol. Ask 

## 星数曲线

```mermaid
xychart-beta
    title "littlebearapps/outlook-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `89f1cb87576f` · [字段定义](../../DATASET.md)*
