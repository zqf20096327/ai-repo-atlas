# lobehub/chat-plugin-search-engine

⭐ 46 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/lobehub/chat-plugin-search-engine) · [官网](https://search-engine.chat-plugin.lobehub.com) · 组织维护

**LobeChat 插件：接入 SerpApi 搜索引擎供对话调用**

面向 LobeChat 的 Function Calling 插件，封装 SerpApi 搜索引擎，用户在 LobeChat 插件设置页安装后即可让模型调用搜索引擎获取结果。属于 LobeChat 插件生态的一部分，配套有插件索引仓库、插件模板、chat-plugin-sdk 与部署在 Vercel 的插件网关。本地开发支持 GitHub Codespaces，或通过 git clone 后用 bun 安装依赖并启动。以 MIT 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 SerpApi 搜索引擎为 LobeChat Function Calling 插件
- 在 LobeChat 插件设置页一键安装
- 提供 bun 本地开发流程（clone/install/dev）

## 适用场景

- 让 LobeChat 对话中调用搜索引擎获取实时信息
- 作为插件开发模板的参考实现

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L28: This is a function calling plugin for Lobe Chat, you can install it in plugin setting page.
> L34: Plugins provide a means to extend the Function Calling capabilities of LobeChat. They can be used to introduce new 

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/chat-plugin-search-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e58b5de5f10e` · [字段定义](../../DATASET.md)*
