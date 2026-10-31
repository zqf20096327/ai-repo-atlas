# fortana-co/youtube-music-dl

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/fortana-co/youtube-music-dl) · 组织维护

**面向 AI agent 的 YouTube 音乐下载与打标 CLI 工具**

基于 yt-dlp 封装的命令行工具，供人类、脚本或 AI agent 调用：下载单曲、播放列表和整专视频（按章节切分），写入标题/艺术家/专辑/音轨号标签，清理歌名与文件名，默认输出 Opus（m4a/mp3 可选，opus/m4a 尽量不重编码）。agent 友好设计：stdout 输出单一 JSON、稳定错误/退出码约定、幂等重跑、--print-skill/--print-schema/--probe 自描述机制，并附带 agent 技能。需系统安装 ffmpeg 与 JS 运行时（Deno/Node），不固定 yt-dlp 版本以便随 YouTube 变化及时升级。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单曲/播放列表/整专视频自动模式检测与章节切分
- stdout 单 JSON、稳定退出码、幂等重跑的 agent 友好契约
- --print-skill/--print-schema/--probe 自描述，无需额外文档
- 自定义时间戳切分（--chapters-file）与单歌列表组专辑

## 适用场景

- 按艺术家/专辑结构下载并整理 YouTube 音乐
- 让 AI agent 依据技能与 JSON 输出自动完成专辑下载
- 无章节的整专视频按描述中的曲目时间手动切分

## 场景标签

 · 领域:多媒体工具/agent 工具

## 证据(README 行号)

> L3: **youtube-music-dl** is an agent-friendly CLI tool that makes it super easy to download and label music from YouTube
> L48: - **Agent-friendly output**: one JSON object on stdout, a stable error/exit-code contract, idempotent re-runs, and 
> L116: Because the CLI is non-interactive and emits stable JSON, an agent can drive it easily. E.g. "download this album 

## 星数曲线

```mermaid
xychart-beta
    title "fortana-co/youtube-music-dl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2083e3856612` · [字段定义](../../DATASET.md)*
