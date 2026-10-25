# deveix/react-native-apple-llm

⭐ 346 · Swift · MIT · 推送 2026-01-17 · [GitHub](https://github.com/deveix/react-native-apple-llm) · 个人维护

**React Native 插件：调用 Apple 端侧 Foundation Models**

面向 React Native/iOS 开发者的原生模块，封装 Apple Intelligence Foundation Models 框架的端侧 LLM API：检查模型可用性、创建会话、生成文本、按 JSON schema 生成结构化输出、支持工具调用与两种流式生成方式，处理全部在设备本地完成。要求 iOS 26.0、Xcode 26 及支持 Apple Intelligence 的设备（iPhone 15 Pro 及以上、M1+ iPad/Mac）。自述为 beta 功能，旧的全局函数已弃用，推荐使用 AppleLLMSession 类。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 封装 Apple Foundation Models 的文本生成与 JSON schema 结构化输出
- 工具调用（function calling）与流式生成（async 迭代/EventEmitter 两种方式）
- isFoundationModelsEnabled 返回四种设备可用性状态
- 全部处理在设备本地，不向服务器发送数据

## 适用场景

- 在 React Native 应用中离线运行 LLM 文本生成
- 从用户输入提取结构化 JSON 数据或自动填写表单
- 构建工具调用型 AI 助手且数据不出设备

## 场景标签

 · 领域:移动端 AI 开发库

## 证据(README 行号)

> L3: A React Native plugin to access Apple Intelligence Foundation Model framework using native on-device LLM APIs. This 
> L7: - **On-device Apple Intelligence** - Access Apple's Foundation Models locally

## 星数曲线

```mermaid
xychart-beta
    title "deveix/react-native-apple-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 345 --> 347
    line [346, 346]
```

2026-10-18 346 → 2026-10-25 346（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7d5f29858b94` · [字段定义](../../DATASET.md)*
