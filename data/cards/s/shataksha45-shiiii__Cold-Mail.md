# shataksha45-shiiii/Cold-Mail

⭐ 4 · JavaScript · MIT · 推送 2026-11-05 · [GitHub](https://github.com/shataksha45-shiiii/Cold-Mail) · [官网](https://coldmail-cpw0.onrender.com) · 个人维护

**给求职者：从简历研究联系人并起草个性化外联邮件的 AI Agent**

读取用户简历生成结构化档案，按目标职位搜索招聘负责人/创始人，按信任顺序查找邮箱（公开页面→Apollo→Hunter→模式推测）并标注可信度，围绕每位联系人的具体成果起草个性化邮件；用户在界面上逐封审阅、编辑或批准后经本人 Gmail 发送并记录去重。每日发送上限 50 封。分笔记本版（本地运行 Claude Code，邮件进 Gmail 草稿箱）和网站版（多用户、Postgres、Render 部署）两个分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按信任顺序查找联系人邮箱并为每条标注可信级别
- 每个人物与 hook 附带可打开的来源 URL，输出经 schema 校验
- 人工逐封审阅批准后才发送，Gmail 仅申请 send-only 权限
- 网站版由本地笔记本 worker 承担 AI 搜索，托管成本为零

## 适用场景

- 申请实习/工作时向目标团队的负责人发送个性化自我推荐邮件
- 控制外联节奏：每天限量、每封亲自过目后再发出
- 本地保留全部数据，不经过第三方服务器处理简历与联系人

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L49: - **The research is an AI agent.** Claude follows a written playbook: confirm each person from a real page, collect
> L21: 4. **Writes each email** around that person: it opens with their hook and features the 1–2 resume items closest to 
> L22: 5. **You review** every postcard on the desk: edit, approve or set aside.

## 星数曲线

```mermaid
xychart-beta
    title "shataksha45-shiiii/Cold-Mail 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-12", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d30b70ed7d56` · [字段定义](../../DATASET.md)*
