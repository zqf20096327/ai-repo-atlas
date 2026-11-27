# MohammedNeana/ApplyCrew

⭐ 4 · HTML · MIT · 推送 2026-11-25 · [GitHub](https://github.com/MohammedNeana/ApplyCrew) · 个人维护

**求职者输入 Start，AI agent 群自动找职位并填表投递**

运行在 Claude Code 中的 AI agent 协作项目：在用户自己的浏览器与账号下执行求职流程，覆盖职位发现（LinkedIn、公司招聘页、job boards 等）、表单自动填写（Greenhouse、Lever、Ashby 等平台）、基于用户 CV 生成每题答案、记录每次投递与回复、邮件/电话提醒面试，以及本地 dashboard 展示。无服务器、无注册，数据留在本地文件夹。首次真实运行记录为两天内经 13 个渠道投递 264 份申请。限制：消耗用户 Claude 订阅额度，运行期间电脑需保持开机，自动化可能违反求职网站条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 协作完成职位搜索、表单填写与答案撰写
- 检查收件箱与垃圾邮件并记录雇主回复，面试时邮件/电话提醒
- 答案全部溯源至用户 CV，不编造内容，首页展示前 3 份申请由用户确认
- 本地 dashboard 汇总所有申请状态与地图

## 适用场景

- 不想重复填写同类求职表单的任意职业求职者
- 投递后自动追踪各家公司的回复与拒信
- 面试前生成针对该公司的准备材料与模拟面试

## 场景标签

`多智能体` `浏览器自动化` · 领域:Agent 开发

## 证据(README 行号)

> L10: **ApplyCrew is a crew of AI agents that does the repetitive part for you, in your own browser, with your own accoun
> L16: 1. Install the Claude desktop app, and sign in. A paid plan is needed for real use.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ecb240bf9470` · [字段定义](../../DATASET.md)*
