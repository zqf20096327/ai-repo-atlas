# splashdeluxe/ai-job-search-template

⭐ 3 · MIT · 推送 2026-11-10 · [GitHub](https://github.com/splashdeluxe/ai-job-search-template) · 个人维护

**求职者的 Muse agent 求职系统：筛岗、评分、定制CV、一次投递与拒信反馈**

一组 markdown 文件模板，把 Muse agent 变成带规则的求职助手：从官方招聘板抓取职位、按候选档案评分、投前明示差距、每职位生成一份定制 CV 并经 AI 文风检查后投递一次，拒信触发反馈回写档案。无代码、无数据库、无构建步骤，依赖 Muse 的浏览器操作、Gmail/Drive 连接器、Vault 与定时运行，在免费计划上运行，邀请码附带 10 亿 token。CAPTCHA 阻塞时回退到人工完成。

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

- 9 个斜杠命令覆盖 setup 到 outcome 全流程
- 投递前差距简报与一次性核验提交，防重复申请
- 每份生成 CV 经 AI 写作模式扫描并改写
- 拒信反馈循环回写档案与抓取策略

## 适用场景

- 让 agent 定时抓取官方招聘板并生成短期清单
- 每职位生成一份定制 CV 并自动提交一次
- 从拒信中收集原因并转化为学习计划

## 场景标签

`AI 助手` `浏览器自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L13: A job search system for your Muse agent. It sources roles from official careers boards, scores them against your pr
> L47: A set of markdown files that turn Muse into a job application assistant with rules. No code to install, no database
> L182: - It runs inside Muse, Meta's assistant, and works on the free plan. No local install, no coding CLI, no API key.

## 星数曲线

```mermaid
xychart-beta
    title "splashdeluxe/ai-job-search-template 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `70e5eced5612` · [字段定义](../../DATASET.md)*
