# cwmd2026/mcd-meal-butler

⭐ 55 · Python · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/cwmd2026/mcd-meal-butler) · [官网](https://github.com/cwmd2026/mcd-meal-butler#readme) · 个人维护 · 中文 README

**麦当劳拼单 Agent Skill：一句话点单、算最优价、AA 分账、出海报**

WorkBuddy Skill 形态的麦当劳拼单助手：由 Agent 读取 SKILL.md 指令，把群聊中的大白话点单解析为结构化订单，经麦当劳 MCP（需在 open.mcd.cn 获取 Token 配置连接器）实价查询，自动构造纯券/积分/组合多套方案选最省，按金额占比 AA 分账，并用 scripts/poster.py 生成 9:16 中文开饭海报，可选输出支付链接。零服务器零部署，clone 放入 skills 目录即用；海报脚本仅依赖 Pillow，字体三级兜底。无 Token 时可用 Mock 数据离线演示。为 2026 麦当劳程序员创意开发大赛参赛作品，个人非商业用途免费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 大白话点单解析为结构化订单，经 MCP 实价精算选最省方案
- AA 分账按金额占比分摊优惠，金额守恒（¥75.00 实测）
- poster.py 独立生成 9:16 中文海报，字体三级兜底免自备
- 零服务器零部署，clone 放入 ~/.workbuddy/skills/ 即用，无 Token 可 Mock 演示

## 适用场景

- 群里多人报菜名，3 秒汇总成订单并算出最省组合
- 聚餐后自动 AA 分账并生成可分享的开饭海报
- 攒了麦当劳券和积分，让 Agent 帮算怎么用最划算

## 场景标签

`AI 助手` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L60: 部署一台常驻服务器门槛太高；而且 **Agent 本身就是 LLM**，天然能把大白话点单解析成结构化订单，
> L69: |🗣️ **大白话点单**|随口说"板烧不要生菜""可乐换无糖"，Agent 解析成结构化订单|
> L90: Agent 会走完 解析 → 精算 → 分账 → 海报 → （可选）下单 全流程，最终给出四块内容：


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f7c7455d7f2d` · [字段定义](../../DATASET.md)*
