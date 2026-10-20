# MadsLorentzen/ai-job-search

⭐ 52,099 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/MadsLorentzen/ai-job-search) · 个人维护

**求职者本地运行的 AI 求职申请框架：评估职位、定制简历与面试准备**

基于 Claude Code CLI 构建的求职申请工作流框架，以命令形式组织：/setup 建立个人档案，/scrape 抓取职位并按匹配度排序，/apply 运行 drafter-reviewer 流程生成 LaTeX 简历与求职信。支持 /interview 面试准备、/rank 批量评分、/outcome 记录进展、/notion-sync 与 /gmail-sync 集成等 13 个命令。核心流程与国家无关，职位门户搜索技能默认面向丹麦市场，可通过 /add-portal 替换为本地招聘网站。要求 Claude Pro/Max 订阅或 Anthropic API 额度，fork 后档案数据会写入受跟踪文件，README 建议使用私有仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.6 天,年发版 10,78 位贡献者
- 涨星:近 1 天 **+2,054**(自 20261016 起算)
- 安装:pypi 包 `pypdf` 月下载 125,991,621
- 平台:WINDOWS / MACOS · 协议:MCP

## 能力要点

- /apply 的 drafter-reviewer 双 agent 流程：起草、评审、修订并强制 PDF 编译
- /add-portal 为任意招聘网站生成搜索技能，核心流程与国家/语言无关
- 13 个命令覆盖评估、投递、面试准备、结果跟踪与学习计划
- 职位描述按不可信输入处理，遵循指令级防护并提示人工复核

## 适用场景

- 批量抓取招聘网站职位并按个人档案评分排序
- 针对具体职位自动生成定制简历和求职信
- 面试前生成阶段化准备材料并模拟面试
- 用本地招聘网站替换默认丹麦门户，适配本国市场

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: An AI-powered job application framework built on Claude Code. Fork it, fill in your profile, and let Claude evaluat
> L34: A structured workflow that turns Claude Code into a full-stack job application assistant. The core workflow (self-p
> L47: - Claude Code (CLI). Claude Code has no free tier: you need a Claude Pro/Max/Team subscription or Anthropic API cre

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `5924e36ffdef` · [字段定义](../../DATASET.md)*
