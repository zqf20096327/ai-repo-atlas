# modal-labs/quillman

⭐ 1,211 · Python · MIT · 推送 2026-05-28 · [GitHub](https://github.com/modal-labs/quillman) · [官网](https://modal.com/docs/examples/llm-voice-chat) · 组织维护

**基于 Moshi 语音大模型的全双工语音聊天应用**

Modal Labs 提供的语音对话示例应用：后端运行 Kyutai Labs 的 Moshi 语音-语音语言模型，通过 Mimi 流式编解码器维持连续音频流，用基础模型决定应答时机；前端 React 应用经 FastAPI 提供，采用双向 WebSocket 流与 Opus 音频编解码降低网络延迟。定位为开发者构建语言模型应用的起点与实验场，需 Modal 账号与 token，通过 modal serve 本地开发、modal deploy 部署到 serverless 平台，闲置时缩容到 0 不产生费用。README 声明代码仅供演示，商用前需检查模型许可。

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

- Moshi 语音-语音模型持续倾听、规划并回应用户
- Mimi 流式编解码器维持不间断的双向音频流
- 双向 WebSocket 流 + Opus 编解码压缩网络音频
- 部署于 Modal serverless，闲置缩容到 0

## 适用场景

- 直接体验 Moshi 语音对话的在线 demo
- 以此为起点开发自己的语音模型应用
- 学习流式语音推理与服务端部署结构

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: A complete voice chat app powered by a speech-to-speech language model and bidirectional streaming.
> L5: On the backend is Kyutai Lab's Moshi model, which will continuously listen, plan, and respond to the user. It uses t

## 星数曲线

```mermaid
xychart-beta
    title "modal-labs/quillman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 1210 --> 1212
    line [1211, 1211]
```

2026-10-18 1,211 → 2026-10-29 1,211（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `56211320c090` · [字段定义](../../DATASET.md)*
