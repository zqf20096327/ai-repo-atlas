# openai/realtime-voice-component

⭐ 886 · TypeScript · Apache-2.0 · 推送 2026-04-27 · [GitHub](https://github.com/openai/realtime-voice-component) · 组织维护

**基于 OpenAI Realtime 的 React 语音控制 UI 组件，给浏览器应用加语音操作**

OpenAI 维护的 React/浏览器层组件，用于在应用中嵌入基于 Realtime API 的语音助手 UI：应用定义窄化的工具，组件提供会话/传输/工具执行控制器（createVoiceControlController）、React 绑定（useVoiceControl）、启动器挂件（VoiceControlWidget）与可选的可视化确认（ghost cursor）。需自建 /session 端点代理 SDP 到 Realtime API，默认 server_vad 轮次检测。未发布到 npm，仅支持从本地 checkout 安装，README 明确声明为参考实现、非生产就绪 UI 套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- defineVoiceTool 将 Zod 定义的应用动作转为 Realtime 函数工具
- 控制器管理会话、传输、工具执行、转写与连接生命周期
- 可选 ghost cursor 可视化确认与启动器挂件
- 附 demo 应用：主题切换、多步表单、共享状态棋局三种流程

## 适用场景

- 为 React 应用添加语音驱动的工具调用 UI
- 在浏览器中实现应用自有动作的语音助手交互
- 参考 Realtime 会话代理与控制器生命周期的集成模式

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: React/browser voice controls for tool-constrained UIs built on OpenAI Realtime.
> L45: Use `openai-agents-js` when you
> L142:  your server forward that request to `POST https://api.openai.com/v1/realtime/calls`.

## 星数曲线

```mermaid
xychart-beta
    title "openai/realtime-voice-component 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 885 --> 887
    line [886, 886]
```

2026-10-18 886 → 2026-10-27 886（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `34ad378920fd` · [字段定义](../../DATASET.md)*
