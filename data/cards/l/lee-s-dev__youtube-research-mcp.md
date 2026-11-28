# lee-s-dev/youtube-research-mcp

⭐ 10 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/lee-s-dev/youtube-research-mcp) · [官网](https://pypi.org/project/youtube-research-mcp/) · 个人维护

**给 MCP 客户端提供 YouTube 字幕、评论与频道数据的 MCP 服务器**

一个遵循 Model Context Protocol 的服务器，向支持 MCP 的 AI 客户端提供 YouTube 数据工具：视频字幕获取、多视频并行采集、频道最新视频分析、关键词搜索、评论采集与配额查询。自身不调用 LLM，仅做数据收集，分析与总结由宿主 AI 完成；字幕与元数据经 yt-dlp 获取，无需 API key，搜索与评论需免费 YouTube Data API key。结果缓存至本地 SQLite 以减少重复配额消耗，字幕/评论附带 safety_notice 字段以防提示注入。

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

- 提供 get_transcript、analyze_videos、analyze_channel 等 8 个 MCP 工具
- 字幕与频道分析经 yt-dlp 无需 API key；搜索与评论需 YouTube Data API key
- SQLite 本地缓存（字幕 30 天/评论 6 小时/搜索 2 小时），README 声明不向外部服务器发送数据
- 字幕与评论含 safety_notice 字段防提示注入

## 适用场景

- 让 Claude Desktop/Cursor 等客户端直接总结 YouTube 视频要点
- 对比多个视频的论点与评论区反应
- 分析某频道近期视频的内容主题
- 检索某关键词视频并批量采集字幕做研究素材

## 场景标签

`网页抓取` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L15: MCP(Model Context Protocol)를 지원하는 AI 클라이언트라면 어디서든 사용할 수 있습니다.
> L164: - **LLM 호출 없음** — 데이터 수집만 담당합니다. 분석·요약·판단은 AI 어시스턴트가 합니다.
> L173: #### `get_transcript` — 영상 자막 가져오기

## 星数曲线

```mermaid
xychart-beta
    title "lee-s-dev/youtube-research-mcp 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `933bf4adcd98` · [字段定义](../../DATASET.md)*
