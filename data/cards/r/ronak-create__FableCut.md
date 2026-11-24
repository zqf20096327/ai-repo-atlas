# ronak-create/FableCut

⭐ 812 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ronak-create/FableCut) · [官网](fablecut.space) · 个人维护

**浏览器端非线性视频编辑器，可由 AI agent 通过 JSON/MCP 驱动**

一个完全在浏览器中运行的 Premiere 风格非线性视频编辑器，整个时间线以单个 JSON 文档（project.json）暴露：媒体、剪辑、轨道、效果、关键帧与转场均可通过手写 JSON、UI 操作或 MCP/REST 的 AI agent 编辑，浏览器 UI 通过 server-sent events 约 150ms 内热重载。零 npm 依赖，`node server.js` 即可启动；agent 的每次修改作为独立撤销步骤，并支持 Versions 版本回滚。语音转写（Whisper）在浏览器本地运行，音频不出本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 时间线整体暴露为 JSON 文档，任何能写 JSON 的进程都能剪辑视频
- MCP + REST 双通道供 AI agent 驱动编辑，UI 实时热重载
- agent 修改独立撤销与 Versions 版本快照机制
- 本地 Whisper 转写、字幕生成、静音切除、节拍对齐、降噪等内置功能

## 适用场景

- 让 Claude 等 agent 帮我剪出一条 reel，同时在 UI 里实时查看
- 人工与 AI agent 同时编辑同一条时间线协作剪辑
- 长素材自动挑精彩片段、切静音、按节拍对齐快速成片

## 场景标签

`语音识别` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: **A browser video editor that AI agents can drive.**
> L20: FableCut is a Premiere-style non-linear video editor that runs entirely in your
> L22: from the UI, or let an AI agent (Claude Code, Claude Desktop, or anything that

## 星数曲线

```mermaid
xychart-beta
    title "ronak-create/FableCut 星数(近 27 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 732 --> 813
    line [738, 740, 744, 746, 748, 763, 767, 770, 771, 772, 774, 746, 786, 789, 790, 791, 793, 795, 797, 799, 800, 803, 804, 805, 804, 807, 807]
```

2026-10-22 738 → 2026-11-24 807（+69）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `71b37754c45a` · [字段定义](../../DATASET.md)*
