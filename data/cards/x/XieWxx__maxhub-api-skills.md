# XieWxx/maxhub-api-skills

⭐ 60 · NOASSERTION · 推送 2026-08-24 · [GitHub](https://github.com/XieWxx/maxhub-api-skills) · [官网](https://www.aconfig.cn) · 组织维护 · 中文 README

**给 AI Agent 接入 20 个平台数据的技能集（984 端点）**

遵循 Agent Skills 标准的技能集合，通过统一的 MAXHUB_API_KEY 调用第三方数据服务 MaxHub API，让 Claude Code、OpenClaw 等 Agent 获取抖音、TikTok、B站、小红书、YouTube 等 20 个平台的视频、用户、搜索、直播、评论等数据（共 984 个端点）。采用渐进式加载与语义路由设计，每个 Skill 含 SKILL.md 入口与按功能分类的 API 引用文件。README 明示数据未获各平台官方授权，高风险端点已移除，合规责任由使用者承担，并提供数据使用政策与合规审查清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 个 Skill 覆盖国内外 20 个平台、984 个端点
- 单一 MAXHUB_API_KEY 统一鉴权，遵循 Agent Skills 标准
- 渐进式加载与语义路由设计，按需加载引用文件
- 附数据使用政策与合规审查清单，高风险端点已移除

## 适用场景

- 让 AI Agent 查询抖音/TikTok 等平台的账号与内容数据
- 多步操作如搜用户、查作品、分析评论的链式引导
- 为 Agent 框架扩展社交媒体数据获取能力

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8:  让 AI Agent 轻松接入 20 个主流平台数据 - 一行指令，数据直达
> L19: |🧠 **AI 原生**|遵循 Agent Skills 标准，渐进式加载，语义路由|
> L52: Agent 会自动激活 `maxhub-douyin` Skill 并调用对应 API。

## 星数曲线

```mermaid
xychart-beta
    title "XieWxx/maxhub-api-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-28 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `34ecce6d9f4e` · [字段定义](../../DATASET.md)*
