# ionic-team/capacitor-local-llm

⭐ 25 · TypeScript · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/ionic-team/capacitor-local-llm) · 组织维护

**Capacitor 插件：在 iOS/Android 应用内运行端侧 LLM**

面向 Capacitor 混合应用开发者的原生插件：封装 iOS 的 Apple Intelligence（Foundation Models）与 Android 的 Gemini Nano（ML Kit），提供文本生成、图像生成（仅 iOS）、多轮会话、warmup 预热与可用性检测 API，全程无网络请求与 API key。限制较多：文本 LLM 需 iOS 26+ 且设备支持 Apple Intelligence，Android 需支持端侧 AI 的真机（如 Pixel 9+），Android 输出 token 上限 256，后台不可推理且受配额约束。项目自声明为实验性，不提供支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 封装 Apple Foundation Models（iOS）与 Gemini Nano（Android）
- 提供 prompt / generateImage / warmup / 会话管理与可用性监听 API
- 无网络请求、无 API key，数据不离开设备
- Android 侧支持按需 download() 模型并轮询可用状态

## 适用场景

- 在混合移动应用中内置离线 AI 对话或文本生成功能
- iOS 应用内集成设备端图像生成
- 为应用添加不依赖云端、不外发数据的 AI 能力

## 场景标签

`推理引擎` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L6: Run large language models entirely on-device using Apple Intelligence (Foundation Models) on iOS and Gemini Nano on 
> L13: npm install @capacitor/local-llm

## 星数曲线

```mermaid
xychart-beta
    title "ionic-team/capacitor-local-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c972d5c896fd` · [字段定义](../../DATASET.md)*
