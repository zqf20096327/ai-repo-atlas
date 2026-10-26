# Maclean-D/three-assistant-glass

⭐ 33 · JavaScript · AGPL-3.0 · 推送 2026-09-26 · [GitHub](https://github.com/Maclean-D/three-assistant-glass) · 个人维护

**可定制的 3D 对话 AI 角色，支持 Looking Glass 全息显示**

基于 three-vrm 的 3D 虚拟角色语音助手：通过 Vapi 平台接入可配置的 LLM（OpenAI/Anthropic/Groq 等）、语音（Cartesia/11labs 等）、知识库、实时转录、情绪检测与函数调用；角色模型用 vrm 文件、动画用 fbx，角色随语音助手的语音做口型/动作动画，可在 Looking Glass 全息显示器上以 3D 呈现。运行需桌面系统与 Node.js，git clone 后 npm install 并启动 node server.mjs，在设置中保存 Vapi 密钥即可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Vapi 接入自定义 LLM、语音、知识库与实时转录
- vrm 角色模型与 fbx 动画，随语音动画化
- 支持在 Looking Glass 全息显示器上以 3D 显示
- 支持情绪检测、打断、函数调用与录音

## 适用场景

- 在桌面浏览器中运行一个 3D 虚拟角色语音助手
- 在 Looking Glass 全息屏上展示 3D AI 角色
- 自定义 vrm 角色模型、卡片与 fbx 动画

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: Customizable 3D conversational AI character
> L9: ### Voice Assistant - Vapi
> L11: - Custom LLM (OpenAI, Anthropic, Groq, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "Maclean-D/three-assistant-glass 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8232ef6390eb` · [字段定义](../../DATASET.md)*
