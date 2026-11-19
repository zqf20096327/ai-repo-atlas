# naveed-gung/nova

⭐ 10 · TypeScript · 推送 2026-05-13 · [GitHub](https://github.com/naveed-gung/nova) · [官网](https://n0v0.netlify.app/) · 个人维护

**浏览器端多语言 AI 语音助手，支持语音/文字/唤醒词交互**

基于 React + TypeScript 的浏览器语音助手，通过 Google Gemini 2.0 Flash 生成回答。语音链路使用 Web Speech API 实现识别与合成，支持 "Hey Nova" 唤醒词、语音切换语言（英语/黎巴嫩阿拉伯语/法语），并配有 Three.js GLSL 3D 可视化。部署在 Netlify：API key 经服务端代理不进浏览器，内置每 IP 限流、SSE 流式输出与慢网络自动降级。安装需自行配置 Gemini API key，本地用 Vite 开发服务器运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web Speech API 语音识别与句队列 TTS，支持三语及语音切换语言
- SSE 流式输出，经 Netlify Edge/Serverless Functions 代理，API key 不暴露给客户端
- Three.js + 自定义 GLSL 着色器的 3D 状态可视化（WebGL 上下文恢复）
- 每 IP 限流、安全响应头、PWA 离线缓存

## 适用场景

- 在浏览器里用语音与 AI 对话，免手操作（唤醒词激活）
- 需要英/阿/法多语言语音助手界面
- 作为 Netlify 部署的带安全代理的语音助手参考实现

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L9: Nova is a production-grade, multilingual AI voice assistant that delivers natural conversation directly in the brows
> L15: - speech recognition **Speech Recognition** -- Browser-native speech-to-text via Web Speech API with interim result
> L128: |ai AI|Google Gemini 2.0 Flash (via Netlify Functions + Edge Functions)|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `540f740a6eb0` · [字段定义](../../DATASET.md)*
