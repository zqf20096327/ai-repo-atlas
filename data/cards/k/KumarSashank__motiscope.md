# KumarSashank/motiscope

⭐ 125 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/KumarSashank/motiscope) · [官网](https://kumarsashank.github.io/motiscope/) · 个人维护

**给编码代理用的动效复刻工具：从录屏测量并重建动画代码**

面向 Claude Code、Codex、Cursor 等编码代理的运动设计插件：读取本地视频文件，用 Python 标准库与 ffmpeg 逐帧计算运动能量曲线与信号分析，测出时长、缓动曲线、分段边界、stagger 与循环周期，再精选关键帧交给模型识别元素与动画类型，最终生成 GSAP / CSS / Framer Motion / Lottie 代码。纯本地运行，无云端与账号；依赖 ffmpeg/ffprobe 与 python3。无法从帧恢复的内容（精确贝塞尔控制点、亚像素运动、真实 3D）在文档中列出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐帧运动能量曲线 + ffmpeg 信号分析测出时长/缓动/stagger/循环周期
- 生成 GSAP / CSS / Framer Motion / Lottie 四种目标代码
- 帧数按运动复杂度封顶（10s 片段约 10 帧），不随视频长度增长
- 以 Claude Code 插件与可移植 agent skills（AGENTS.md）两种形式分发

## 适用场景

- 把网站上看到的动画录屏后复刻成本项目代码
- 从落地页走屏录屏重建整个页面的滚动动画
- 测量参考动画的精确时序与缓动供设计参考

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L20: A motion-design tool for coding agents. Pure Python (standard library) + `ffmpeg`.
> L21: No cloud, no npm, no accounts required. Ships as a **Claude Code plugin**, and as
> L79: So: **measured timing + curated frames → the model recreates it.** motiscope is a

## 星数曲线

```mermaid
xychart-beta
    title "KumarSashank/motiscope 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 123 --> 126
    line [124, 125, 125]
```

2026-10-18 124 → 2026-10-27 125（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e3ff444b1bf8` · [字段定义](../../DATASET.md)*
