# lobehub/lobe-tts

⭐ 809 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/lobehub/lobe-tts) · [官网](https://tts.lobehub.com) · 组织维护 · 中文 README

**给 Web/Node 开发者的 TTS/STT 语音库，服务端与浏览器通用**

TypeScript 库 @lobehub/tts，提供文本转语音与语音转文本能力，可在 Node.js/Bun 服务端生成音频文件，或在浏览器直接播放。统一 API 支持四种语音来源：Microsoft Edge、Microsoft Speech、OpenAI 与浏览器内置语音。附带 React 入口，提供 hooks 与带进度/暂停/下载的音频播放器组件，长文本可边生成边播放。仅发布 ESM 包，React 入口需 @lobehub/ui、react 19 等对等依赖；另发布面向编码 agent 的 skills.md 与 llms.txt 文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 接入 Microsoft Edge / Microsoft Speech / OpenAI / 浏览器内置语音四种来源
- React hooks 与音频播放器组件（进度/暂停/下载）
- 长文本边生成边播放
- @lobehub/tts/server 入口可从自有 API 路由代理 OpenAI 语音与转录

## 适用场景

- 在 React 应用中加朗读按钮和语音输入
- 在 Node.js/Bun 服务端批量生成音频文件
- 通过自有 API 路由代理 OpenAI 语音服务避免暴露 key

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L5: Text-to-speech and speech-to-text for server and browser, with React hooks and audio components.
> L33: - **Pick your voice provider** — Microsoft Edge, Microsoft Speech, OpenAI or the browser's built-in speech, behind 

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-tts 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-26"]
    y-axis "stars" 805 --> 810
    line [806, 807, 809, 809]
```

2026-10-18 806 → 2026-10-26 809（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0eb7b8f994ca` · [字段定义](../../DATASET.md)*
