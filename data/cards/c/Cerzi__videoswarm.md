# Cerzi/videoswarm

⭐ 106 · JavaScript · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/Cerzi/videoswarm) · [官网](https://github.com/Cerzi/videoswarm/releases) · 个人维护

**大规模视频集批量播放与审阅的桌面浏览器**

基于 Electron + React 的桌面应用，用于浏览含成百上千视频的目录：以虚拟化瀑布流网格同时播放多个视频，支持递归目录树导航、Accept/Reject/评分/标签式审阅流程、批量移动/复制/删除、SQLite 索引与实时文件监控，并可读取 ComfyUI/VHS 嵌入的生成元数据。面向 AI 视频生成（如 ComfyUI）输出的筛选与大规模视频数据集审阅场景。限制：桌面端专用，主要面向短视频集合，Windows x64 与 Debian/Ubuntu x64 发行，Pre-1.0 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 虚拟化瀑布流网格同时播放数千短视频，多档播放模式
- A/S/D/F 审阅快捷键、五星评分、自定义标签与持久化审阅进度
- SQLite 索引的增量递归扫描与 Chokidar 实时监控
- 读取 ComfyUI/VHS 嵌入生成元数据（prompt/seed/model/LoRA 等）

## 适用场景

- 快速浏览和对比 ComfyUI 批量生成的视频输出
- 对 AI 视频训练数据集做_accept/reject 筛选与评分
- 在大量 B-roll 或档案视频中按目录查找所需片段

## 场景标签

 · 领域:视频浏览/数据集审阅工具

## 证据(README 行号)

> L6: I got tired of manually opening tens or hundreds of ComfyUI video outputs to try and find an old workflow or get a q
> L35: - Reviewing outputs from AI video generation workflows (e.g. ComfyUI)
> L36: - Seeing a clear overview of video training datasets for AI training

## 星数曲线

```mermaid
xychart-beta
    title "Cerzi/videoswarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-23 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4b87816750d0` · [字段定义](../../DATASET.md)*
