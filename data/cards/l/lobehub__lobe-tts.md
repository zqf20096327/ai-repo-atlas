# lobehub/lobe-tts

⭐ 810 · TypeScript · MIT · 推送 2026-11-12 · [GitHub](https://github.com/lobehub/lobe-tts) · [官网](https://tts.lobehub.com) · 组织维护

**给应用加语音的 TTS/STT 库：服务端与浏览器均可运行**

@lobehub/tts 是一个 TypeScript 语音库，用统一 API 接入 Microsoft Edge、Microsoft Speech、OpenAI 与浏览器内置语音，实现文本转语音与语音转文本；提供 React hooks 与带进度、暂停、下载的音频播放组件，长文本可边生成边播放。仅支持 ESM，通过 pnpm 安装；React 入口需 @lobehub/ui 与 React 19 等对等依赖。另发布 skills.md 与 llms.txt 供编码 agent 读取真实 API 文档。维护方 LobeHub，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 API 接入 Microsoft Edge、Microsoft Speech、OpenAI 与浏览器内置语音
- Node.js / Bun 服务端生成音频，浏览器端直接播放
- React hooks 与音频播放组件（进度/暂停/下载）
- 提供 skills.md 与 llms.txt 供 AI 编码工具读取

## 适用场景

- 给 React 应用加朗读按钮与语音输入
- 在自己的 API 路由代理 OpenAI 语音与转写请求
- 长文本语音播报场景中快速起播

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L5: Text-to-speech and speech-to-text for server and browser, with React hooks and audio components.
> L32: - **Speak and listen** — turn text into speech and speech into text with one library
> L33: - **Pick your voice provider** — Microsoft Edge, Microsoft Speech, OpenAI or the browser's built-in speech, behind 

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-tts 星数(近 8 点)"
    x-axis ["2026-10-23", "2026-10-28", "2026-10-31", "2026-11-08", "2026-11-16", "2026-11-20", "2026-11-21", "2026-11-25"]
    y-axis "stars" 808 --> 813
    line [809, 810, 809, 810, 812, 811, 810, 810]
```

2026-10-23 809 → 2026-11-25 810（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `df4ca723fb54` · [字段定义](../../DATASET.md)*
