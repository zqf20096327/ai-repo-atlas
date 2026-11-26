# silentco2/LinKit-All

⭐ 5 · Python · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/silentco2/LinKit-All) · [官网](https://silentco2.github.io/LinKit-All/) · 组织维护

**本地运行的 AI 求职工具：找岗位、评匹配、改简历并自动填申请表**

一个运行在用户自己电脑上的开源求职申请工具：从 295 个来源抓取职位并按简历与偏好本地排序（离线识别虚假招聘），对简历做逐词微调（规则拒绝改变雇主、日期、学历等事实的编辑），再通过浏览器自动化填写申请表。支持 ChatGPT/Claude 订阅的 CLI、API key 或 Ollama/LM Studio 本地模型；敏感问题不发给 AI。默认练习模式不点提交；仅 Greenhouse、Lever、Ashby 有专用表单处理器，其余站点走通用表单代理。Windows/macOS/Linux 可用，含全阿拉伯语界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地运行：无账号、无遥测，选本地模型时简历与职位文本不出本机
- 简历逐词微调，规则拒绝改写雇主、头衔、日期、学位或数字
- 敏感问题（签证/薪资/人口统计）由本地档案回答，不送 AI
- 练习模式填表但不提交，295 个职位来源，阿拉伯语界面

## 适用场景

- 自动抓取并按简历匹配排序 Greenhouse/Lever/Ashby/Workday 等平台的职位
- 对每个职位微调简历后自动填写申请表（先练习后真实提交）
- 用 Ollama 本地模型保证简历数据不出本机
- 识别虚假招聘和重复职位

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: Open-source AI job search and auto-apply: it finds jobs, ranks them against your CV, tailors your CV in small checke
> L31: - **Bring any AI.** A ChatGPT plan (Codex CLI), a Claude plan (Claude Code CLI), an API key, or a local model throu
> L66: 2. **Ranks them** against your CV and preferences. Ranking runs locally and costs no AI calls. An offline check fla


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `954801eb34bc` · [字段定义](../../DATASET.md)*
