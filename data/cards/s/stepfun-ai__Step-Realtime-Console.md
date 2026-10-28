# stepfun-ai/Step-Realtime-Console

⭐ 84 · JavaScript · Apache-2.0 · 推送 2026-06-09 · [GitHub](https://github.com/stepfun-ai/Step-Realtime-Console) · 组织维护 · 中文 README

**阶跃星辰实时语音 API 的前端演示控制台**

基于 SvelteKit 与 Bun 构建的 Web 演示项目，用于展示和测试阶跃星辰实时语音对话 API：支持实时语音输入输出、音频波形可视化（WaveSurfer.js）、自定义 AI 人设与指令、API 调用调试日志。通过服务端 WebSocket 中转携带 API Key 与 API 通信，支持 step-audio-2 系列四个模型，需配置阶跃星辰开放平台的 API Key 与音色。运行时必须使用 Bun（1.2 以上），不兼容 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时语音交互与自动语音转文本
- WaveSurfer.js 音频波形可视化与调试日志
- 服务端 WebSocket 中转避免前端暴露 API Key
- 兼容 OpenAI 实时语音 SDK 修改版，支持 step-audio-2 系列四模型

## 适用场景

- 开发者调试和体验阶跃星辰实时语音 API
- 测试不同模型、音色与 System Prompt 的对话效果
- 参考 WebSocket 中转实现接入实时语音 API

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: 这是一个基于阶跃星辰实时语音 API 的前端演示项目，用于展示和测试阶跃星辰的实时语音对话功能。通过该项目，用户可以体验实时语音交互以及相关功能的调试与测试。项目提供了友好的用户界面，方便开发者和测试人员快速上手并了解阶跃星辰实时 
> L130: 本项目使用阶跃星辰实时语音 API，主要功能包括：

## 星数曲线

```mermaid
xychart-beta
    title "stepfun-ai/Step-Realtime-Console 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-28 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `770bdb2c1fea` · [字段定义](../../DATASET.md)*
