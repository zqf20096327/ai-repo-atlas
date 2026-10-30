# mage-os-lab/module-admin-assistant

⭐ 21 · PHP · MIT · 推送 2026-07-21 · [GitHub](https://github.com/mage-os-lab/module-admin-assistant) · 组织维护

**Magento 2 管理后台 AI 助手模块：聊天问答与安全 SQL 查询**

面向 Magento 2（Mage-OS）的管理后台扩展模块，在后台左侧边栏提供聊天机器人 UI，管理员可直接提问获取回答。核心功能包括：AI 聊天集成、与 agents/bots/callbacks 交互的接口定义、文档嵌入生成以增强提示词、自动化测试集生成、带安全措施的安全 SQL 查询处理与执行、根据问题自动建议相关链接并跳转。通过 composer 安装，需在后台配置 LLM provider 与 host URL/API 凭证，并运行 assistant:train 命令加载 Magento 领域知识。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台侧边栏聊天机器人 UI，直接提问获取回答
- 带内置安全措施的 SQL 查询处理与执行
- 文档嵌入生成以增强 AI 提示词
- 一键根据提问建议相关链接并跳转

## 适用场景

- Magento 2 管理员通过对话查询店铺数据与后台操作
- 安全地用自然语言执行后台 SQL 查询
- 让管理员快速跳转到与问题相关的后台页面

## 场景标签

`聊天机器人` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: - **🚀 AI Chatbot Integration:** Enhance admin experience with an intuitive chatbot UI.
> L24: enable this feature, select your LLM provider and put in the LLM host url and/or API credentials

## 星数曲线

```mermaid
xychart-beta
    title "mage-os-lab/module-admin-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ec773ff2f21e` · [字段定义](../../DATASET.md)*
