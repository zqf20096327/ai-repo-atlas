# Techopolis/AFM-Studio

⭐ 18 · Swift · 推送 2026-06-14 · [GitHub](https://github.com/Techopolis/AFM-Studio) · 个人维护

**iOS/macOS 应用：试用、对比与基准测试 Apple Foundation Models 框架下的语言模型**

SwiftUI 编写的 Mac 与 iOS 双端应用，通过 Apple Foundation Models 框架的 LanguageModelSession 与模型对话。支持三类模型来源：Apple 系统模型、Private Cloud Compute（需向 Apple 申请 entitlement）、以及从磁盘加载的 Core AI 模型包（内置 Gemma 3/4 与 GPT-OSS 20B 预设，可用脚本导出安装）。可跨多模型对比同一 prompt、运行本地基准测试并用 SwiftData 保存结果、解析思考/推理轨迹。基于 OS 27 / Xcode 27 beta 构建，需 Apple Developer 团队；MLX 支持当前未接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 LanguageModelSession 聊天，支持系统模型、Private Cloud Compute 与 Core AI 模型包三类来源
- 同一 prompt 跨多模型对比
- 本地基准测试套件，SwiftData 保存结果
- 脚本导出并安装 Apple coreai-models 预设（gemma3-4b/12b、gpt-oss-20b）

## 适用场景

- 在 Mac/iPhone 上试用并对比多个 Apple 端侧与云端语言模型
- 运行本地基准测试评估模型表现
- 查看 Private Cloud Compute 可用性与配额状态

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: AFM Studio is an open-source Mac and iOS app for trying, comparing, and benchmarking language models through Apple'
> L17: - Chat with models through `LanguageModelSession`.

## 星数曲线

```mermaid
xychart-beta
    title "Techopolis/AFM-Studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a6101d357188` · [字段定义](../../DATASET.md)*
