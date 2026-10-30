# buluoai6-eng/online-meeting-interview-assistant

⭐ 15 · JavaScript · MIT · 推送 2026-07-23 · [GitHub](https://github.com/buluoai6-eng/online-meeting-interview-assistant) · 个人维护 · 中文 README

**Windows 线上会议面试助手：本地语音识别加回答生成小窗**

基于 Electron 的 Windows 置顶辅助小窗，支持腾讯会议、Zoom、Teams、飞书、钉钉、Webex、Google Meet 的窗口路由及自定义窗口选择。双通道采集系统回环音频与麦克风，本机运行 FunASR Paraformer 流式字幕与 SenseVoice 最终转写，Silero VAD 做静音过滤；问题判断后由本地 Ollama/Qwen 或用户自填的 OpenAI 兼容 API 生成回答抓手。领域模块（内置金融与会计）可加载术语纠错与知识条目。仅支持 Windows，需 Node.js 20+，建议预留 18GB 磁盘与 NVIDIA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个主流会议平台快捷匹配与自定义窗口/屏幕路由
- FunASR 流式字幕 + SenseVoice 最终转写的双阶段本地识别
- 可切换领域模块：内置金融与会计模块含 19 组术语纠错、52 个误识别别名、14 个知识专题
- 默认本地模式只访问 127.0.0.1，原始音频不上传不写文件

## 适用场景

- 线上面试时实时获取对方问题的字幕与回答抓手
- 金融、会计、审计类面试中纠正领域术语误识别
- 在允许 AI 辅助的场合作为无障碍/笔记型辅助工具使用

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: 一个面向 Windows 主流视频会议平台的始终置顶线上面试辅助小窗。用户可以选择腾讯会议、Zoom、Microsoft Teams、飞书/Lark、钉钉、Webex、Google Meet，也可以手动选择任意窗口或屏幕。应用分别捕
> L77: - **本地模型（默认）**：使用本机 Ollama/Qwen，题目、知识和准备信息均不上传；

## 星数曲线

```mermaid
xychart-beta
    title "buluoai6-eng/online-meeting-interview-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dec341e4285d` · [字段定义](../../DATASET.md)*
