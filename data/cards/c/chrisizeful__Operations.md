# chrisizeful/Operations

⭐ 34 · C# · MIT · 推送 2026-07-13 · [GitHub](https://github.com/chrisizeful/Operations) · 个人维护

**Godot 引擎的动画与行为树编程库（C#/GDScript）**

面向 Godot 4 游戏开发者的动画与复杂行为树构建库：提供大量内置 operation，支持以代码组合（sequence 等）方式编写角色动画逻辑（如 2D 角色死亡动画），自定义 operation 易于编写。同时提供 C# 与 GDScript 两套 API，二者基本一致，主要差异为 GDScript 中不使用对象池。安装方式为复制 addons 目录到项目，C# 版可经 NuGet 获取；运行 demo 需 git clone 仓库。MIT 许可，部分对象池代码改自 libGDX（Apache 2.0）。README 未展示 AI 相关功能，主题标签中的 ai 缺乏正文支撑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置大量 operation，支持代码化组合动画与行为树
- 同时提供 C# 与 GDScript 两套基本一致的 API
- 支持自定义 operation 扩展
- C# 版以 NuGet 包分发，GDScript 版以 addon 形式安装

## 适用场景

- 用代码而非编辑器编排角色动画序列
- 在 Godot 4 项目中构建复杂行为树逻辑
- C# 或 GDScript 项目中复用同一套动画组合 API

## 场景标签

 · 领域:游戏开发/引擎扩展

## 证据(README 行号)

> L5: Operations provides a quick and efficient way to programmatically create animations and complex behavior trees in th

## 星数曲线

```mermaid
xychart-beta
    title "chrisizeful/Operations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `49a197cc84c2` · [字段定义](../../DATASET.md)*
