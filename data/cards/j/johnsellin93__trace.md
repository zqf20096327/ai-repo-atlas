# johnsellin93/trace

⭐ 28 · Shell · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/johnsellin93/trace) · 个人维护

**终端代码调查工具：为 AI 渐进采集代码证据**

面向开发者与 AI 协作调试的命令行工具：开发者描述问题后，由 AI 生成批量的 trace 命令，在终端执行以定向提取证据——仓库/文件 diff、符号实现、函数索引、jq 日志查询、HTML/CSS/JSON/YAML/Markdown 片段。每次成功提取会累积到调查上下文并自动复制到剪贴板，供粘贴回 AI 对话循环。支持 Python/C#/JS/TS 等语言与前端/配置/文档格式；必需依赖为 zsh 与 ripgrep，安装方式为 git clone 源码并加入 PATH，限定 zsh 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 生成批量 trace 命令做渐进式证据采集
- 仓库级函数索引提供确定性坐标供后续提取
- 覆盖 diff、符号、jq、HTML/CSS、JSON/YAML/Markdown 等证据类型
- 证据累积至 ~/.cache/trace 并自动复制到剪贴板（tmux/Wayland/X/macOS）

## 适用场景

- 版本升级引入回归时对比两个仓库逐步定位变更
- 配合 AI 对话对大仓库或大日志做定向调查而非整包上传
- 前端问题跨 HTML/CSS/JS/状态一次性采集证据

## 场景标签

 · 领域:开发者工具/AI 辅助开发

## 证据(README 行号)

> L15: The AI generates a batch of Trace commands based on your problem. You run them in your terminal, paste the accumula
> L354: The developer remains in control of execution while the model directs the investigation.

## 星数曲线

```mermaid
xychart-beta
    title "johnsellin93/trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81a9967c493e` · [字段定义](../../DATASET.md)*
