# Overusedhydra/reels-vault

⭐ 18 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/Overusedhydra/reels-vault) · 个人维护

**把 Instagram Reels 转成可检索的本地内容研究库**

本地优先的流水线工具：粘贴 Reel 链接后自动下载视频、用 Whisper 转录、Shazam 接口识别音乐、抽取关键帧与元数据，并按创作者和主题归档到 Obsidian、Notion 或两者。提供 MCP 服务器与 Claude 技能包，使 Claude/Cursor 等 AI 客户端可代为保存、分类、检索 Reel；分类标签由调用工具的 AI agent 填写。无云端转录，首次完整安装约需 1.7 GB 磁盘；Instagram 下载可能需要浏览器 cookies。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 下载→转录→音乐识别→按主题归档的本地流水线，无需云端转录或付费 AI API
- 支持 Obsidian、Notion 或双存储，笔记含 YAML frontmatter 与关键帧
- 通过 MCP 与 Claude 技能包接入 Claude Desktop、Claude Code、Cursor 等 AI 客户端
- 提供 5 档 Whisper 模型选择与 vault 修复工具

## 适用场景

- 收藏大量 Reels 并按创作者/主题检索，做内容选题研究
- 让 Claude 保存并自动分类 Reel，之后用自然语言查询库里关于 hooks、CTA 的说法
- 把 Reel 转录、音乐与画面整理进 Obsidian 笔记库做研究素材管理

## 场景标签

`知识库管理` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L11: A local-first pipeline that extracts transcripts, music, frames, and metadata
> L22: - **Extract** video, transcript, metadata, and music from any public reel
> L25: - **Connect** to Claude/Cursor via MCP so your AI can search your reels

## 星数曲线

```mermaid
xychart-beta
    title "Overusedhydra/reels-vault 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7cb44a2a3370` · [字段定义](../../DATASET.md)*
