# zihanyang-dev/onmark

⭐ 126 · Rust · MIT · 推送 2026-08-01 · [GitHub](https://github.com/zihanyang-dev/onmark) · 个人维护 · 中文 README

**面向人与 agent 的剧本优先 HTML 视频编译 CLI**

以单个 HTML 文档（自定义语义元素 + CSS）作为剧本，编译为时间线 IR 与经验证的 Render Units，经 Chromium 渲染帧、FFmpeg 混流，输出可交付视频（H.264/AAC MP4 或 ProRes 4444 MOV）。提供渲染、校验、单帧快照、review 检查点、批量化变体、字幕烧录等子命令，支持 macOS arm64/Linux x64/Windows x64，通过 npm 全局安装。架构上 Rust 负责编译/渲染/编码，TypeScript 负责浏览器呈现层；另提供可选的 agent skill 供创建-检查-渲染循环使用。

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

- 剧本优先：单个 HTML 文档编译为时间线 IR 与经验证的 Render Units
- Chromium 渲染 + FFmpeg 混流，输出 H.264/MP4 或 ProRes 4444/MOV
- typed 演示字段与批量变体渲染，未变更区域跨批次复用
- check/inspect/snapshot/review/benchmark 等确定性子命令

## 适用场景

- 用一份 HTML 剧本批量生成多语言/多数据变体的宣传视频
- 在 CI 中校验与快照视频帧，对比编辑前后的渲染区域
- agent 通过技能包执行创建-检查-渲染的视频生成循环

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L13: Onmark is a screenplay-first video compiler for people and agents. Write one
> L148: Install the optional agent skill for a product-owned create/check/inspect/render
> L152: npx skills add varo-yang/onmark --skill onmark-video

## 星数曲线

```mermaid
xychart-beta
    title "zihanyang-dev/onmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-28 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5dff092f157c` · [字段定义](../../DATASET.md)*
