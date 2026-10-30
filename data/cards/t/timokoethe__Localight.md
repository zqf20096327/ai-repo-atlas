# timokoethe/Localight

⭐ 18 · Swift · MIT · 推送 2026-10-19 · [GitHub](https://github.com/timokoethe/Localight) · [官网](https://itstimo.me/projects/localight) · 个人维护

**基于 Apple 设备端 Foundation Models 的 SwiftUI 聊天演示应用**

面向 iOS 26/27 的原生 SwiftUI 聊天应用示例，通过 SystemLanguageModel.default 接入 Apple 设备端基础模型，实现文本与（iOS 27）单图多模态对话、流式输出、可编辑模型指令、温度调节与逐条 token 统计；对话不持久化，模型就绪后可离线生成。维护者声明该应用为演示用途、非生产就绪，仓库无自动化测试目标。开发者需 Xcode 26/27 自行编译，且实际生成需 Apple Intelligence 资格设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 SystemLanguageModel 接入 Apple 设备端模型，支持流式输出与会话预热
- iOS 27 实现支持单图附件、上下文用量与逐条 token 统计
- 对话仅存内存、不持久化，模型就绪后离线生成
- iOS 26/27 双实现按 SDK 编译条件与运行时 #available 切换

## 适用场景

- 学习如何在 SwiftUI 应用中集成 Apple Foundation Models
- 在 Apple Intelligence 设备上体验设备端模型的离线对话
- 参考流式输出、错误映射与 token 上限（4,096/会话）的处理方式

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L10: **Localight** is a native SwiftUI chat app for iOS 26 and iOS 27, powered entirely by Apple’s on-device Foundation 
> L37: - 🧠 **On-device model**: Uses Apple’s local Foundation Models for text generation.
> L67: - For meaningful generation, an Apple Intelligence-eligible physical device with Apple Intelligence enabled, a supp

## 星数曲线

```mermaid
xychart-beta
    title "timokoethe/Localight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `532c78d59d4d` · [字段定义](../../DATASET.md)*
