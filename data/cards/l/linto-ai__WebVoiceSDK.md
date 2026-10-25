# linto-ai/WebVoiceSDK

⭐ 37 · JavaScript · AGPL-3.0 · 推送 2026-02-05 · [GitHub](https://github.com/linto-ai/WebVoiceSDK) · 组织维护

**浏览器内全离线语音前端 JS 库：麦克风到唤醒词全链路**

JavaScript 库，为浏览器中的常听式语音应用提供建模块：麦克风采集、降采样、语音预加重、VAD（RNN+WebAssembly）、纯 JS MFCC 特征提取与唤醒词推理（基于 Tensorflow JS，WebAssembly 运行时）。节点式 API 串联成处理管线，全离线运行无服务端。面向开发语音应用的 Web 开发者，预置 LinTO/Snips/Firefox 唤醒词模型，支持自定义模型。提供 ES 模块、IIFE 与 CDN 引入方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 麦克风→VAD→降采样→特征提取→唤醒词推理的完整节点式管线
- RNN + WebAssembly 的语音活动检测（低信噪比下可用）
- Tensorflow JS 驱动的多唤醒词推理，模型可跨嵌入式/移动/桌面/网页使用
- 全离线浏览器内运行，无需服务端

## 适用场景

- 网页中实现离线唤醒词监听以触发任务
- 构建浏览器内的语音助手或语音控制前端
- 处理麦克风音频流：录制、降采样、特征提取

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: WebVoice SDK is a JavaScript library that provides lightweights and fairly well optimized buildings block for always
> L38: - The wake word Engine relies on Tensorflow JS and WebAssembly portable runtime to infers towards single or multipl

## 星数曲线

```mermaid
xychart-beta
    title "linto-ai/WebVoiceSDK 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `22545cd55680` · [字段定义](../../DATASET.md)*
