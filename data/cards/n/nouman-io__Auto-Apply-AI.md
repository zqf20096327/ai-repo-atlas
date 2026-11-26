# nouman-io/Auto-Apply-AI

⭐ 19 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/nouman-io/Auto-Apply-AI) · 个人维护

**为求职者自动匹配并投递职位的多智能体工作台**

面向求职者的自动化工作台：解析上传的简历（PDF/DOCX/TXT），抽取技能与项目并生成 ATS 审计分数；从 LinkedIn、Indeed、Google、Greenhouse 四个来源抓取职位，按简历相关度排序展示；每日最多 15 个投递，有 HR 邮箱时经 Gmail OAuth2 发送邮件，网页表单类申请用 Playwright 自动填写并留存截图证明；申请记录与通知在门户中可查。提供 python start.py 启动与 Docker Compose 部署两种方式，前端 3000 端口、后端 API 8000 端口。

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

- 四来源实时职位发现（LinkedIn/Indeed/Google/Greenhouse）
- 简历与项目匹配评分及 ATS 审计分数
- Playwright 自动填表投递并保存证明截图
- Gmail OAuth2 自动发送 HR 外联邮件

## 适用场景

- 让 AI 按我的简历自动寻找并投递匹配职位
- 在门户里查看每次申请的截图证明与投递状态
- 自动给找到的 HR 邮箱发送求职邮件

## 场景标签

`多智能体` `浏览器自动化` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Real-Time Job Discovery (LinkedIn, Indeed, Google, Greenhouse), Resume &amp; Project Matching, Playwright Web-Form 
> L8: 2. **Resume & Project Extraction**: Extracts skills, experience, education, **projects**, summary, and contact links
> L9: 3. **4-Source Job Discovery**: Connects to **LinkedIn**, **Indeed**, **Google**, and **Greenhouse** using queries de


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `adf6a015ecad` · [字段定义](../../DATASET.md)*
