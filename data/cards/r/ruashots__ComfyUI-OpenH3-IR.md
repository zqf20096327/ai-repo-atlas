# ruashots/ComfyUI-OpenH3-IR

⭐ 38 · Python · Apache-2.0 · 推送 2026-08-23 · [GitHub](https://github.com/ruashots/ComfyUI-OpenH3-IR) · [官网](https://github.com/ruashots/open-h3-ir) · 个人维护

**ComfyUI 节点包：为 MiniMax H3 编译结构化 Context-IR 简报**

面向 ComfyUI 用户的四个自定义节点，封装 OpenH3-IR（MiniMax H3 的本地 Context-IR 层实现）：Main 节点接收自然语言提示与时长/画幅/镜头数等决策，Media 节点以命名媒体槽（@引用）管理图片/视频/音频并标注用途角色，Setup 节点配置 OpenAI 兼容语言模型端点与 H3 模型文件，Director 节点提供可选的摄影/灯光/节奏方案。安装时将 open-h3-ir 装入 ComfyUI 的 Python，全程进程内运行，无需额外服务。语言模型可本地或托管，需支持 OpenAI API；含视觉引用时模型需具备视觉能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个节点：Main/Media/Setup/Director，覆盖 H3 工作流的提示编译与媒体绑定
- 以 @名字 引用媒体、@speaks() 锁定逐字对白，替换文件时保持引用关系
- 支持角色/物体替换（编辑既有片段并替换其中主体）
- 安装即把 open-h3-ir 装入 ComfyUI 的 Python，进程内运行，无需第二服务

## 适用场景

- 在 ComfyUI 中用自然语言加参考图片/视频/音频驱动 MiniMax H3 生成视频
- 锁定必须逐字保留的台词并指定对白语言
- 通过编辑模式替换已有片段中的角色或物体并保持运镜与时机

## 场景标签

`视频生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: The ComfyUI-native way to use OpenH3-IR, the open local Context-IR implementation for MiniMax H3.
> L26: This repository is the ComfyUI side of the project: four nodes and a ready-to-run workflow built around the same Op
> L110: Your language model can be local or hosted. Anything speaking the OpenAI API works, including:

## 星数曲线

```mermaid
xychart-beta
    title "ruashots/ComfyUI-OpenH3-IR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e8c5dcfc617e` · [字段定义](../../DATASET.md)*
