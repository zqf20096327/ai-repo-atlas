# hardenbr-personal/JobScoutPublic

⭐ 19 · Python · 推送 2026-08-12 · [GitHub](https://github.com/hardenbr-personal/JobScoutPublic) · 个人维护

**AI 求职侦察 agent：每日扫职位板，LLM 筛选，人保留申请权**

Python 编写的求职自动化 agent：每日抓取 Greenhouse/Lever/Ashby 公开 ATS API 及远程职位聚合源，运行确定性硬过滤，再用 Gemini（经 OpenAI 兼容端点调用）做 LLM 分诊，并以代码强制溯源规则——LLM 剔除岗位必须引用 JD 原文；聚合源结果会与实时招聘板复核剔除已关闭岗位。设计上不做投递、不联系任何人，产出每日邮件摘要；可本地运行或用 GitHub Actions 定时执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代码强制的溯源规则：LLM 剔除岗位需引用 JD 原文
- 聚合结果与实时 ATS 招聘板复核剔除已关闭岗位
- 所有被过滤岗位记录原因，可审计
- 通过 GitHub Actions 工作日定时运行并邮件推送摘要

## 适用场景

- 每日自动扫目标公司招聘板并收邮件摘要
- 用 LLM 对岗位做初筛但保留人工决策
- 追踪已关闭或过期职位减少无效申请

## 场景标签

`网页抓取` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: An AI job-search agent that deliberately does NOT apply for you.
> L9: remote-job aggregators, applies deterministic hard filters, runs LLM

## 星数曲线

```mermaid
xychart-beta
    title "hardenbr-personal/JobScoutPublic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e4021033e0b1` · [字段定义](../../DATASET.md)*
