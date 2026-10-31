# james2doyle/sublime-simpleai

⭐ 14 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/james2doyle/sublime-simpleai) · 个人维护

**Sublime Text 插件：在编辑器内调用 OpenAI 兼容 API 完成代码**

面向 Sublime Text 4 用户的插件：通过命令面板或快捷键调用两个核心命令——对选区代码做补全（completion）和附加自然语言指令改写/问答（instruct），未选中时发送整个文件。后端可接入任意 OpenAI 兼容服务，默认设置面向 OpenRouter，也支持自托管 Ollama、LM Studio 等自定义 hostname。支持 reasoning_effort 参数与自定义提示片段（含 $OS/$SOURCE_CODE 等变量）。安装方式为 git clone 到 Packages 目录，需自行配置 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- completion / instruct 两个核心命令，支持自定义快捷键
- 可接入任意 OpenAI 兼容服务，默认面向 OpenRouter
- 支持自托管 Ollama / LM Studio 等自定义端点
- reasoning_effort 控制与含变量的自定义提示片段

## 适用场景

- 在 Sublime Text 内对选区代码做补全或按提示改写
- 在编辑器里提问代码与编程概念
- 接自托管模型做本地代码辅助

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: Simple AI is a powerful Sublime Text plugin that integrates AI directly into your editor (but only when you want it)
> L45: Simple AI can use any OpenAI API compatible service. The easiest way to get access to the most models, in my experi

## 星数曲线

```mermaid
xychart-beta
    title "james2doyle/sublime-simpleai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0a0167f62fbd` · [字段定义](../../DATASET.md)*
