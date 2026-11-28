# backmesh/openai-react-native

⭐ 46 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/backmesh/openai-react-native) · [官网](https://www.npmjs.com/package/openai-react-native) · 组织维护

**React Native 直连 OpenAI API 的客户端库**

一个 React Native 客户端库，使用 react-native-sse 与 Expo FileSystem 取代 polyfills，使移动应用可直接调用 OpenAI API，支持流式响应与文件上传，类型与 API 与 OpenAI Node SDK 保持一致。要求强制设置 baseURL，README 提醒不得在客户端暴露密钥，应通过后端代理转发调用。覆盖 Chat Completion、Models、Files、Moderations 与 Beta 的 Threads/Assistants；Images、Audio、Embeddings 尚未覆盖。MIT 许可，npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 react-native-sse 实现流式 chat.completions，提供 onData/onDone/onOpen/onError 回调
- 基于 Expo FileSystem 的文件上传，仅需提供文件路径
- 类型与 API 与 OpenAI Node SDK 尽可能一致
- 强制 baseURL 参数，引导经后端代理保障密钥安全

## 适用场景

- 在 React Native 应用中调用 OpenAI 聊天补全并流式展示
- 从移动端上传文件用于 fine-tune 等用途
- 为 React Native 应用接入内容审核（Moderations）接口

## 场景标签

 · 领域:移动开发/LLM 客户端库

## 证据(README 行号)

> L3: The goal of this library is to use React Native SSE and Expo FileSystem instead of polyfills to support calling the 
> L17: npm i openai-react-native
> L53: - [x] Chat Completion


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `71b10e278fe0` · [字段定义](../../DATASET.md)*
