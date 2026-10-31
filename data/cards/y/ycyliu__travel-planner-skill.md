# ycyliu/travel-planner-skill

⭐ 20 · HTML · MIT · 推送 2026-03-19 · [GitHub](https://github.com/ycyliu/travel-planner-skill) · 个人维护 · 中文 README

**为 WorkBuddy/CodeBuddy 生成小红书风格 HTML 旅行攻略的技能**

面向 WorkBuddy / CodeBuddy（或兼容 AI Agent 环境）的 Agent Skill：用户输入目的地、天数与偏好后，自动执行信息研究、路线规划与 HTML 攻略页面生成。信息研究优先从小红书搜索真实用户反馈（需配合 xiaohongshu-mcp），再以公开搜索补充验证。生成页面含路线总览、每日行程、预约准备、三档预算预估等板块，全内联 CSS 无外部依赖，适配桌面/移动端并可打印为 PDF。安装方式为克隆到 skills 目录，以关键词触发。

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

- 小红书优先研究：覆盖攻略/避坑/费用/拍照等维度，深挖笔记正文与评论区
- 一键生成流程：需求确认 → 信息研究 → 路线规划 → HTML 生成 → 预览
- 自动计算经济/舒适/豪华三档预算，含机票酒店门票餐饮明细
- 生成页面全内联 CSS 自包含，支持打印导出 PDF

## 适用场景

- 让 AI Agent 帮我规划旅行路线并生成可打印的攻略页面
- 出行前参考小红书真实用户反馈避坑和估算预算
- 按偏好定制多日行程安排与预约清单

## 场景标签

 · 领域:旅行规划/Agent 技能

## 证据(README 行号)

> L3: **旅行路线规划与精美攻略生成** — 一个为 WorkBuddy / CodeBuddy 设计的 AI Agent Skill。
> L7: - 根据用户需求（目的地、天数、偏好），自动研究目的地信息并生成精美的 HTML 旅行攻略

## 星数曲线

```mermaid
xychart-beta
    title "ycyliu/travel-planner-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `32690701444d` · [字段定义](../../DATASET.md)*
