# Oal36ar/ytmaxxing

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Oal36ar/ytmaxxing) · 个人维护

**把 YouTube 长视频转成 AI agent 可用的技能与知识库的工具**

提供 MCP server、CLI 与 Claude Code 插件三种形态：给定 YouTube 链接（视频/播放列表/频道），抓取字幕并切分结构化转写稿，按 7 种模式（skill/knowledge/summary/learn/outcomes/check/max）生成带时间戳引用的 markdown 输出，存入本地 ~/ytmaxxing 库，技能可安装到 ~/.claude/skills。产品自身不做推理，把转写稿与写作指南交给用户已有的 AI（Claude、Cursor 等 MCP 客户端），因此无需 API key；无字幕视频可启用 faster-whisper 本地转录。需 Python 3.10+ 与 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种输出模式，从可安装的 SKILL.md 到带时间戳引用的知识笔记
- MCP server 提供 maxx/get_video/save_output/search_library/install_skill 等工具
- 无字幕视频可用 faster-whisper 本地转录（[whisper] extra）
- 输出为本地纯 markdown，可接入 Obsidian 或任意 agent

## 适用场景

- 把教程视频转成 agent 可加载的技能文件
- 为长访谈/播客生成可检索的带引用知识笔记
- 离线或无字幕环境下本地转录视频内容
- 针对自己的目标从视频中提取行动清单

## 场景标签

`知识库管理` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L20: **ytmaxxing** fixes both. Give it any YouTube link and your AI turns the video into things you keep: a **skill** yo
> L130: ytmaxxing does the parts a model is bad at: fetching captions reliably, splitting long videos into readable parts,
> L136: |`maxx`|Fetches the video and returns the guide for the chosen mode|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `3d74e82632e3` · [字段定义](../../DATASET.md)*
