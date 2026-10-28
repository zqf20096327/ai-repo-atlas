# rudrankriyam/Core-AI-Framework-Lab

⭐ 66 · Swift · MIT · 推送 2026-07-03 · [GitHub](https://github.com/rudrankriyam/Core-AI-Framework-Lab) · [官网](https://developer.apple.com/core-ai/) · 个人维护

**探索 Apple Core AI 框架的原生模型工作台应用**

SwiftUI 编写的 macOS/iOS 应用，围绕 Apple 的 CoreAI.framework 提供模型发现、转换、检查、运行、基准测试与打包功能：收录 33 个固定的 Apple 模型配方（语言/视觉/音频/扩散），支持导入 .aimodel 资产、选择 CPU/GPU/神经网络引擎特化配置运行无状态函数、导出证据 JSON 与无依赖 Swift 集成包。配方是转换指令，不附带模型权重；需 Xcode 27 beta、Swift 6.4，自行从源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 33 个固定 Apple 模型配方，覆盖语言/视觉/音频/扩散四类
- Asset Inspector 检查 .aimodel 元数据，Runtime Studio 运行与计时
- 基准测试证据 JSON 导出与无依赖 Swift 集成包导出
- 内容寻址的项目存储：导入文件经哈希与符号链接检查后原子晋升

## 适用场景

- 在 Apple 平台上转换并检查 Core AI 模型资产
- 对 .aimodel 函数做基准测试并导出可验证证据
- 将验证过的模型打包成 Swift 集成包供工程使用

## 场景标签

`模型评测` `推理引擎` · 领域:评测与运维

## 证据(README 行号)

> L10: A native SwiftUI workbench for discovering, converting, inspecting, running,
> L11: benchmarking, and packaging models with Apple's `CoreAI.framework`.
> L21: > Core AI is the asset, specialization, and runtime layer explored here. It is

## 星数曲线

```mermaid
xychart-beta
    title "rudrankriyam/Core-AI-Framework-Lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-28 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d2c7e93fca4b` · [字段定义](../../DATASET.md)*
