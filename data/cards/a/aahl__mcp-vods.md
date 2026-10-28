# aahl/mcp-vods

⭐ 27 · Python · MIT · 推送 2026-02-25 · [GitHub](https://github.com/aahl/mcp-vods) · [官网](https://zread.ai/aahl/mcp-vods) · 个人维护 · 中文 README

**影视搜索 MCP 服务器：为 AI 提供追剧播放地址检索与电视播放**

面向 Binge-watch/MoonTV/LunaTV 影视源的 MCP 服务器，向 AI 客户端提供搜索影视播放地址的工具能力，并支持通过小米电视（MITV_*）或安装 TvBox 的安卓电视（TVBOX_*）直接播放。订阅源配置、缓存 TTL、搜索站点数等经环境变量设置，可对接已部署的 LunaTV/MoonTV 实例。安装途径包括 uvx、Docker Compose 与 Home Assistant OS Add-on，可添加到 Claude Code、OpenAI CodeX、Cursor、VS Code、Cherry Studio 等客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 AI 提供影视播放地址搜索的 MCP 工具
- 支持小米电视及安装 TvBox 的安卓电视直接播放
- 内置默认 LunaTV/MoonTV 订阅源配置，可远程覆盖
- 提供 uvx、Docker、Home Assistant Add-on 三种安装方式

## 适用场景

- 在 Claude Code/Cursor 等客户端中让 AI 帮我找剧并投到电视播放
- 家庭多台电视（小米/安卓+TvBox）的追剧播放控制
- 对接自部署的 LunaTV/MoonTV 服务搜索影视

## 场景标签

 · 领域:影视/智能家居工具

## 证据(README 行号)

> L3: 一个用于追剧/追番的MCP服务器，为AI提供搜索影视播放地址的能力，并支持在小米电视上直接播放。
> L33: - 添加到 Claude Code, 执行命令:

## 星数曲线

```mermaid
xychart-beta
    title "aahl/mcp-vods 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f8032dec9ca8` · [字段定义](../../DATASET.md)*
