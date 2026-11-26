# DHURJATI-JS/employee-management-system

⭐ 3 · HTML · MIT · 推送 2026-11-02 · [GitHub](https://github.com/DHURJATI-JS/employee-management-system) · 个人维护

**自托管 AI 员工管理系统：招聘考勤薪酬聊天一体**

运行在自有服务器上的员工管理系统（FastAPI + PostgreSQL/pgvector + Redis），覆盖招聘审批、考勤（工时内计数与空闲检测）、薪资周期与工资单、任务、群聊与视频会议、九种语言界面及内置商店。AI 为可切换功能：本地 vLLM 运行 Gemma 3 12B（需约 16GB 显存显卡）或 Anthropic Claude（自备 API key），AI 按钮可整体关闭。学生项目，未经审计，MIT 许可，需 Windows 11 与网络连接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 引擎一键切换：本地 vLLM+Gemma 3 或 Claude，ID 照片永不发给 Claude
- 考勤、薪资、任务、视频会议（字幕/AI 笔记）、聊天与商店集成于一个应用
- start.cmd 一键安装：uv、WSL、Docker、Redis/PostgreSQL/ClamAV 容器自动部署
- 邮件加密（AES-256-GCM）、上传文件病毒扫描、九种语言界面

## 适用场景

- 在自己服务器上管理公司的招聘、考勤与薪酬流程
- 数据不出内网地使用本地 AI 助手、会议字幕与翻译
- 用 AI 从简历与历史记录推荐任务人选或晋升名单

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L1: Deminic: AI employee management that runs on your own server
> L3:  Hiring, attendance, payroll, tasks, video meetings, chats and a marketplace in one app.
> L64: - **The local AI** needs an AMD or NVIDIA graphics card with about 16 GB of memory, a current driver, and about 60 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `b2523cb8078d` · [字段定义](../../DATASET.md)*
