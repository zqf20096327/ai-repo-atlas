# zas/mcp-musicbrainz

⭐ 13 · Python · GPL-3.0 · 推送 2026-04-05 · [GitHub](https://github.com/zas/mcp-musicbrainz) · 个人维护

**为 AI 助手提供 MusicBrainz 音乐数据库查询工具的 MCP 服务器**

一个 MCP (Model Context Protocol) 服务器，向 AI 助手暴露查询 MusicBrainz 音乐数据库的工具：覆盖艺术家、专辑、录音、厂牌、作品、地点、乐器、事件等十余类实体的搜索与详情获取，支持模糊搜索、实体关系浏览、ISRC/ISWC 编码转换及封面艺术 URL 获取。通过 uv 从源码运行，可接入 Claude Desktop、Cursor、Windsurf 等客户端；响应使用 diskcache 本地缓存 24 小时以遵守 MusicBrainz 速率限制。面向需要音乐元数据查询能力的 AI 助手用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 个工具覆盖 12+ 类音乐实体的搜索与详情查询
- ISRC/ISWC 编码转换到 MusicBrainz 实体
- 本地 diskcache 缓存 24 小时以遵守 MusicBrainz 速率限制
- 支持 Claude Desktop、Cursor、Windsurf、Kiro CLI 等 MCP 客户端接入

## 适用场景

- 让 AI 助手查询艺术家专辑、曲目、厂牌等音乐元数据
- 通过 ISRC 码定位 Spotify/Apple 曲目对应的 MusicBrainz 录音
- 查询专辑制作信息（录音室、工程师、制作人）与封面图

## 场景标签

 · 领域:AI 工具接入/音乐元数据

## 证据(README 行号)

> L3: An MCP (Model Context Protocol) server that provides tools for querying the MusicBrainz music database. Search for a
> L59: ### Claude Desktop

## 星数曲线

```mermaid
xychart-beta
    title "zas/mcp-musicbrainz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c5639a7fd347` · [字段定义](../../DATASET.md)*
