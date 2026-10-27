# sambuild04/screen-voice-agent

⭐ 40 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/sambuild04/screen-voice-agent) · 个人维护

**macOS 语音优先 AI 桌面助手：看屏幕听音频并实时对话操控**

面向 macOS 用户的 Electron 桌面 AI 助手：唤醒词语音交互（基于 OpenAI Realtime API），经授权后读取屏幕画面与系统音频，通过 macOS Accessibility 树操控应用，经 Playwright 打开可见浏览器执行网页操作；可在运行时用 GPT-5.5 生成插件、用 GPT-4o-mini 审查并自动修复，保存 3 步以上工具链为可复用技能；支持语音注册的环境触发器与本地滚动音频缓冲按需转录。桌面应用提供 Apple Silicon 的 dmg 安装包，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唤醒词语音进出，亚 500ms 语音回环（OpenAI Realtime API）
- 屏幕+系统音频环境感知与实时问答（含本地音频缓冲按需转录）
- 经 Accessibility 树驱动应用，Playwright 可见浏览器自动化
- 运行时自生成工具并自动修复（GPT-5.5 + GPT-4o-mini 审查）

## 适用场景

- 会议/播客/课程中直接语音追问刚才说了什么
- 看动漫、韩剧时做沉浸式语言学习与实时讲解
- RSI 或免手操作用户用语音控制 Mac 与浏览网页
- 语音让 AI 现场为自己写小工具并复用为技能

## 场景标签

`语音 Agent` `AI 助手` `浏览器自动化` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: A **voice-first AI companion for macOS**. Wake-word activated, speaks back in under 500 ms, sees your screen and he
> L64: 1. **Wake-word voice in / voice out, sub-500 ms.** Not push-to-talk. Not type-and-read. You talk, Samuel talks back
> L66: 3. **Real computer use.** Clicks, types, drives apps via the macOS Accessibility tree with a GPT-5.5 visual fallbac

## 星数曲线

```mermaid
xychart-beta
    title "sambuild04/screen-voice-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-27"]
    y-axis "stars" 37 --> 41
    line [38, 39, 40, 40]
```

2026-10-18 38 → 2026-10-27 40（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ad78f729fe2c` · [字段定义](../../DATASET.md)*
