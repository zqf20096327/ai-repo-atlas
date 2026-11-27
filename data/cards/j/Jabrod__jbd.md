# Jabrod/jbd

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/Jabrod/jbd) · [官网](https://jabrod.com/jbd) · 组织维护

**带 AI Director 的 Windows 桌面视频编辑器**

面向 Windows 10/11 的桌面视频编辑器，提供多轨时间线（ripple/roll/slip/slide 修剪）、调色（曲线、色轮、示波器）、音频混音与响度表、字幕轨道及设备端语音转文字，导出支持至 4K。自 1.1 版起内置 AI Director：用户描述想要的剪辑后，它逐步在时间线上执行、生成视频与旁白，并在渲染帧上检查结果，所有修改可撤销。基于开源 Rust 编辑器 FilmCraft 构建，可从 Microsoft Store 或官网下载，另有 JBD Pro（按月 AI 额度）与 9876 端口的 agent 控制服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI Director 逐步执行剪辑规划，生成视频与旁白并自检渲染帧
- 设备端语音转文字与可编辑字幕轨道
- 提供 agent 控制服务器（端口 9876）与控制协议文档
- 多轨时间线、调色、混音与 4K 导出

## 适用场景

- 用自然语言描述让 AI 分步完成剪辑、配乐与字幕
- 多轨时间线剪辑、调色与音频混音
- 让 agent 通过控制协议操作编辑器

## 场景标签

`图像视频处理` `语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L17: JBD is a desktop video editor for Windows 10 and 11. It provides a multi-track timeline with
> L22: Since version 1.1, JBD includes the **AI Director**: describe the edit you want, and it plans the
> L23: edit, works step by step on your timeline, generates video and voiceover, and checks the result

## 星数曲线

```mermaid
xychart-beta
    title "Jabrod/jbd 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `850dfc820d81` · [字段定义](../../DATASET.md)*
