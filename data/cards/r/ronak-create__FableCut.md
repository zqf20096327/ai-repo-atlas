# ronak-create/FableCut

⭐ 821 · JavaScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ronak-create/FableCut) · [官网](fablecut.space) · 个人维护

**浏览器内视频编辑器，AI agent 可经 JSON/MCP 驱动剪辑**

Premiere 风格的非线性视频编辑器，完全在浏览器中运行；整个时间线暴露为一份 project.json，任何能写 JSON 的进程都可编辑视频，浏览器 UI 通过 server-sent events 约 150ms 内热更新，人与 agent 可同时操作同一条时间线。提供 MCP 与 REST 接口及 fablecut_* 工具（转写、剪辑、降噪、字幕等）。每次 agent 编辑是独立撤销步骤并自动存版本。零 npm 依赖，node server.js 启动；降噪、代理、转写（本地 Whisper）依赖 ffmpeg/ffprobe。

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

- 时间线即 JSON 项目文件，MCP + REST 供 agent 驱动
- agent 编辑独立成撤销步骤，自动版本快照可回滚对比
- 浏览器本地 Whisper 转写与文字化剪辑，音频不出本机
- 零 npm 依赖，一条 node server.js 启动

## 适用场景

- 让 Claude 等 agent 自动剪出 reel 短视频
- 用文字稿选词删除来剪辑访谈内容
- 人机同时编辑同一条时间线
- 去静音、对节拍切点、自动生成字幕

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **A browser video editor that AI agents can drive.**
> L20: FableCut is a Premiere-style non-linear video editor that runs entirely in your
> L22: from the UI, or let an AI agent (Claude Code, Claude Desktop, or anything that
> L26: Zero npm dependencies. One `node server.js`. That's it.

## 星数曲线

```mermaid
xychart-beta
    title "ronak-create/FableCut 星数(近 26 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 737 --> 828
    line [744, 746, 748, 763, 767, 770, 771, 772, 774, 746, 786, 789, 790, 791, 793, 795, 797, 799, 800, 803, 804, 805, 804, 807, 812, 821]
```

2026-10-24 744 → 2026-11-26 821（+77）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `fccdd9d8afef` · [字段定义](../../DATASET.md)*
