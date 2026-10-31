# wwxxzz666/Mo-Shen

⭐ 15 · Python · MIT · 推送 2026-08-13 · [GitHub](https://github.com/wwxxzz666/Mo-Shen) · 个人维护 · 中文 README

**面向 Web/微信小程序的多智能体协作小说生成工作台**

基于 AgentScope 2.x 的多智能体小说创作框架，7 个专职 Agent（策划、世界观、角色、大纲、写作、审校、总编）接力完成从创意到成稿的流水线，共享故事状态。提供三档工作流（quick/standard/deep）、200 字试写确认、大纲确认关口、后台任务暂停恢复、故事持久化与局部编辑。以 Python 包安装，支持 DeepSeek/OpenAI/Anthropic/Google 模型切换，交付 Web 工作台、微信小程序与 CLI 三端入口。需 Python 3.11+ 与模型 API Key，v1 的 LangGraph 版保留在历史标签。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个专职 Agent 流水线：策划→世界观→角色→大纲→写作→审校→总编
- 三档工作流 quick/standard/deep，进阶环节按模式启用
- 200 字试写确认与大纲确认关口，后台任务可暂停恢复
- DeepSeek/OpenAI/Claude/Gemini 多模型切换，可本地部署

## 适用场景

- 让多个 AI 智能体协作生成长篇小说并保持人设一致性
- 在 Web 工作台或微信小程序中管理试写、大纲确认与逐章生成
- 通过 CLI 一条命令生成指定章节数与字数的小说初稿

## 场景标签

`多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L21: > **墨神 v2.0.2** 把「写小说」拆成专业流水线：**策划 → 世界观 → 角色 → 大纲确认 → 写作 → 审校 → 总编**。
> L24: > 本分支多智能体编排使用 **AgentScope 2.x**。
> L234: - **🤖 AgentScope 多智能体协作** — 7 个专职 Agent 接力，状态共享、环节清晰

## 星数曲线

```mermaid
xychart-beta
    title "wwxxzz666/Mo-Shen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `16bc83b7e9c7` · [字段定义](../../DATASET.md)*
