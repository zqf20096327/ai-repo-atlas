# elias-soykat/interview-copilot

⭐ 29 · TypeScript · 推送 2026-09-12 · [GitHub](https://github.com/elias-soykat/interview-copilot) · [官网](https://interview-copilot.app) · 个人维护

**面试实时助手桌面应用：听题、转写并生成答案**

基于 Electron + React 19 的跨平台（Windows/macOS/Linux）桌面应用：实时采集麦克风或系统音频，经 OpenAI Whisper 转写，用语言学启发式检测提问（可配置停顿阈值），调用 GPT-4o 生成口语化回答；支持截图分析 LeetCode/系统设计题并给出分步解答（Vision API）。窗口可通过 setContentProtection 对 Zoom/Teams 等屏幕共享隐藏，支持置顶与透明度调节。需用户自备 OpenAI API Key，从源码克隆后用 npm 安装并构建各平台安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时音频转写（Whisper）与基于停顿阈值的提问检测
- GPT-4o 生成口语化回答，可附简历上下文个性化
- 截图分析 LeetCode/系统设计题（GPT-4o Vision）
- setContentProtection 使窗口对 Zoom/Teams/Discord 屏幕共享隐藏

## 适用场景

- 远程面试中实时获取口头回答建议
- 截图编程题获取分步解答
- 面试准备练习时获取参考答案

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: An AI-powered cross-platform desktop application (Windows, macOS, Linux) that acts as a real-time interview assistan
> L9: - 🤖 **AI-Powered Answer Generation** — Generates concise, natural, human-like answers tailored for verbal responses.

## 星数曲线

```mermaid
xychart-beta
    title "elias-soykat/interview-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b429f3972a4c` · [字段定义](../../DATASET.md)*
