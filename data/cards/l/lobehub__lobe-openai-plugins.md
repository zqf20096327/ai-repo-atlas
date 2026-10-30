# lobehub/lobe-openai-plugins

⭐ 24 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/lobehub/lobe-openai-plugins) · [官网](https://openai-collections.chat-plugin.lobehub.com) · 组织维护

**LobeChat 的社区 ChatGPT 插件聚合目录（含代理）**

LobeHub 维护的 OpenAI/ChatGPT 插件聚合仓库：从社区筛选插件清单，通过编辑 src/syncList.ts 同步插件 manifest，作为 LobeChat 可用的插件索引（index.json）供用户浏览与安装；插件用于扩展 LobeChat 的 Function Calling 能力与消息渲染方式。本地开发使用 Bun（git clone 后 bun install / bun dev），也可用 GitHub Codespaces 在线开发。周边生态含插件模板、chat-plugin-sdk 与插件网关服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合社区 ChatGPT 插件供 LobeChat 使用
- 通过 src/syncList.ts 同步插件 manifest
- 作为 index.json 插件索引供 LobeChat 读取展示
- 配套插件 SDK、开发模板与 Vercel 部署的插件网关

## 适用场景

- 为 LobeChat 查找可用的 Function Calling 插件
- 开发者参照模板与 SDK 开发 LobeChat 插件
- 通过索引仓库向 LobeChat 用户分发自己的插件

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L1: OpenAI Plugins Directory LobeChat Plugin
> L3: Proxy for selected ChatGPT plugins from community
> L33: - [lobe-chat-plugins][lobe-chat-plugins]: This is the plugin index for LobeChat. It accesses index.json from this r

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-openai-plugins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `73ba725c85ed` · [字段定义](../../DATASET.md)*
