# chenyu152/BossFlow

⭐ 27 · Python · 推送 2026-08-26 · [GitHub](https://github.com/chenyu152/BossFlow) · 个人维护 · 中文 README

**本地优先的 AI 求职工作台：采集管理 BOSS 直聘岗位、定制简历与面试准备**

面向个人求职者的本地化工作台，Python/FastAPI 后端加 React 前端，含 Windows Electron 桌面版。功能覆盖 BOSS 直聘岗位自动化采集与规则过滤粗评、个人求职记录同步、JD 与履历证据链核对（区分已有证据/待确认/技能缺口）、多格式简历导入、经人工勾选确认的 LLM 简历优化建议、能力覆盖报告与 STAR 面试故事库。内置 Streamable HTTP 与 stdio 桥接的 MCP Server，供 Claude Code、Trae、Codex 等 Agent 调用岗位与简历数据。所有数据（岗位库、简历、证据、Cookie）存放本机，LLM 生成内容需用户确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BOSS 直聘自动化采集与多城市/关键词/黑名单规则过滤粗评
- JD 与履历证据链核对，区分已有证据、待确认与技能缺口
- LLM 优化建议需人工勾选确认，仅确认事实写入定制简历
- 内置 MCP Server（Streamable HTTP & stdio）与 3 套 Agent Skills

## 适用场景

- 集中采集和管理 BOSS 直聘岗位并自动粗评分数
- 针对不同求职方向隔离维护简历与证据，生成定制简历
- 基于真实经历准备面试并沉淀 STAR 故事库
- 通过 Claude Code 等 Agent 以 MCP 调用求职数据

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L3: **本地优先的 AI 求职工作台 | Local-First AI Job Search Workbench**
> L24: - 🔍 **事实约束型 AI**：AI 绝不假造未确认的经历，每一条简历建议与面试准备都严格基于你的实际证据。
> L66: 内置 Streamable HTTP & stdio 桥接 MCP Server，支持 Claude Code, Trae 等工具直接调用岗位、简历与技能面板。

## 星数曲线

```mermaid
xychart-beta
    title "chenyu152/BossFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d7bce9827410` · [字段定义](../../DATASET.md)*
