# kdandy/invisibleCoder

⭐ 13 · TypeScript · NOASSERTION · 推送 2026-03-19 · [GitHub](https://github.com/kdandy/invisibleCoder) · 个人维护

**隐形桌面应用：截屏分析编程面试题并生成解答**

基于 Electron/React/TypeScript 的隐形桌面应用，通过全局快捷键截取面试题目截图，调用 OpenAI GPT-4o/GPT-4o-mini Vision API 提取题目、生成含时空复杂度分析的解答并辅助调试；窗口可对部分屏幕共享软件不可见，全部处理在本地进行，仅 API 调用外发。需用户自带 OpenAI API key，从源码运行（Node.js v16+、npm install、平台脚本），可自行扩展 Claude/Deepseek 等模型。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截屏队列 + GPT-4 Vision 提取题目并生成解答与调试分析
- 窗口对多数屏幕捕获方式不可见，支持透明度/缩放/移动快捷键
- 自带 API key、本地处理，按阶段选择 GPT-4o 或 GPT-4o-mini
- 可通过修改 ProcessingHelper.ts 接入 Claude/Deepseek 等其他模型

## 适用场景

- 技术面试中隐形截屏题目并获取 AI 解答与调试建议
- 作为付费面试辅助工具的开源替代自行定制
- 学习 Electron + OpenAI Vision API 的应用开发

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L60: - 🤖 AI-Powered Analysis: Automatically extracts and analyzes coding problems using GPT-4o
> L238:  - AI extracts problem requirements from the screenshots using GPT-4 Vision API

## 星数曲线

```mermaid
xychart-beta
    title "kdandy/invisibleCoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7f30c38bb039` · [字段定义](../../DATASET.md)*
