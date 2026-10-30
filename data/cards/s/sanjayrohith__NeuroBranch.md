# sanjayrohith/NeuroBranch

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/sanjayrohith/NeuroBranch) · 个人维护

**可视化搭建神经网络并同步生成 PyTorch 代码的桌面工具**

Electron 桌面应用：在画布上以 100+ 类型化可执行卡片拼装神经网络架构，图与生成的 PyTorch 代码双向同步，可在本地 Python 3 运行时逐步执行并查看张量。内置受限的 'Ask NeuroBranch' 规划器，用自然语言描述架构后生成可审计的结构化计划，经本地校验后应用；AI 部分需连接 ChatGPT（OpenAI Codex App Server）或 OpenAI API key，图编辑与执行无需账号。草稿、自定义卡片与预设存于本地 SQLite。作者自述为个人项目、早期演进的 MVP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 100+ 类型化卡片拖拽拼装，类型不兼容的端口无法连接
- 图与生成 PyTorch 双向同步，本地 Python 运行时可逐步执行
- Ask NeuroBranch 受限规划器：输出结构化计划，校验通过且可选人工审批后才应用
- 提供 macOS/Windows/Linux 一键安装脚本，安装包经 SHA-256 校验且本地从源码构建

## 适用场景

- 以可视化方式理解与搭建 GPT-like、MoE、ViT 等架构
- 让 AI 规划器根据自然语言描述生成架构图并审查后应用
- 导出架构 SVG 图或生成的 Python 代码用于学习与开发

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L4: Snap typed blocks together on a canvas, watch the **PyTorch write itself**, step through execution tensor-by-tensor,
> L62: The graph is the source of truth, but it isn't a drawing — it compiles to real PyTorch and runs on a real
> L44: |**Ask**|Describe an architecture in plain English; **Ask NeuroBranch** plans it, wires only compatible ports, and 

## 星数曲线

```mermaid
xychart-beta
    title "sanjayrohith/NeuroBranch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cafa380da922` · [字段定义](../../DATASET.md)*
