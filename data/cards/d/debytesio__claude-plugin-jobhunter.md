# debytesio/claude-plugin-jobhunter

⭐ 14 · Python · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/debytesio/claude-plugin-jobhunter) · [官网](https://docs.debytes.io) · 组织维护

**Claude Code 求职插件：跨 14 平台抓取并 AI 评分输出 Excel 报告**

面向求职者的 Claude Code 插件：并行抓取英法两国 14 个招聘平台，对职位做 JD 增强、8 维度 AI 评分（角色/技能/要求/经验/资历/薪资/地点/签证），并做雇主评级、UKVI 签证赞助核验与中介识别；财务可行性按国家计算税收与社会分摊后估算到手收入。跨平台去重、会话断点续传，最终导出含 5 个工作表的 Excel 报告。首次运行需浏览器认证 DEB Cloud（免费试用，无需信用卡），要求 Python 3.13+ 与 openpyxl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行抓取 UK/France 14 个招聘平台并跨平台去重
- 8 维度 AI 评分与 ATS 级要求匹配
- UKVI 签证赞助核验（140k+ 注册记录）与中介识别
- 按国家计算税收/社保/通勤成本后的到手收入，导出 5 表 Excel 报告

## 适用场景

- 我想批量抓取并按个人条件给求职岗位打分排序
- 申请前核验岗位的实际到手薪资与签证赞助情况
- 生成一份可分享的求职分析 Excel 报告

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: **AI-powered job search for Claude Code**
> L38: /plugin marketplace add debytesio/claude-plugins
> L39: /plugin install job-hunter@debytes

## 星数曲线

```mermaid
xychart-beta
    title "debytesio/claude-plugin-jobhunter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `de1f7d83c747` · [字段定义](../../DATASET.md)*
