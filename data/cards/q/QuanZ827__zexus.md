# QuanZ827/zexus

⭐ 98 · C# · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/QuanZ827/zexus) · 个人维护

**Revit 进程内 AI agent：用自然语言驱动 C# 代码执行 BIM 操作**

作为 Revit 插件运行在 Revit 进程内的 AI agent：用户用自然语言描述需求，agent 生成 Revit API 的 C# 代码，经 Roslyn 运行时编译并作用于当前活动文档。写操作前 agent 须提交计划并获得用户确认（护栏机制）。支持 Anthropic/OpenAI/Google 三家 LLM，自带 API key 配置。以每用户 MSI 安装包分发，注册为 Revit Ribbon 标签页，支持 Revit 2022–2026（.NET Framework 4.8 + .NET 8）。作者为独立开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Roslyn 运行时编译 C#，无预定义工具目录，可触达任意 Revit API 表面
- 多 LLM 提供商（Anthropic/OpenAI/Google），自带 key 首次配置
- 写操作须提交计划并经用户确认的护栏机制
- 每用户 MSI 安装，支持 Revit 2022–2026

## 适用场景

- 用自然语言批量执行 Revit API 操作，无需编写脚本文件
- 对当前模型做只读检查或批量修改（修改前需确认）
- 替代逐任务编写固定工具的 BIM 自动化流程

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: **An in-process Revit AI agent that compiles and runs C# at runtime to drive any Revit API operation through natural
> L5: Zexus is a Revit add-in that runs entirely inside the Revit process. Describe what you want in plain English; the ag

## 星数曲线

```mermaid
xychart-beta
    title "QuanZ827/zexus 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 97 --> 102
    line [101, 98, 98]
```

2026-10-18 101 → 2026-10-24 98（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d9fd9346f28b` · [字段定义](../../DATASET.md)*
