# banghuazhao/swift-ai-agent-demo

⭐ 15 · Swift · MIT · 推送 2026-06-26 · [GitHub](https://github.com/banghuazhao/swift-ai-agent-demo) · [官网](https://www.linkedin.com/pulse/building-simple-ai-agent-my-journey-creating-react-ios-banghua-zhao-yivmc) · 个人维护

**iOS 原生 ReAct 模式 AI Agent 演示应用（SwiftUI）**

基于 SwiftUI 与 MVVM 的原生 iOS 应用，实现 ReAct（推理+行动）Agent 模式：用户输入任务后，应用调用 OpenAI GPT 模型进行思考-行动-观察循环，执行 read_file、write_to_file、get_current_time 等工具完成任务，界面实时展示推理过程。API 密钥需在源码中配置，推理在设备本地协调但依赖 OpenAI API，会话不持久化。项目定位为 AI Agent 与 iOS 开发的学习资源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 ReAct 思考-行动-观察循环与工具执行引擎
- 可扩展工具框架，内置文件读写与时间获取工具
- SwiftUI 实时可视化 Agent 推理过程
- 会话不持久化，数据不落盘

## 适用场景

- 学习 ReAct Agent 模式在 iOS 上的实现
- 作为 SwiftUI AI 应用开发的参考工程
- 演示多步推理任务（计算、文件操作、时间查询）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L27: This project implements the **ReAct (Reasoning + Acting)** pattern, where the AI agent:
> L36: - **🌐 ChatGPTService**: OpenAI API integration for intelligent responses

## 星数曲线

```mermaid
xychart-beta
    title "banghuazhao/swift-ai-agent-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `21410e7a575f` · [字段定义](../../DATASET.md)*
