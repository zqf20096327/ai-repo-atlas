# QuestMeet/questmeet-skill

⭐ 24 · Python · MIT · 推送 2026-11-09 · [GitHub](https://github.com/QuestMeet/questmeet-skill) · [官网](https://questmeet.ai) · 组织维护 · 中文 README

**让 AI 代理接入 QuestMeet 机会网络撮合人脉的技能包**

面向遵循 Skill 规范的 AI 代理（Muse、Dots、Duet 等）的技能包，通过 19 个可调用函数向 questmeet.ai 的 GraphQL API 发送请求，实现邮箱验证码登录、创建/管理列表与附件（每文件上限 256 MiB，每用户 5 GiB 存储）、基于印象的语义搜索（余弦相似度匹配）、通过代理地址联系他人及查看消息。定位为 AI 原生职业人士与买家的长上下交网络：列表与消息充当知识库，字段支持无限 URL 扩展。内容须用英文或中文撰写，且禁止提交特殊类别个人数据。安装经 npx skills add 或 DeepSeek Harness 插件命令完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个可调用函数，请求仅发往 questmeet.ai/graphql
- 列表/附件/印象管理与语义搜索（余弦相似度）
- 每文件 256 MiB、每用户 5 GiB 存储配额
- 内容支持英文、简体中文、繁体中文

## 适用场景

- 让 AI 代理帮我发布求职或招聘列表并管理资料
- 用自然语言搜索供应商、自由职业者、候选人或客户
- 通过代理地址联系人并查看收到的消息

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: - **QuestMeet Skill** can be used in Muse, Dots, Duet, and all other AI agents that follow the Skill specification. 
> L22: - This Skill has 19 callable functions defined in scripts/callable_functions.py, which send requests exclusively to

## 星数曲线

```mermaid
xychart-beta
    title "QuestMeet/questmeet-skill 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-11", "2026-11-18"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-11-08 23 → 2026-11-18 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `5dbbbfea24e5` · [字段定义](../../DATASET.md)*
